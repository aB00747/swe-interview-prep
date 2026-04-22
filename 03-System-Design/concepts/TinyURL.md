# URL Shortener System Design

## 1. API Design (REST APIs)

### ➤ Create Short URL

POST: `/create-url`
- params:
  - long url
  - Status code: 201 created

### ➤ Redirect to Original URL

GET: `/short-url`
- params:
  - status code: 301 Permanent Redirect


|Funtional Requirement  | Non Functional Requirement    |
|:----------------------:|:------------------------------:|
|Give a long URL create a short URL|Very Low Latency                         |
|Given a short URL redirect to long URL| Very High Availability |

```text
LONG URL -> SHORT URL -> LONG URL
```

Schema:
- long URL `string`
- short-url `string`
- created_at `timestamp`

## Key Question

### Q1. How long should the URL be?

e.g.

1,000 URL generate per second

```text
so, 1,000 * 60 * 60 * 24 * 365

31.5 billion url created each year
            ↓
10 to 1 read to write request means 300 billion read per year

```

### Q2. What character can we use?

Alphanumric 

We use **Base62 encoding**:
- A–Z → 26 characters
- a–z → 26 characters
- 0–9 → 10 characters

Total = **62 characters**

Unique short URLs

## Capacity Calculation

| Length | Combinations |
|:------:|:-------------|
| 1 char | 62 |
| 2 char | 3,844 |
| 6 char | ~56 billion |
| 7 char | ~3.5 trillion |

## High Level System Design

```text
      Client
        ↓
    Load Balancer
        ↓
    Web Servers
        ↓
    Database
```

> what our solution to this 

```text
      Client
        ↓
    Load Balancer
        ↓
    Web Servers
        ↓
    Count Cache (In-memory / Redis)
        ↓
    Database
```
---


## Description of Components

### Client
- Sends requests to create or access short URLs

---

### Load Balancer
- Distributes incoming traffic evenly across web servers

---

### Web Servers
- Handles API requests
- Generates / resolves short URLs
- Communicates with cache before hitting database

---

### Count Cache (Important Layer)
- Stores frequently accessed counts (e.g., URL access count)
- Reduces database load
- Improves performance and latency
- Can be implemented using:
  - In-memory cache (e.g., LRU cache)
  - Distributed cache (e.g., Redis)

---

### Database
- Stores permanent mapping:
  - long_url
  - short_url
  - metadata (created_at, etc.)
- Source of truth

## Problem with Count Cache

Adding a **Count Cache** layer can introduce a new issue:

### Collision / Redundancy Problem

Multiple servers may read the same cached value simultaneously and update it independently.

Example:

```text
Request 1 → Server 1 → reads count = 10 from Redis
Request 2 → Server 2 → reads count = 10 from Redis

Server 1 increments → 11
Server 2 increments → 11
``` id="collision_example"

Both servers write back:

```text
Server 1 → Redis = 11
Server 2 → Redis = 11
``` id="collision_writeback"

### Expected Result

```text
12
``` id="expected_result"

### Actual Result

```text
11
``` id="actual_result"

This creates:

- **Data collision**
- **Lost updates**
- **Redundant writes**
- **Inconsistent count values**

---

## Visual Representation

```text
          ┌──────────────┐
Request → │   Server 1   │ ── reads 10 ──┐
          └──────────────┘               │
                                         ▼
                                     ┌────────┐
                                     │ Redis  │
                                     └────────┘
                                         ▲
          ┌──────────────┐               │
Request → │   Server 2   │ ── reads 10 ──┘
          └──────────────┘
``` 
id="visual_collision"

---

## Root Cause

The issue occurs because the **read → modify → write** operation is **not atomic**.

# Next Level Iteration: Using Zookeeper for ID Generation

---

## Updated System Design

```text
System → Load Balancer → Web Servers → Database
                         │
                         │
                         └───────────────┐
                                         │
                                         ▼
                                   Zookeeper
                            ┌──────────────────────┐
                            │ 0 - 1,000,000        │
                            │ 1,000,001 - 2,000,000│
                            │ 2,000,001 - 3,000,000│
                            └──────────────────────┘
``` 
id="zk_arch"

---

## Range Allocation

Each server gets a fixed range of IDs:

| Range | Assigned Server |
|-------|-----------------|
| 0 - 1,000,000 | Server 1 |
| 1,000,001 - 2,000,000 | Server 2 |
| 2,000,001 - 3,000,000 | Server 3 |

This is called the **Range Technique**.

---

## Why Use Zookeeper?

:contentReference[oaicite:0]{index=0} is used for:

- Centralized service for maintaining configuration information  
- Providing distributed synchronization  
- Providing distributed notifications  

Instead of asking for a new ID on every request, servers request a **range of IDs**.

This reduces load significantly.

---

## Problem Scenario

### What if Zookeeper assigns a range and the server instantly dies?

Example:

- Server 1 gets range `0 - 1,000,000`
- Server crashes before using the range

### Result:

- That entire range may remain unused
- Millions of requests may fail or be lost temporarily

---

## Is Zookeeper a Single Point of Failure?

Yes, if only one instance exists.

### Solution:

Use multiple Zookeeper instances in a cluster.

Benefits:

- High availability  
- Fault tolerance  
- Leader election support  

Also, Zookeeper receives fewer read requests because:

- Web servers request **ranges** only occasionally
- Unlike Count Cache, they do not hit Zookeeper for every request

This solution scales much better.

---

# Scaling Databases

As traffic grows, databases also need scaling.

## Types of Databases

- SQL Databases  
- NoSQL Databases  
- Graph Databases  

---

## SQL Option

Example: :contentReference[oaicite:1]{index=1}

Advantages:

- ACID compliance  
- Strong consistency  

Scaling:

- Sharding can be used  

Tradeoff:

- Slightly less performant at massive scale

---

## NoSQL Option

Example: :contentReference[oaicite:2]{index=2}

Advantages:

- Easily handles massive scale  
- High write throughput  
- Better horizontal scaling  

---

## Distributed Cache

To reduce DB load further:

Use distributed cache systems like:

- :contentReference[oaicite:3]{index=3}  
- :contentReference[oaicite:4]{index=4}  

Benefits:

- Faster reads  
- Reduced database pressure  

---

# Workflow

## POST Request Flow

```text
Client
   ↓
Load Balancer
   ↓
Web Server
   ↓
Generate short URL using allocated range
   ↓
Store mapping in Database
``` id="post_flow"

---

## GET Request Flow

```text
Client
   ↓
Load Balancer
   ↓
Web Server
   ↓
Check Cache
   ↓
Database (if cache miss)
   ↓
Redirect to Long URL
``` 
id="get_flow"

---

# Additional Features

## 1. Analytics

Track:

- Count of each URL  
- Popular URLs for caching  
- IP address for location analytics  
- Determine optimal cache/server placement  
- Fix Hotkey problem like twitter has

---

## 2. Rate Limiting

Prevent abuse such as:

- DDoS attacks  
- Malicious spam requests  

Techniques:

- Token bucket  
- Sliding window  

---

## 3. Security

Prevent predictable URLs by:

- Adding randomness to short URLs  
- Hashing / salting IDs  

This makes URL guessing harder for hackers.

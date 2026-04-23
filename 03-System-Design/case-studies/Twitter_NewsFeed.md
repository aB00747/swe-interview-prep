# 🐦 Twitter / Newsfeed System Design

## 📌 Functional Requirements

* Feed publishing (post tweets)
* Feed retrieval (view timeline)
* Follow/unfollow users
* Notification & analytics service

## ⚙️ Non-Functional Requirements

* High availability
* Minimal latency
* Scalability
* Fault tolerance
* Consistency (eventual consistency is acceptable)

---

## 📊 Scale Estimation

Assumptions:

* **20 million DAU (Daily Active Users)**
* Each user posts **~5 tweets/day**

### Write Throughput

```
20M users × 5 tweets/day = 100M tweets/day
100M / (24 × 60 × 60) ≈ 1,157 ≈ 1K tweets/sec
```

### Read Throughput

* Assume **100:1 read-to-write ratio**

```
1K writes/sec × 100 = 100K reads/sec
```

### Storage Estimation

* Assume **100 bytes per tweet**

```
100M tweets/day × 100 bytes = 10 GB/day
10 GB × 365 ≈ 3.65 TB/year
```

---

## 🗄️ Data Model

### Tables Overview

#### `USERS`

| Column    | Type      | Notes       |
| --------- | --------- | ----------- |
| id        | UUID      | Primary Key |
| email     | varchar   |             |
| dob       | date      |             |
| createdAt | timestamp |             |

#### `TWEETS`

| Column    | Type      | Notes       |
| --------- | --------- | ----------- |
| id        | UUID      | Primary Key |
| userID    | UUID      | Foreign Key |
| type      | enum      |             |
| content   | varchar   |             |
| createdAt | timestamp |             |

#### `FOLLOWERS`

| Column     | Type | Notes       |
| ---------- | ---- | ----------- |
| id         | UUID | Primary Key |
| followerID | UUID | FK → USERS  |
| followeeID | UUID | FK → USERS  |

#### `FEEDS`

| Column    | Type      | Notes       |
| --------- | --------- | ----------- |
| id        | UUID      | Primary Key |
| userID    | UUID      | Foreign Key |
| updatedAt | timestamp |             |

#### `FEEDS_TWEETS`

| Column  | Type | Notes       |
| ------- | ---- | ----------- |
| id      | UUID | Primary Key |
| tweetID | UUID | FK → TWEETS |
| feedID  | UUID | FK → FEEDS  |

---

## 🔗 Relationships

* A user can post many tweets
* A user can follow many users
* A feed belongs to a user
* A feed contains many tweets (via join table)

---

## 🌐 API Design

### REST APIs

#### 1. Create Tweet

```
POST /tweet
```

**Params:**

* `content`
* `auth_token`

#### 2. Get Feed

```
GET /feed
```

**Params:**

* `auth_token`

---

### 🔷 GraphQL API

#### Key Features

* Single endpoint
* Client specifies response shape
* Prevents over-fetching / under-fetching

#### Concepts

* **Query** → Read data (GET)
* **Mutation** → Write/update data (POST/PUT/PATCH)

#### Example Query

```graphql
query feed($userID: UUID!) {
  feed(userID: $userID) {
    feeds_tweets {
      tweet_id
    }
  }
}
```

---

## ⚡ Feed Publishing Strategies

### 📣 Fanout

Fanout is the process of distributing a new tweet to followers.

### 1. Fanout on Write (Push Model)

* When a user tweets, push it to all followers' feeds
* **Pros:**

  * Fast read (precomputed feed)
* **Cons:**

  * Expensive write (especially for users with many followers)

---

### 2. Fanout on Read (Pull Model)

* Build feed at read time by fetching tweets from followed users
* **Pros:**

  * Cheap writes
* **Cons:**

  * Slow reads

---

### 🧠 Hybrid Approach (Recommended)

* Use **fanout-on-write** for normal users
* Use **fanout-on-read** for high-follower users (celebrities)

---

## ✅ Summary

* System handles **~1K writes/sec** and **~100K reads/sec**
* Storage grows ~**3.65 TB/year**
* Core challenge: **efficient feed generation**
* Best practice: **hybrid fanout strategy + caching**


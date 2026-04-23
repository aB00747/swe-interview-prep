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

## Feed Publishing in News Feed System Design

Feed publishing is the process of distributing newly created content (e.g., tweets/posts) to followers.

---

### 1. Fanout on Write (Push Model)

In this approach, when a user publishes a tweet/post, it is immediately pushed to all followers’ feed caches.

### Diagram

```text
                +----------------+
Mobile/User --->| Tweet Service   |
                +----------------+
                         |
                         v
                +----------------------+
                | Followers Feed Cache |
                +----------------------+
                  /      |        \
                 v       v         v
              User A   User B    User C
````

### Explanation

* User posts a tweet.
* Tweet Service receives it.
* System finds all followers.
* Pushes the tweet into each follower’s News Feed Cache.

This means the news feed is **precomputed**.

When followers open the app:

```text
User -> Feed Cache -> Response
```

No need to compute feed at read time.

#### Pros

* Very fast reads
* Feed is already generated
* Real-time user experience

#### Cons

* Wastes resources for inactive users
* Expensive writes
* **Hot Key Problem**:

  * If a celebrity with millions of followers posts,
  * system must write to millions of caches instantly.

---

### 2. Fanout on Read (Pull Model)

Instead of pushing content at write time, generate the feed when the user requests it.

### Diagram

```text
User A ----\
User B -----\ 
User C ------> +------------------+
               | News Feed Service |
               +------------------+
                        |
                        v
                 +-------------+
                 | Database    |
                 +-------------+
                        |
                        v
                 Generate Feed
                        |
                        v
                 Return Response
```

### Explanation

* User opens app.
* Request goes to News Feed Service.
* Service fetches recent posts from followed users.
* Feed is computed dynamically.

#### Pros

* Saves resources for inactive users
* No expensive writes
* Avoids celebrity hot-key issue

#### Cons

* Slower reads than push model
* Feed generation takes time

---

### 3. Hybrid Approach (Recommended)

Use both models.

* **Push model** for normal users
* **Pull model** for celebrities / high follower accounts

### Diagram

```text
                   +----------------+
                   | Tweet Service   |
                   +----------------+
                     /            \
                    /              \
                   v                v
       Normal User Posts       Celebrity Posts
              |                     |
              v                     v
      Push to Feed Cache      Store in DB only
                                    |
                                    v
                          Fetch on Read
```

### Example

* Your friend posts → pushed instantly to your feed.
* Celebrity posts → fetched dynamically when you open app.

This balances:

* Read speed
* Write cost
* Scalability

---

## Architecture Overview

## Diagram

```text
                +------------------+
                |      Client      |
                +------------------+
                         |
                         v
                +------------------+
                | Load Balancer    |
                +------------------+
                         |
      ------------------------------------------------
      |                |                |            |
      v                v                v            v
+------------+   +--------------+  +------------+  +----------------+
| User       |   | News Feed    |  | Tweet      |  | Notification   |
| Service    |   | Service      |  | Service    |  | Service        |
+------------+   +--------------+  +------------+  +----------------+
      |                |                |                 |
      v                v                v                 v
+------------+   +--------------+  +------------+   +----------------+
| User Cache |   | Feed Cache   |  | Tweet DB   |   | Email/SMS/Push |
+------------+   +--------------+  +------------+   +----------------+
      |
      v
+-------------+
| User DB     |
+-------------+

                +------------------+
                | Kafka / Queue    |
                +------------------+
                         |
      -----------------------------------------------
      |                                             |
      v                                             v
+----------------+                        +----------------+
| Analytics      |                        | Background Jobs|
| Service        |                        | Workers        |
+----------------+                        +----------------+
```

---

# Service Breakdown

## 1. User Service

Handles:

* user profile
* followers/following
* authentication-related data

### Components

```text
User Service
   |
   +--> User Cache
   |
   +--> User Database
```

Cache is used for fast retrieval.

---

## 2. Graph Database

Useful for relationship-heavy queries.

Example:

* LinkedIn connections
* Mutual followers
* “People you may know”

Examples:

* Neo4j
* Amazon Neptune

---

## 3. News Feed Service

Responsible for:

* publishing feeds
* retrieving feeds

Interacts with:

* Tweet Service
* Cache
* Database

---

## 4. Tweet Service

Handles:

* posting tweets
* liking tweets
* retweeting tweets
* storing tweet data

---

## 5. Notification Service

Push notifications to users.

Examples:

* Email
* SMS
* Firebase Cloud Messaging
* Apple Push Notification Service

---

## 6. Kafka / Queue

Kafka is a distributed event streaming platform.

Used for:

* decoupling services
* asynchronous processing
* scaling independently

Example flow:

```text
Tweet Created -> Kafka -> Feed Worker / Notification Worker / Analytics
```

---

## 7. Analytics Service

Tracks:

* popular URLs
* user engagement
* impressions
* likes/comments/retweets
* dwell time (linger time)

Can use:

* Spark
* Hadoop
* BigQuery

to improve recommendation system and UX.

---

# Additional Design Considerations

## Keep Services Stateless

Each request should be independent.

Benefits:

* easy horizontal scaling
* easier failover

---

## Multiple Instances of Each Service

```text
Service A (Instance 1)
Service A (Instance 2)
Service A (Instance 3)
```

If one fails, others continue serving traffic.

---

## Multi Data Center Deployment

Spread services geographically.

Benefits:

* lower latency
* disaster recovery

---

## Read Replicas

To handle high read load.

```text
Primary DB -> Replica 1 -> Replica 2
```

---

## Cache Aggressively

Examples:

* user profile cache
* feed cache
* trending topics cache

Need cache expiration / invalidation policy.

---

## Monitor Metrics

Track:

* QPS
* CPU / Memory
* DB latency
* Cache hit rate

Helps autoscaling and capacity planning.

```

This structure is more readable and interview-friendly.
```



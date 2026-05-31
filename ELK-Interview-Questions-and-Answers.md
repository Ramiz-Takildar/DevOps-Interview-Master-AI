# ELK Stack Interview Questions & Answers

## 📋 Table of Contents

- [Overview](#overview)
- [Interview Preparation Strategy](#interview-preparation-strategy)
- [Core Concepts & Architecture](#core-concepts--architecture)
- [Elasticsearch Fundamentals](#elasticsearch-fundamentals)
- [Logstash & Data Processing](#logstash--data-processing)
- [Kibana & Visualization](#kibana--visualization)
- [Beats & Data Shippers](#beats--data-shippers)
- [Index Management & ILM](#index-management--ilm)
- [Search & Queries](#search--queries)
- [Performance & Scaling](#performance--scaling)
- [Security & Access Control](#security--access-control)
- [Troubleshooting & Operations](#troubleshooting--operations)
- [Production Best Practices](#production-best-practices)
- [Quick Reference Guide](#quick-reference-guide)

---

## Overview

### Purpose
This comprehensive guide provides 100 carefully curated ELK Stack interview questions designed for **Senior DevOps Engineers, SREs, and Platform Engineers**. Each question includes practical, production-ready answers demonstrating real-world log management expertise.

### Target Audience
- **Senior DevOps Engineers** implementing centralized logging
- **Site Reliability Engineers** managing observability platforms
- **Platform Engineers** building log aggregation solutions
- **Technical Leads** conducting interviews

### What Makes This Guide Different
- ✅ **Production-focused answers** with real-world scenarios
- ✅ **Architecture patterns** for scalable deployments
- ✅ **Performance optimization** strategies
- ✅ **Security best practices** for enterprise environments
- ✅ **Troubleshooting approaches** for common issues

---

## Interview Preparation Strategy

### Recommended Study Approach

#### Week 1-2: Foundation Building
1. **Core Concepts** (Questions 1-25)
   - Understand ELK architecture
   - Learn Elasticsearch basics
   - Master data flow concepts

2. **Daily Practice**
   - Read 10-15 questions per day
   - Set up local ELK stack
   - Practice with sample logs

#### Week 3-4: Advanced Topics
1. **Processing & Visualization** (Questions 26-50)
   - Master Logstash pipelines
   - Learn Kibana dashboards
   - Understand data transformation

2. **Index Management** (Questions 51-75)
   - Learn ILM policies
   - Practice shard management
   - Understand retention strategies

#### Week 5-6: Production Readiness
1. **Operations & Security** (Questions 76-100)
   - Understand scaling patterns
   - Learn security implementation
   - Practice troubleshooting

### Interview Answer Framework

| Component | Description |
|-----------|-------------|
| **Definition** | Clear explanation of the concept |
| **Purpose** | Why it matters in production |
| **Implementation** | Practical example or configuration |
| **Considerations** | Trade-offs and best practices |
| **Troubleshooting** | Common issues and solutions |

### Key Interview Success Factors

#### Technical Depth
- Explain **ELK architecture** components
- Demonstrate **query optimization**
- Discuss **scaling strategies**
- Show **security awareness**

#### Red Flags to Avoid
- ❌ Not understanding shard management
- ❌ Ignoring performance implications
- ❌ No security considerations
- ❌ Lack of production experience
- ❌ Not knowing troubleshooting approaches

---

## Core Concepts & Architecture

### 1. What is the ELK Stack?

**Answer:**

The **ELK Stack** is a collection of three open-source products: **Elasticsearch**, **Logstash**, and **Kibana**, used for centralized logging, search, and visualization.

**Components:**
- **Elasticsearch:** Distributed search and analytics engine
- **Logstash:** Data processing pipeline for ingestion and transformation
- **Kibana:** Visualization and exploration interface

**Modern Stack (Elastic Stack):**
```
Beats → Logstash → Elasticsearch → Kibana
  ↓         ↓            ↓            ↓
Collect   Process     Store      Visualize
```

**Why ELK is Popular:**
- Centralized log management
- Real-time search and analysis
- Scalable architecture
- Rich visualization capabilities
- Open-source with enterprise options

---

### 2. What is Elasticsearch?

**Answer:**

**Elasticsearch** is a distributed, RESTful search and analytics engine built on Apache Lucene.

**Key Features:**
- **Full-text search** with relevance scoring
- **Distributed architecture** for scalability
- **Near real-time** indexing and search
- **RESTful API** for easy integration
- **Schema-free** JSON documents

**Use Cases:**
- Log and event data analysis
- Full-text search
- Security analytics
- Business analytics
- Application monitoring

---

### 3. What is Logstash?

**Answer:**

**Logstash** is a server-side data processing pipeline that ingests, transforms, and forwards data.

**Pipeline Stages:**
```
Input → Filter → Output
  ↓       ↓        ↓
Collect Transform Forward
```

**Common Inputs:** Files, Beats, Kafka, HTTP, Syslog
**Common Filters:** Grok, Mutate, Date, GeoIP
**Common Outputs:** Elasticsearch, Kafka, S3, File

---

### 4. What is Kibana?

**Answer:**

**Kibana** is the visualization layer for Elasticsearch, providing search, visualization, and dashboard capabilities.

**Key Features:**
- **Discover:** Interactive log exploration
- **Visualize:** Create charts and graphs
- **Dashboard:** Combine visualizations
- **Canvas:** Pixel-perfect presentations
- **Maps:** Geospatial data visualization

---

### 5. What are Beats?

**Answer:**

**Beats** are lightweight data shippers that send data to Logstash or Elasticsearch.

**Common Beats:**
- **Filebeat:** Log files
- **Metricbeat:** System and service metrics
- **Packetbeat:** Network data
- **Winlogbeat:** Windows event logs
- **Heartbeat:** Uptime monitoring
- **Auditbeat:** Audit data

---

## Elasticsearch Fundamentals

### 6. What is an Elasticsearch cluster?

**Answer:**

A **cluster** is a collection of one or more nodes that together hold all data and provide indexing and search capabilities.

**Cluster Components:**
```
Cluster
├── Node 1 (Master-eligible, Data)
├── Node 2 (Data)
├── Node 3 (Data)
└── Node 4 (Coordinating)
```

---

### 7. What are the different node types?

**Answer:**

**Node Types:**

| Type | Role | Purpose |
|------|------|---------|
| **Master** | Cluster management | Manages cluster state, shard allocation |
| **Data** | Store data | Holds shards, executes queries |
| **Ingest** | Pre-processing | Runs ingest pipelines |
| **Coordinating** | Request routing | Routes requests, merges results |
| **ML** | Machine learning | Runs ML jobs |

---

### 8. What is an index?

**Answer:**

An **index** is a collection of documents with similar characteristics.

**Example:**
```
logs-2024.01.01  ← Index
├── Document 1 (log entry)
├── Document 2 (log entry)
└── Document 3 (log entry)
```

---

### 9. What is a document?

**Answer:**

A **document** is a JSON object stored in an index, representing a single record.

**Example:**
```json
{
  "@timestamp": "2024-01-01T10:00:00Z",
  "level": "ERROR",
  "service": "api",
  "message": "Connection timeout",
  "host": "server-1"
}
```

---

### 10. What is a shard?

**Answer:**

A **shard** is a partition of an index that allows data distribution across nodes.

**Types:**
- **Primary shard:** Original shard where data is written
- **Replica shard:** Copy of primary for redundancy

**Example:**
```
Index: logs-2024.01.01
├── Primary Shard 0 (Node 1)
│   └── Replica Shard 0 (Node 2)
├── Primary Shard 1 (Node 2)
│   └── Replica Shard 1 (Node 3)
└── Primary Shard 2 (Node 3)
    └── Replica Shard 2 (Node 1)
```

---

### 11. What is cluster health?

**Answer:**

**Cluster health** indicates the status of shards in the cluster.

**Health States:**
- **Green:** All primary and replica shards allocated
- **Yellow:** All primary shards allocated, some replicas missing
- **Red:** Some primary shards unallocated (data loss risk)

**Check Health:**
```bash
GET /_cluster/health

{
  "status": "green",
  "number_of_nodes": 3,
  "active_primary_shards": 15,
  "active_shards": 30
}
```

---

### 12. What is mapping?

**Answer:**

**Mapping** defines how documents and fields are stored and indexed.

**Example:**
```json
{
  "mappings": {
    "properties": {
      "@timestamp": {"type": "date"},
      "level": {"type": "keyword"},
      "message": {"type": "text"},
      "response_time": {"type": "integer"}
    }
  }
}
```

---

### 13. What is the difference between text and keyword types?

**Answer:**

| Feature | Text | Keyword |
|---------|------|---------|
| **Analysis** | Analyzed (tokenized) | Not analyzed (exact) |
| **Use Case** | Full-text search | Filtering, sorting, aggregations |
| **Example** | Log messages | Status codes, hostnames |

**Example:**
```json
{
  "message": {"type": "text"},      // "Error connecting to database"
  "status": {"type": "keyword"}     // "ERROR"
}
```

---

### 14. What is dynamic mapping?

**Answer:**

**Dynamic mapping** automatically detects and creates field mappings when new fields are encountered.

**Pros:**
- Easy to get started
- Flexible for varied data

**Cons:**
- Can create incorrect types
- May cause mapping explosions
- Inconsistent field types

**Best Practice:** Define explicit mappings for production.

---

### 15. What is an inverted index?

**Answer:**

An **inverted index** maps terms to documents containing them, enabling fast full-text search.

**Example:**
```
Term        → Documents
"error"     → [doc1, doc3, doc5]
"timeout"   → [doc1, doc4]
"database"  → [doc2, doc3]
```

---

## Logstash & Data Processing

### 16. What is a Logstash pipeline?

**Answer:**

A **pipeline** defines how data flows through Logstash: Input → Filter → Output.

**Example:**
```ruby
input {
  beats {
    port => 5044
  }
}

filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  date {
    match => [ "timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ]
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}
```

---

### 17. What is the Grok filter?

**Answer:**

**Grok** parses unstructured text into structured fields using patterns.

**Example:**
```ruby
filter {
  grok {
    match => {
      "message" => "%{IP:client_ip} %{WORD:method} %{URIPATHPARAM:request} %{NUMBER:response_code}"
    }
  }
}

# Input:  "192.168.1.1 GET /api/users 200"
# Output: client_ip=192.168.1.1, method=GET, request=/api/users, response_code=200
```

---

### 18. What is the Mutate filter?

**Answer:**

**Mutate** modifies fields (rename, convert, remove, add).

**Example:**
```ruby
filter {
  mutate {
    rename => { "old_field" => "new_field" }
    convert => { "response_time" => "integer" }
    remove_field => [ "temp_field" ]
    add_field => { "environment" => "production" }
  }
}
```

---

### 19. What is the Date filter?

**Answer:**

**Date** parses timestamps and sets the event time.

**Example:**
```ruby
filter {
  date {
    match => [ "timestamp", "ISO8601", "yyyy-MM-dd HH:mm:ss" ]
    target => "@timestamp"
  }
}
```

---

### 20. What are common Logstash inputs?

**Answer:**

**Common Inputs:**
- **Beats:** Receive from Filebeat, Metricbeat
- **File:** Read from log files
- **Kafka:** Consume from Kafka topics
- **HTTP:** Receive via HTTP endpoint
- **Syslog:** Receive syslog messages
- **JDBC:** Query databases

---

## Kibana & Visualization

### 21. What is Kibana Discover?

**Answer:**

**Discover** is the interface for searching and exploring documents.

**Features:**
- Interactive search
- Field filtering
- Time range selection
- Document inspection
- Saved searches

---

### 22. What is a Kibana index pattern (data view)?

**Answer:**

An **index pattern** (now called data view) defines which indices Kibana should query.

**Example:**
```
Pattern: logs-*
Matches: logs-2024.01.01, logs-2024.01.02, logs-2024.01.03
```

---

### 23. What visualization types does Kibana support?

**Answer:**

**Visualization Types:**
- **Line/Area/Bar charts:** Time-series data
- **Pie/Donut charts:** Proportions
- **Data tables:** Structured data
- **Metrics:** Single values
- **Tag clouds:** Term frequency
- **Heatmaps:** Density visualization
- **Maps:** Geospatial data

---

### 24. What is a Kibana dashboard?

**Answer:**

A **dashboard** is a collection of visualizations and saved searches.

**Best Practices:**
- Focus on specific use cases
- Use consistent time ranges
- Add filters for interactivity
- Organize logically
- Document purpose

---

### 25. What are Kibana Spaces?

**Answer:**

**Spaces** provide logical separation for dashboards, visualizations, and saved objects.

**Use Cases:**
- Team isolation
- Environment separation
- Multi-tenancy
- Access control

---

## Beats & Data Shippers

### 26. What is Filebeat?

**Answer:**

**Filebeat** is a lightweight shipper for forwarding and centralizing log data.

**Configuration:**
```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/*.log
    fields:
      environment: production

output.elasticsearch:
  hosts: ["localhost:9200"]
  index: "filebeat-%{+yyyy.MM.dd}"
```

---

### 27. What is Metricbeat?

**Answer:**

**Metricbeat** collects metrics from systems and services.

**Modules:**
- System (CPU, memory, disk)
- Docker
- Kubernetes
- Nginx
- MySQL
- Redis

---

### 28. What are Filebeat modules?

**Answer:**

**Modules** provide pre-built configurations for common log formats.

**Examples:**
- Apache
- Nginx
- MySQL
- System
- Elasticsearch

**Enable Module:**
```bash
filebeat modules enable nginx
filebeat setup
```

---

### 29. What is the difference between Filebeat and Logstash?

**Answer:**

| Feature | Filebeat | Logstash |
|---------|----------|----------|
| **Weight** | Lightweight | Heavier |
| **Purpose** | Log shipping | Data processing |
| **Processing** | Basic | Advanced |
| **Resource Usage** | Low | Higher |
| **Deployment** | Edge nodes | Central servers |

**Typical Architecture:**
```
Filebeat (edge) → Logstash (central) → Elasticsearch
```

---

### 30. What is backpressure handling in Beats?

**Answer:**

**Backpressure** occurs when output can't keep up with input.

**Handling:**
- Internal queuing
- Automatic retry
- Acknowledgment tracking
- Flow control

---

## Index Management & ILM

### 31. What is Index Lifecycle Management (ILM)?

**Answer:**

**ILM** automates index lifecycle through phases: Hot → Warm → Cold → Delete.

**Phases:**
- **Hot:** Active indexing and querying
- **Warm:** Read-only, less frequent queries
- **Cold:** Rarely queried, searchable snapshots
- **Delete:** Remove old data

**Example Policy:**
```json
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_size": "50GB",
            "max_age": "1d"
          }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "shrink": {"number_of_shards": 1},
          "forcemerge": {"max_num_segments": 1}
        }
      },
      "cold": {
        "min_age": "30d",
        "actions": {
          "searchable_snapshot": {"snapshot_repository": "my_repo"}
        }
      },
      "delete": {
        "min_age": "90d",
        "actions": {"delete": {}}
      }
    }
  }
}
```

---

### 32. What is index rollover?

**Answer:**

**Rollover** creates a new index when conditions are met (size, age, documents).

**Example:**
```json
{
  "conditions": {
    "max_age": "7d",
    "max_size": "50gb",
    "max_docs": 1000000
  }
}
```

---

### 33. What is an index template?

**Answer:**

**Index templates** define settings and mappings for new indices matching a pattern.

**Example:**
```json
{
  "index_patterns": ["logs-*"],
  "template": {
    "settings": {
      "number_of_shards": 3,
      "number_of_replicas": 1
    },
    "mappings": {
      "properties": {
        "@timestamp": {"type": "date"},
        "message": {"type": "text"}
      }
    }
  }
}
```

---

### 34. What is an index alias?

**Answer:**

An **alias** is a logical name pointing to one or more indices.

**Use Cases:**
- Zero-downtime reindexing
- Rollover workflows
- Read/write separation

**Example:**
```json
POST /_aliases
{
  "actions": [
    {"add": {"index": "logs-2024.01.01", "alias": "logs-current"}},
    {"remove": {"index": "logs-2023.12.31", "alias": "logs-current"}}
  ]
}
```

---

### 35. What is reindexing?

**Answer:**

**Reindexing** copies documents from one index to another.

**Use Cases:**
- Mapping changes
- Shard count changes
- Data migration

**Example:**
```json
POST /_reindex
{
  "source": {"index": "old_index"},
  "dest": {"index": "new_index"}
}
```

---

## Search & Queries

### 36. What is a term query?

**Answer:**

**Term query** matches exact values (keyword fields).

```json
{
  "query": {
    "term": {
      "status": "ERROR"
    }
  }
}
```

---

### 37. What is a match query?

**Answer:**

**Match query** performs full-text search (text fields).

```json
{
  "query": {
    "match": {
      "message": "connection timeout"
    }
  }
}
```

---

### 38. What is a bool query?

**Answer:**

**Bool query** combines multiple queries with must, should, filter, must_not.

```json
{
  "query": {
    "bool": {
      "must": [
        {"match": {"message": "error"}}
      ],
      "filter": [
        {"term": {"level": "ERROR"}},
        {"range": {"@timestamp": {"gte": "now-1h"}}}
      ],
      "must_not": [
        {"term": {"service": "test"}}
      ]
    }
  }
}
```

---

### 39. What is the difference between query and filter context?

**Answer:**

| Context | Scoring | Caching | Use Case |
|---------|---------|---------|----------|
| **Query** | Yes | No | Relevance search |
| **Filter** | No | Yes | Exact matching |

**Example:**
```json
{
  "query": {
    "bool": {
      "must": [{"match": {"message": "error"}}],     // Query context
      "filter": [{"term": {"status": "500"}}]        // Filter context
    }
  }
}
```

---

### 40. What are aggregations?

**Answer:**

**Aggregations** summarize data (counts, averages, percentiles).

**Types:**
- **Bucket:** Group documents (terms, date histogram)
- **Metric:** Calculate values (avg, sum, percentiles)
- **Pipeline:** Aggregate aggregation results

**Example:**
```json
{
  "aggs": {
    "errors_by_service": {
      "terms": {"field": "service"},
      "aggs": {
        "avg_response_time": {
          "avg": {"field": "response_time"}
        }
      }
    }
  }
}
```

---

## Performance & Scaling

### 41. How do you optimize Elasticsearch performance?

**Answer:**

**Optimization Strategies:**
1. **Proper shard sizing** (20-50GB per shard)
2. **Use filters** instead of queries when possible
3. **Disable unnecessary features** (_source, doc_values)
4. **Use bulk API** for indexing
5. **Optimize mappings** (disable _all, use appropriate types)
6. **Tune JVM heap** (50% of RAM, max 31GB)
7. **Use SSD storage**
8. **Implement ILM** for data lifecycle

---

### 42. What causes high heap usage?

**Answer:**

**Common Causes:**
- Too many shards
- Large aggregations
- Fielddata usage
- Heavy indexing
- Large queries
- Insufficient heap size

**Solutions:**
- Reduce shard count
- Use doc_values instead of fielddata
- Increase heap (up to 31GB)
- Optimize queries
- Use circuit breakers

---

### 43. What is the optimal shard size?

**Answer:**

**Guidelines:**
- **Target:** 20-50GB per shard
- **Avoid:** Too many small shards (overhead)
- **Avoid:** Too few large shards (inflexibility)

**Calculation:**
```
Daily data: 100GB
Retention: 30 days
Total: 3TB
Shard size: 30GB
Shards needed: 100 shards
```

---

### 44. How do you scale Elasticsearch?

**Answer:**

**Scaling Strategies:**

**Vertical Scaling:**
- Add more CPU/RAM/Disk to nodes
- Limited by hardware

**Horizontal Scaling:**
- Add more nodes to cluster
- Distribute shards across nodes
- Preferred for Elasticsearch

**Architecture:**
```
3 Master nodes (cluster management)
6 Data nodes (hot tier)
3 Data nodes (warm tier)
2 Coordinating nodes (load balancing)
```

---

### 45. What is hot-warm-cold architecture?

**Answer:**

**Tiered Storage:**

| Tier | Purpose | Hardware | Data Age |
|------|---------|----------|----------|
| **Hot** | Active indexing/search | Fast SSD, high CPU/RAM | 0-7 days |
| **Warm** | Read-only search | Standard SSD | 7-30 days |
| **Cold** | Rare access | HDD, searchable snapshots | 30-90 days |
| **Frozen** | Archive | Object storage | 90+ days |

**Benefits:**
- Cost optimization
- Performance optimization
- Flexible retention

---

## Security & Access Control

### 46. How do you secure Elasticsearch?

**Answer:**

**Security Measures:**
1. **Enable Security Features**
   ```yaml
   xpack.security.enabled: true
   xpack.security.transport.ssl.enabled: true
   xpack.security.http.ssl.enabled: true
   ```

2. **Authentication:** Built-in, LDAP, SAML, PKI
3. **Authorization:** Role-based access control (RBAC)
4. **Encryption:** TLS for transport and HTTP
5. **Audit Logging:** Track access and changes
6. **Network Security:** Firewall, VPN

---

### 47. What is RBAC in Elasticsearch?

**Answer:**

**Role-Based Access Control** restricts access based on user roles.

**Example:**
```json
{
  "cluster": ["monitor"],
  "indices": [
    {
      "names": ["logs-*"],
      "privileges": ["read", "view_index_metadata"]
    }
  ]
}
```

---

### 48. How do you handle sensitive data in logs?

**Answer:**

**Strategies:**
1. **Redaction at source:** Remove before logging
2. **Pipeline filtering:** Remove in Logstash/ingest
3. **Field-level security:** Restrict access to fields
4. **Encryption:** Encrypt sensitive fields
5. **Audit:** Track access to sensitive data

**Example:**
```ruby
filter {
  mutate {
    gsub => [
      "message", "password=\S+", "password=***REDACTED***",
      "message", "\d{16}", "****-****-****-****"
    ]
  }
}
```

---

### 49. What are API keys in Elasticsearch?

**Answer:**

**API keys** provide programmatic access with specific privileges.

**Create API Key:**
```json
POST /_security/api_key
{
  "name": "my-api-key",
  "role_descriptors": {
    "logs_reader": {
      "cluster": ["monitor"],
      "index": [
        {
          "names": ["logs-*"],
          "privileges": ["read"]
        }
      ]
    }
  }
}
```

---

### 50. How do you implement audit logging?

**Answer:**

**Audit Logging** tracks security-related events.

**Configuration:**
```yaml
xpack.security.audit.enabled: true
xpack.security.audit.logfile.events.include:
  - access_denied
  - authentication_failed
  - authentication_successful
```

---

## Troubleshooting & Operations

### 51. How do you troubleshoot missing logs?

**Answer:**

**Troubleshooting Steps:**
1. **Check source:** Verify logs are being generated
2. **Check shipper:** Filebeat/Logstash status
3. **Check pipeline:** Parsing errors, dropped events
4. **Check Elasticsearch:** Index exists, documents indexed
5. **Check Kibana:** Index pattern, time range, filters

**Commands:**
```bash
# Check Filebeat status
systemctl status filebeat
tail -f /var/log/filebeat/filebeat

# Check Elasticsearch indices
GET /_cat/indices?v

# Check document count
GET /logs-*/_count
```

---

### 52. How do you troubleshoot slow searches?

**Answer:**

**Investigation:**
1. **Profile queries:** Use _profile API
2. **Check shard count:** Too many small shards
3. **Review mappings:** Incorrect field types
4. **Check heap:** Memory pressure
5. **Analyze queries:** Expensive aggregations

**Profile Query:**
```json
GET /logs-*/_search
{
  "profile": true,
  "query": {...}
}
```

---

### 53. How do you troubleshoot red cluster health?

**Answer:**

**Steps:**
1. **Check unassigned shards:**
   ```bash
   GET /_cat/shards?v&h=index,shard,prirep,state,unassigned.reason
   ```

2. **Check disk space:**
   ```bash
   GET /_cat/allocation?v
   ```

3. **Check cluster allocation:**
   ```bash
   GET /_cluster/allocation/explain
   ```

4. **Common causes:**
   - Disk watermark exceeded
   - Node failure
   - Shard allocation disabled
   - Mapping conflicts

---

### 54. How do you troubleshoot high disk usage?

**Answer:**

**Solutions:**
1. **Implement ILM:** Automate retention
2. **Reduce replicas:** If acceptable
3. **Optimize mappings:** Disable _source if not needed
4. **Compress indices:** Use best_compression
5. **Delete old indices:** Manual cleanup
6. **Increase storage:** Add nodes/disks

**Check Disk Usage:**
```bash
GET /_cat/allocation?v
GET /_cat/indices?v&s=store.size:desc
```

---

### 55. How do you monitor Elasticsearch?

**Answer:**

**Key Metrics:**
```bash
# Cluster health
GET /_cluster/health

# Node stats
GET /_nodes/stats

# Index stats
GET /_stats

# Thread pool
GET /_cat/thread_pool?v

# Pending tasks
GET /_cat/pending_tasks?v
```

**Monitor:**
- Cluster health status
- JVM heap usage
- Disk space
- Indexing/search rate
- Query latency
- Rejected requests

---

## Production Best Practices

### 56. What are ELK deployment best practices?

**Answer:**

**Architecture:**
1. **Separate roles:** Master, data, coordinating nodes
2. **Minimum 3 master nodes:** Quorum
3. **Use dedicated master nodes:** Stability
4. **Implement hot-warm-cold:** Cost optimization
5. **Use load balancer:** Distribute requests

**Configuration:**
```yaml
# Master node
node.master: true
node.data: false
node.ingest: false

# Data node
node.master: false
node.data: true
node.ingest: false

# Coordinating node
node.master: false
node.data: false
node.ingest: false
```

---

### 57. What are index naming best practices?

**Answer:**

**Naming Convention:**
```
<type>-<environment>-<date>

Examples:
logs-prod-2024.01.01
metrics-staging-2024.01.01
audit-prod-2024.01
```

**Benefits:**
- Easy identification
- Supports ILM
- Enables filtering
- Facilitates cleanup

---

### 58. What are mapping best practices?

**Answer:**

**Best Practices:**
1. **Define explicit mappings:** Don't rely on dynamic
2. **Use appropriate types:** text vs keyword
3. **Disable unnecessary features:** _all, _source (if not needed)
4. **Use doc_values:** For aggregations/sorting
5. **Set index.mapping.total_fields.limit:** Prevent explosion

**Example:**
```json
{
  "mappings": {
    "_source": {"enabled": true},
    "dynamic": "strict",
    "properties": {
      "@timestamp": {"type": "date"},
      "level": {"type": "keyword"},
      "message": {"type": "text"},
      "service": {"type": "keyword"},
      "response_time": {"type": "integer"}
    }
  }
}
```

---

### 59. What are Logstash pipeline best practices?

**Answer:**

**Best Practices:**
1. **Use structured logging:** JSON format
2. **Minimize grok usage:** CPU intensive
3. **Use conditionals:** Process only relevant events
4. **Implement error handling:** Dead letter queue
5. **Monitor performance:** Pipeline stats

**Example:**
```ruby
filter {
  if [type] == "apache" {
    grok {
      match => { "message" => "%{COMBINEDAPACHELOG}" }
    }
  }
  
  if "_grokparsefailure" in [tags] {
    mutate {
      add_field => { "parse_error" => "true" }
    }
  }
}
```

---

### 60. What are retention best practices?

**Answer:**

**Strategy:**
1. **Define retention policy:** Based on compliance/needs
2. **Implement ILM:** Automate lifecycle
3. **Use tiered storage:** Hot-warm-cold
4. **Regular cleanup:** Delete old indices
5. **Monitor storage:** Prevent disk full

**Example Policy:**
- Hot: 7 days (active search)
- Warm: 30 days (occasional search)
- Cold: 90 days (rare access)
- Delete: After 90 days

---

### 61. How do you handle log volume spikes?

**Answer:**

**Strategies:**
1. **Queue buffering:** Kafka, Redis
2. **Rate limiting:** At source
3. **Sampling:** Reduce volume
4. **Horizontal scaling:** Add nodes
5. **Circuit breakers:** Prevent overload

---

### 62. What is your disaster recovery strategy?

**Answer:**

**DR Components:**
1. **Snapshots:** Regular backups
2. **Cross-cluster replication:** Real-time sync
3. **Configuration backup:** Templates, pipelines
4. **Documented procedures:** Recovery steps
5. **Regular testing:** Verify recovery

**Snapshot Configuration:**
```json
PUT /_snapshot/my_backup
{
  "type": "s3",
  "settings": {
    "bucket": "my-backup-bucket",
    "region": "us-east-1"
  }
}

PUT /_snapshot/my_backup/snapshot_1
{
  "indices": "logs-*",
  "include_global_state": false
}
```

---

### 63. How do you handle schema evolution?

**Answer:**

**Strategies:**
1. **Version indices:** logs-v1, logs-v2
2. **Use aliases:** Point to current version
3. **Reindex:** Migrate to new schema
4. **Backward compatibility:** Support old format
5. **Gradual migration:** Parallel processing

---

### 64. What are common ELK anti-patterns?

**Answer:**

**Anti-Patterns:**
- ❌ Too many small shards
- ❌ No ILM policy
- ❌ Dynamic mapping in production
- ❌ No monitoring
- ❌ Single node cluster
- ❌ No security
- ❌ Logging sensitive data
- ❌ No backup strategy

---

### 65. How do you optimize for cost?

**Answer:**

**Cost Optimization:**
1. **Implement ILM:** Tiered storage
2. **Reduce replicas:** Where acceptable
3. **Compress data:** best_compression codec
4. **Optimize retention:** Delete old data
5. **Use searchable snapshots:** Cold tier
6. **Right-size nodes:** Match workload

---

### 66. What is your approach to ELK governance?

**Answer:**

**Governance Framework:**
1. **Standards:** Naming, mapping, retention
2. **Access control:** RBAC, spaces
3. **Monitoring:** Performance, usage
4. **Documentation:** Runbooks, procedures
5. **Review process:** Regular audits

---

### 67. How do you handle multi-tenancy?

**Answer:**

**Strategies:**
1. **Index-based:** Separate indices per tenant
2. **Cluster-based:** Separate clusters
3. **Space-based:** Kibana spaces
4. **Field-based:** Filter by tenant field

**Example:**
```
tenant-a-logs-2024.01.01
tenant-b-logs-2024.01.01
```

---

### 68. What is your capacity planning approach?

**Answer:**

**Planning Factors:**
1. **Ingest rate:** Events per second
2. **Retention period:** Days/months
3. **Replication factor:** Copies
4. **Growth rate:** Trend analysis
5. **Query load:** Concurrent searches

**Calculation:**
```
Daily volume: 100GB
Retention: 30 days
Replicas: 1
Total: 100GB × 30 × 2 = 6TB
```

---

### 69. How do you test ELK changes?

**Answer:**

**Testing Strategy:**
1. **Dev environment:** Test changes
2. **Staging:** Validate with production-like data
3. **Canary deployment:** Gradual rollout
4. **Monitoring:** Watch metrics
5. **Rollback plan:** Quick recovery

---

### 70. What is your approach to ELK upgrades?

**Answer:**

**Upgrade Process:**
1. **Review release notes:** Breaking changes
2. **Backup:** Snapshots, configs
3. **Test in lower environment**
4. **Rolling upgrade:** Minimize downtime
5. **Monitor:** Watch for issues
6. **Rollback plan:** If needed

**Order:**
1. Elasticsearch
2. Kibana
3. Logstash
4. Beats

---

## Quick Reference Guide

### Essential Commands

```bash
# Cluster health
GET /_cluster/health

# List indices
GET /_cat/indices?v

# Index stats
GET /logs-*/_stats

# Search
GET /logs-*/_search
{
  "query": {
    "match": {"message": "error"}
  }
}

# Create index
PUT /logs-2024.01.01
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  }
}

# Delete index
DELETE /logs-2024.01.01

# Reindex
POST /_reindex
{
  "source": {"index": "old"},
  "dest": {"index": "new"}
}
```

### Common Queries

```json
// Term query (exact match)
{"query": {"term": {"status": "ERROR"}}}

// Match query (full-text)
{"query": {"match": {"message": "connection timeout"}}}

// Range query
{"query": {"range": {"@timestamp": {"gte": "now-1h"}}}}

// Bool query
{
  "query": {
    "bool": {
      "must": [{"match": {"message": "error"}}],
      "filter": [{"term": {"level": "ERROR"}}]
    }
  }
}

// Aggregation
{
  "aggs": {
    "by_service": {
      "terms": {"field": "service"}
    }
  }
}
```

### Configuration Snippets

```yaml
# Elasticsearch
cluster.name: my-cluster
node.name: node-1
network.host: 0.0.0.0
discovery.seed_hosts: ["host1", "host2"]
cluster.initial_master_nodes: ["node-1", "node-2", "node-3"]

# Logstash
input {
  beats { port => 5044 }
}
filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
}
output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}

# Filebeat
filebeat.inputs:
  - type: log
    paths: ["/var/log/*.log"]
output.elasticsearch:
  hosts: ["localhost:9200"]
```

---

## Final Interview Tips

### What Interviewers Look For

1. **Technical Depth**
   - Understanding of distributed systems
   - Shard management knowledge
   - Query optimization skills
   - Security awareness

2. **Production Experience**
   - Real-world examples
   - Troubleshooting stories
   - Scaling experience
   - Incident response

3. **Best Practices**
   - Index management
   - Performance optimization
   - Security implementation
   - Operational maturity

### Red Flags to Avoid

- ❌ Not understanding shards
- ❌ Ignoring security
- ❌ No monitoring strategy
- ❌ Poor retention planning
- ❌ Lack of production experience

### Success Factors

- ✅ Explain concepts clearly
- ✅ Provide production examples
- ✅ Discuss trade-offs
- ✅ Show systematic thinking
- ✅ Demonstrate troubleshooting skills
- ✅ Mention best practices

### Key Takeaways

- **Shard management is critical** - Balance size and count
- **ILM saves costs** - Automate data lifecycle
- **Security matters** - Protect sensitive logs
- **Monitoring is essential** - Track cluster health
- **Plan for scale** - Design for growth

---

**Good luck with your interview! Remember: Focus on understanding concepts deeply, practice with real ELK deployments, and always think about production implications.**

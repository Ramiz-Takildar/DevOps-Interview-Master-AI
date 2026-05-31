# Prometheus Interview Questions & Answers

## 📋 Table of Contents

- [Overview](#overview)
- [Interview Preparation Strategy](#interview-preparation-strategy)
- [Core Concepts & Architecture](#core-concepts--architecture)
- [Metrics & Data Model](#metrics--data-model)
- [PromQL & Querying](#promql--querying)
- [Alerting & Alertmanager](#alerting--alertmanager)
- [Exporters & Instrumentation](#exporters--instrumentation)
- [Service Discovery & Configuration](#service-discovery--configuration)
- [Scaling & High Availability](#scaling--high-availability)
- [Performance & Optimization](#performance--optimization)
- [Security & Best Practices](#security--best-practices)
- [Troubleshooting & Operations](#troubleshooting--operations)
- [Production Best Practices](#production-best-practices)
- [Quick Reference Guide](#quick-reference-guide)

---

## Overview

### Purpose
This comprehensive guide provides 100 carefully curated Prometheus interview questions designed for **Senior DevOps Engineers, SREs, and Platform Engineers**. Each question includes practical, production-ready answers that demonstrate real-world monitoring expertise.

### Target Audience
- **Senior DevOps Engineers** implementing observability solutions
- **Site Reliability Engineers** managing production monitoring
- **Platform Engineers** building monitoring infrastructure
- **Technical Leads** conducting interviews

### What Makes This Guide Different
- ✅ **Production-focused answers** with real-world scenarios
- ✅ **PromQL examples** for practical querying
- ✅ **Cardinality management** strategies
- ✅ **Scaling patterns** for enterprise environments
- ✅ **Troubleshooting approaches** for common issues

---

## Interview Preparation Strategy

### Recommended Study Approach

#### Week 1-2: Foundation Building
1. **Core Concepts** (Questions 1-25)
   - Understand time-series databases
   - Master metric types and labels
   - Learn pull-based architecture

2. **Daily Practice**
   - Read 10-15 questions per day
   - Practice PromQL queries
   - Set up local Prometheus instance

#### Week 3-4: Advanced Topics
1. **PromQL & Alerting** (Questions 26-50)
   - Master query functions
   - Design effective alerts
   - Understand Alertmanager workflows

2. **Exporters & Integration** (Questions 51-75)
   - Learn common exporters
   - Practice instrumentation
   - Integrate with Kubernetes

#### Week 5-6: Production Readiness
1. **Scaling & Operations** (Questions 76-100)
   - Understand cardinality challenges
   - Learn scaling strategies
   - Practice troubleshooting scenarios

### Interview Answer Framework

Use this structure for comprehensive answers:

| Component | Description | Example |
|-----------|-------------|---------|
| **Definition** | Clear explanation of the concept | "Prometheus is a time-series monitoring system..." |
| **Purpose** | Why it matters in production | "It enables real-time alerting and capacity planning..." |
| **Implementation** | Practical example or query | "We use rate() to calculate request rates..." |
| **Considerations** | Trade-offs and best practices | "High cardinality can impact performance..." |
| **Troubleshooting** | Common issues and solutions | "Check scrape targets and metric endpoints..." |

### Key Interview Success Factors

#### Technical Depth
- Explain **metric types** and when to use each
- Demonstrate **PromQL proficiency**
- Discuss **cardinality management**
- Show **scaling awareness**

#### Communication Style
- Start with clear definitions
- Use concrete PromQL examples
- Show systematic thinking
- Demonstrate operational experience

#### Red Flags to Avoid
- ❌ Not understanding cardinality impact
- ❌ Overusing high-cardinality labels
- ❌ Ignoring alert fatigue
- ❌ No retention strategy
- ❌ Lack of production monitoring experience

---

## Core Concepts & Architecture

### 1. What is Prometheus and why is it popular in cloud-native environments?

**Answer:**

Prometheus is an **open-source monitoring and alerting system** designed for reliability and scalability in dynamic environments. It's a time-series database optimized for metrics collection and querying.

**Key Characteristics:**
- **Pull-based model** for metric collection
- **Multi-dimensional data model** with labels
- **Powerful query language** (PromQL)
- **Built-in alerting** capabilities
- **Service discovery** for dynamic infrastructure

**Why Cloud-Native:**
- Native Kubernetes integration
- Handles dynamic service discovery
- Supports containerized workloads
- Integrates with cloud platforms
- Part of CNCF graduated projects

**Architecture Overview:**
```
┌─────────────────────────────────────────────────┐
│           Prometheus Server                      │
│  ┌──────────────┐  ┌──────────────┐            │
│  │   Retrieval  │  │   Storage    │            │
│  │   (Scraper)  │→ │   (TSDB)     │            │
│  └──────────────┘  └──────────────┘            │
│         ↓                  ↓                     │
│  ┌──────────────┐  ┌──────────────┐            │
│  │ Service      │  │   PromQL     │            │
│  │ Discovery    │  │   Engine     │            │
│  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────┘
         ↓                      ↓
    ┌─────────┐          ┌──────────────┐
    │ Targets │          │ Alertmanager │
    │ /metrics│          │              │
    └─────────┘          └──────────────┘
```

---

### 2. Explain the pull-based model and its advantages

**Answer:**

Prometheus uses a **pull-based model** where the server actively scrapes metrics from target endpoints at regular intervals.

**Advantages:**

| Benefit | Description |
|---------|-------------|
| **Centralized Control** | Prometheus controls scrape timing |
| **Target Health Visibility** | Can detect when targets are down |
| **Simpler Configuration** | Targets just expose metrics |
| **Better Security** | No push credentials needed |
| **Easier Debugging** | Can manually curl endpoints |

---

### 3. What is a time-series database?

**Answer:**

A **time-series database (TSDB)** stores data points indexed by time, optimized for metrics workloads.

**Time-Series Example:**
```
http_requests_total{method="GET", status="200"} 1234 @1622548800
http_requests_total{method="GET", status="200"} 1250 @1622548815
```

---

### 4. What is a metric in Prometheus?

**Answer:**

A **metric** is a named measurement with labels that creates time series.

```
metric_name{label1="value1", label2="value2"} value timestamp
```

---

### 5. What are labels and why are they important?

**Answer:**

**Labels** are key-value pairs that enable multi-dimensional data modeling.

**Good Labels:**
```promql
http_requests_total{method="GET", status="200", endpoint="/api"}
```

**Bad Labels (High Cardinality):**
```promql
http_requests_total{user_id="12345"}  # ❌ Millions of users
```

---

## Metrics & Data Model

### 6. What is metric cardinality?

**Answer:**

**Cardinality** is the number of unique time series created by label combinations.

**Example:**
```
method: 4 values × status: 10 values × endpoint: 20 values = 800 series
```

**High cardinality causes:**
- Memory exhaustion
- Slow queries
- Storage issues

---

### 7. What are the four Prometheus metric types?

**Answer:**

**1. Counter** - Monotonically increasing (requests, errors)
**2. Gauge** - Can go up/down (memory, temperature)
**3. Histogram** - Observations in buckets (latency)
**4. Summary** - Client-side quantiles

---

### 8. What is a Counter?

**Answer:**

A **Counter** only increases or resets to zero.

```python
requests_total = Counter('http_requests_total', 'Total requests')
requests_total.inc()
```

```promql
rate(http_requests_total[5m])  # Requests per second
```

---

### 9. What is a Gauge?

**Answer:**

A **Gauge** can increase or decrease.

```python
memory_usage = Gauge('memory_usage_bytes', 'Memory usage')
memory_usage.set(1024000000)
```

---

### 10. What is a Histogram?

**Answer:**

A **Histogram** samples observations into buckets.

```python
request_duration = Histogram(
    'http_request_duration_seconds',
    'Request duration',
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)
```

```promql
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
```

---

### 11. What is the difference between Histogram and Summary?

**Answer:**

| Feature | Histogram | Summary |
|---------|-----------|---------|
| **Quantiles** | Server-side | Client-side |
| **Aggregation** | ✅ Possible | ❌ Not possible |
| **Accuracy** | Approximate | Exact |
| **Preferred** | ✅ Yes | Rare cases |

---

### 12. When should you use each metric type?

**Answer:**

- **Counter:** Event counts (requests, errors)
- **Gauge:** Current values (memory, connections)
- **Histogram:** Latency, response sizes
- **Summary:** Exact quantiles (rarely needed)

---

## PromQL & Querying

### 13. What is PromQL?

**Answer:**

**PromQL** is Prometheus Query Language for selecting and aggregating time-series data.

```promql
# Instant vector
up

# Range vector
up[5m]

# With labels
up{job="api-server"}
```

---

### 14. What is `rate()` and when to use it?

**Answer:**

`rate()` calculates per-second average rate over a time range.

```promql
rate(http_requests_total[5m])  # Requests/sec over 5 minutes
```

**Use for:** Counters, alerting, dashboards

---

### 15. What is the difference between `rate()` and `irate()`?

**Answer:**

- **`rate()`:** Average over entire range (stable)
- **`irate()`:** Instant rate from last 2 samples (volatile)

```promql
rate(http_requests_total[5m])   # For alerts
irate(http_requests_total[5m])  # For debugging
```

---

### 16. What is `increase()`?

**Answer:**

`increase()` calculates total increase over a time range.

```promql
increase(http_requests_total[1h])  # Total requests in 1 hour
```

---

### 17. What are aggregation operators?

**Answer:**

```promql
sum(http_requests_total)                    # Total
avg(cpu_usage_percent)                      # Average
max(response_time_seconds)                  # Maximum
count(up == 1)                              # Count
sum by (endpoint) (rate(requests[5m]))      # Group by
```

---

### 18. What is `histogram_quantile()`?

**Answer:**

Calculates quantiles from histogram buckets.

```promql
# 95th percentile latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# 99th percentile by endpoint
histogram_quantile(0.99,
  sum by (endpoint, le) (rate(http_request_duration_seconds_bucket[5m]))
)
```

---

### 19. How do you calculate error rates?

**Answer:**

```promql
# Error rate
rate(http_requests_total{status=~"5.."}[5m])
/
rate(http_requests_total[5m])

# Error percentage
100 * (
  rate(http_requests_total{status=~"5.."}[5m])
  /
  rate(http_requests_total[5m])
)
```

---

### 20. How do you calculate CPU usage?

**Answer:**

```promql
# CPU usage percentage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Or
rate(node_cpu_seconds_total{mode!="idle"}[5m])
```

---

## Alerting & Alertmanager

### 21. What is an alerting rule?

**Answer:**

Defines conditions that trigger alerts.

```yaml
groups:
  - name: example_alerts
    rules:
      - alert: HighErrorRate
        expr: |
          rate(http_requests_total{status=~"5.."}[5m])
          /
          rate(http_requests_total[5m])
          > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
```

---

### 22. What is Alertmanager?

**Answer:**

**Alertmanager** handles alerts from Prometheus:
- **Grouping:** Combine similar alerts
- **Inhibition:** Suppress dependent alerts
- **Silencing:** Temporarily mute alerts
- **Routing:** Send to different receivers

---

### 23. What is alert grouping?

**Answer:**

Combines related alerts into single notifications.

```yaml
route:
  group_by: ['alertname', 'cluster']
  group_wait: 30s
  group_interval: 5m
```

**Without grouping:** 5 separate notifications
**With grouping:** 1 combined notification

---

### 24. What is alert inhibition?

**Answer:**

Suppresses alerts when related alerts are firing.

```yaml
inhibit_rules:
  - source_match:
      severity: 'critical'
      alertname: 'NodeDown'
    target_match:
      severity: 'warning'
    equal: ['instance']
```

---

### 25. What is alert silencing?

**Answer:**

Temporarily mutes alerts during maintenance.

```bash
amtool silence add \
  alertname=HighCPU \
  instance=server-1 \
  --duration=2h
```

---

## Exporters & Instrumentation

### 26. What is a Prometheus exporter?

**Answer:**

Exposes metrics from systems that don't natively support Prometheus format.

**Common exporters:**
- node_exporter (host metrics)
- blackbox_exporter (endpoint probing)
- mysqld_exporter (MySQL)
- postgres_exporter (PostgreSQL)

---

### 27. What is node_exporter?

**Answer:**

Exposes Linux/Unix host metrics.

```promql
# CPU usage
rate(node_cpu_seconds_total{mode!="idle"}[5m])

# Memory usage
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes

# Disk usage
node_filesystem_avail_bytes / node_filesystem_size_bytes
```

---

### 28. What is blackbox_exporter?

**Answer:**

Probes endpoints externally (HTTP, TCP, ICMP, DNS).

```yaml
modules:
  http_2xx:
    prober: http
    http:
      valid_status_codes: [200]
```

```promql
probe_success                    # 1 = success, 0 = failure
probe_http_duration_seconds      # Response time
```

---

### 29. What is application instrumentation?

**Answer:**

Adding Prometheus metrics to application code.

```python
from prometheus_client import Counter, Histogram

requests_total = Counter('http_requests_total', 'Total requests')
request_duration = Histogram('http_request_duration_seconds', 'Duration')

requests_total.inc()
request_duration.observe(0.234)
```

---

### 30. What are Prometheus client libraries?

**Answer:**

Official libraries for instrumentation:
- **Go:** `prometheus/client_golang`
- **Python:** `prometheus_client`
- **Java:** `io.prometheus:simpleclient`
- **Node.js:** `prom-client`

---

## Service Discovery & Configuration

### 31. What is service discovery?

**Answer:**

Automatically finds scrape targets from dynamic infrastructure.

```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
```

**Supported:** Kubernetes, Consul, EC2, Azure, GCE, DNS

---

### 32. What is relabeling?

**Answer:**

Modifies labels during target discovery.

```yaml
relabel_configs:
  # Keep only annotated pods
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
    action: keep
    regex: true
  
  # Drop system namespaces
  - source_labels: [__meta_kubernetes_namespace]
    action: drop
    regex: kube-system
```

---

### 33. What is metric relabeling?

**Answer:**

Modifies metrics after scraping, before storage.

```yaml
metric_relabel_configs:
  # Drop high-cardinality metrics
  - source_labels: [__name__]
    regex: 'go_.*'
    action: drop
  
  # Normalize paths
  - source_labels: [path]
    regex: '/api/users/[0-9]+'
    replacement: '/api/users/:id'
    target_label: path
```

---

### 34. What is scrape interval?

**Answer:**

How often Prometheus collects metrics.

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'high-frequency'
    scrape_interval: 5s
```

**Choosing interval:**
- 5-10s: Real-time monitoring
- 15-30s: Standard applications
- 60s+: Slow-changing metrics

---

### 35. What is scrape timeout?

**Answer:**

Maximum time to wait for target response.

```yaml
global:
  scrape_timeout: 10s
```

**Best practice:** Set timeout < scrape_interval

---

## Scaling & High Availability

### 36. Why is Prometheus single-node by default?

**Answer:**

Standard Prometheus stores data locally and isn't horizontally scalable.

**Limitations:**
- Single point of failure
- Limited retention
- Storage capacity constraints

---

### 37. How do you scale Prometheus?

**Answer:**

**Strategies:**
1. **Federation:** Hierarchical scraping
2. **Sharding:** Split targets across instances
3. **Remote Write:** Send to external storage
4. **Thanos/Cortex/Mimir:** Long-term storage

---

### 38. What is Prometheus federation?

**Answer:**

One Prometheus scrapes metrics from another.

```yaml
scrape_configs:
  - job_name: 'federate'
    honor_labels: true
    metrics_path: '/federate'
    params:
      'match[]':
        - '{job="prometheus"}'
    static_configs:
      - targets:
        - 'prometheus-1:9090'
        - 'prometheus-2:9090'
```

---

### 39. What is remote write?

**Answer:**

Sends metrics to external storage systems.

```yaml
remote_write:
  - url: "http://remote-storage:9009/api/v1/write"
    queue_config:
      capacity: 10000
      max_shards: 5
```

---

### 40. What is Thanos?

**Answer:**

Extends Prometheus with:
- Long-term storage (object storage)
- Global querying across clusters
- Deduplication
- High availability

**Components:**
- Sidecar
- Store Gateway
- Querier
- Compactor

---

## Performance & Optimization

### 41. What affects Prometheus performance?

**Answer:**

**Key factors:**
- Number of time series (cardinality)
- Scrape frequency
- Number of targets
- Query complexity
- Retention period

---

### 42. How do you monitor Prometheus itself?

**Answer:**

```promql
# Memory usage
process_resident_memory_bytes

# Time series count
prometheus_tsdb_head_series

# Scrape duration
scrape_duration_seconds

# Query duration
prometheus_engine_query_duration_seconds
```

---

### 43. What is a recording rule?

**Answer:**

Precomputes expensive queries and stores results.

```yaml
groups:
  - name: example_rules
    interval: 30s
    rules:
      - record: job:http_requests:rate5m
        expr: sum by (job) (rate(http_requests_total[5m]))
```

**Benefits:**
- Faster dashboard queries
- Reduced query load
- Standardized metrics

---

### 44. How do you reduce cardinality?

**Answer:**

**Strategies:**
1. Drop high-cardinality labels
2. Normalize label values
3. Use recording rules
4. Drop unnecessary metrics
5. Set sample limits

```yaml
metric_relabel_configs:
  - source_labels: [user_id]
    action: labeldrop
```

---

### 45. What is retention and how do you configure it?

**Answer:**

How long Prometheus keeps data.

```yaml
storage:
  tsdb:
    retention.time: 15d
    retention.size: 50GB
```

**Considerations:**
- Disk space
- Query performance
- Compliance requirements

---

## Security & Best Practices

### 46. How do you secure Prometheus?

**Answer:**

**Security measures:**
1. Network isolation
2. Authentication (reverse proxy)
3. TLS encryption
4. Access control
5. Secure scrape endpoints

```yaml
# Use TLS for scraping
scrape_configs:
  - job_name: 'secure-app'
    scheme: https
    tls_config:
      ca_file: /etc/prometheus/ca.crt
```

---

### 47. What are the risks of exposing metrics?

**Answer:**

Metrics can reveal:
- Internal architecture
- Service names and versions
- Performance characteristics
- Security vulnerabilities

**Mitigation:**
- Restrict network access
- Use authentication
- Sanitize metric labels

---

### 48. What are metric naming best practices?

**Answer:**

```
<namespace>_<subsystem>_<name>_<unit>

Examples:
http_requests_total
process_cpu_seconds_total
node_memory_bytes
```

**Guidelines:**
- Use snake_case
- Include units in name
- Be descriptive
- Follow conventions

---

### 49. What are label best practices?

**Answer:**

**DO:**
- Use bounded cardinality
- Keep labels stable
- Use meaningful names
- Document label meanings

**DON'T:**
- Use unique identifiers (user_id, request_id)
- Use timestamps as labels
- Create unbounded labels
- Change label meanings

---

### 50. How do you design good alerts?

**Answer:**

**Principles:**
1. **Actionable:** Clear next steps
2. **Symptom-based:** Focus on user impact
3. **Low noise:** Avoid alert fatigue
4. **Contextual:** Include relevant information
5. **SLO-aligned:** Tied to service objectives

```yaml
- alert: HighErrorRate
  expr: |
    (
      sum(rate(http_requests_total{status=~"5.."}[5m]))
      /
      sum(rate(http_requests_total[5m]))
    ) > 0.05
  for: 5m
  annotations:
    summary: "Error rate above 5%"
    description: "Current rate: {{ $value | humanizePercentage }}"
    runbook: "https://wiki.example.com/runbooks/high-error-rate"
```

---

## Troubleshooting & Operations

### 51. How do you troubleshoot missing metrics?

**Answer:**

**Checklist:**
1. Check target discovery: `http://prometheus:9090/targets`
2. Verify scrape status
3. Test endpoint manually: `curl http://target:9090/metrics`
4. Check relabeling rules
5. Verify network connectivity
6. Review Prometheus logs

---

### 52. How do you troubleshoot high memory usage?

**Answer:**

**Investigation steps:**
1. Check cardinality: `prometheus_tsdb_head_series`
2. Identify high-cardinality metrics
3. Review recent configuration changes
4. Check for label explosions
5. Analyze scrape targets

```promql
# Top metrics by cardinality
topk(10, count by (__name__) ({__name__=~".+"}))

# Series per job
count by (job) ({__name__=~".+"})
```

---

### 53. How do you troubleshoot slow queries?

**Answer:**

**Optimization:**
1. Reduce time range
2. Use recording rules
3. Limit cardinality
4. Optimize aggregations
5. Check query complexity

```promql
# Check query stats
prometheus_engine_query_duration_seconds
```

---

### 54. What is the `up` metric?

**Answer:**

Indicates scrape success (1) or failure (0).

```promql
# Alert on target down
up == 0

# Count healthy targets
count(up == 1)

# Targets down by job
count by (job) (up == 0)
```

---

### 55. How do you debug scrape failures?

**Answer:**

**Steps:**
1. Check target status page
2. Review error messages
3. Test endpoint manually
4. Verify network connectivity
5. Check authentication/TLS
6. Review timeout settings

---

## Production Best Practices

### 56. What is your approach to metric design?

**Answer:**

**Principles:**
1. Clear naming conventions
2. Low cardinality labels
3. Meaningful units
4. Consistent instrumentation
5. Documentation

---

### 57. What is your approach to alert design?

**Answer:**

**Strategy:**
1. SLO-based alerting
2. Symptom over cause
3. Proper severity levels
4. Runbook links
5. Regular review and tuning

---

### 58. How do you handle alert fatigue?

**Answer:**

**Solutions:**
1. Increase thresholds
2. Add `for` duration
3. Use alert grouping
4. Implement inhibition
5. Remove noisy alerts
6. Focus on user impact

---

### 59. What are the four golden signals?

**Answer:**

1. **Latency:** Response time
2. **Traffic:** Request rate
3. **Errors:** Error rate
4. **Saturation:** Resource utilization

```promql
# Latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# Traffic
sum(rate(http_requests_total[5m]))

# Errors
sum(rate(http_requests_total{status=~"5.."}[5m]))

# Saturation
avg(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)
```

---

### 60. How do you monitor SLOs?

**Answer:**

```promql
# Availability SLO (99.9%)
1 - (
  sum(rate(http_requests_total{status=~"5.."}[30d]))
  /
  sum(rate(http_requests_total[30d]))
)

# Latency SLO (95% < 200ms)
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) < 0.2
```

---

### 61. What is your Prometheus backup strategy?

**Answer:**

**Approaches:**
1. Snapshot TSDB data
2. Use remote write
3. Implement Thanos/Cortex
4. Regular configuration backups
5. Document recovery procedures

---

### 62. How do you handle Prometheus upgrades?

**Answer:**

**Process:**
1. Review release notes
2. Test in non-production
3. Backup configuration and data
4. Plan rollback procedure
5. Monitor after upgrade
6. Validate alerts and queries

---

### 63. What is your capacity planning approach?

**Answer:**

**Factors:**
1. Expected time series growth
2. Retention requirements
3. Query load
4. Scrape frequency
5. High availability needs

**Monitoring:**
```promql
prometheus_tsdb_head_series
process_resident_memory_bytes
prometheus_tsdb_storage_blocks_bytes
```

---

### 64. How do you organize Prometheus in Kubernetes?

**Answer:**

**Best practices:**
1. Use Prometheus Operator
2. Implement ServiceMonitors
3. Configure PodMonitors
4. Use kube-state-metrics
5. Deploy node-exporter as DaemonSet
6. Implement proper RBAC

---

### 65. What is Prometheus Operator?

**Answer:**

Kubernetes operator for managing Prometheus deployments.

**Custom Resources:**
- Prometheus
- ServiceMonitor
- PodMonitor
- PrometheusRule
- Alertmanager

---

### 66. What is a ServiceMonitor?

**Answer:**

Kubernetes CRD that defines how to scrape services.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: example-app
spec:
  selector:
    matchLabels:
      app: example
  endpoints:
    - port: metrics
      interval: 30s
```

---

### 67. How do you handle multi-tenancy?

**Answer:**

**Strategies:**
1. Separate Prometheus instances
2. Use Cortex/Mimir
3. Implement label-based isolation
4. Configure proper RBAC
5. Use federation for aggregation

---

### 68. What is your disaster recovery plan?

**Answer:**

**Components:**
1. Regular backups
2. Configuration version control
3. Documented procedures
4. Tested recovery process
5. Remote write for data durability
6. High availability setup

---

### 69. How do you test Prometheus configuration?

**Answer:**

```bash
# Validate configuration
promtool check config prometheus.yml

# Validate rules
promtool check rules rules.yml

# Test queries
promtool query instant http://localhost:9090 'up'

# Unit test rules
promtool test rules test.yml
```

---

### 70. What is your monitoring-as-code approach?

**Answer:**

**Practices:**
1. Version control all configs
2. Use GitOps workflows
3. Implement CI/CD pipelines
4. Automated testing
5. Code review process
6. Documentation

---

### 71. How do you handle seasonal traffic patterns?

**Answer:**

**Strategies:**
1. Baseline normal behavior
2. Use dynamic thresholds
3. Implement anomaly detection
4. Adjust alert thresholds
5. Capacity planning

---

### 72. What is your approach to metric retention?

**Answer:**

**Tiers:**
1. **Hot:** Recent data (15-30 days) in Prometheus
2. **Warm:** Medium-term (90 days) in remote storage
3. **Cold:** Long-term (1+ year) in object storage

---

### 73. How do you handle metric migrations?

**Answer:**

**Process:**
1. Run old and new metrics in parallel
2. Update dashboards gradually
3. Migrate alerts
4. Deprecate old metrics
5. Document changes
6. Communicate to teams

---

### 74. What is your approach to Prometheus governance?

**Answer:**

**Framework:**
1. Naming conventions
2. Label standards
3. Alert guidelines
4. Review process
5. Documentation requirements
6. Training programs

---

### 75. How do you measure monitoring effectiveness?

**Answer:**

**Metrics:**
1. Mean time to detection (MTTD)
2. Mean time to resolution (MTTR)
3. Alert accuracy rate
4. False positive rate
5. Coverage percentage
6. SLO compliance

---

## Quick Reference Guide

### Essential PromQL Functions

```promql
# Rate functions
rate(counter[5m])           # Per-second rate
irate(counter[5m])          # Instant rate
increase(counter[1h])       # Total increase

# Aggregations
sum(metric)                 # Sum
avg(metric)                 # Average
max(metric)                 # Maximum
min(metric)                 # Minimum
count(metric)               # Count

# Grouping
sum by (label) (metric)     # Group by label
sum without (label) (metric) # Exclude label

# Time functions
time()                      # Current timestamp
timestamp(metric)           # Metric timestamp

# Math
abs(metric)                 # Absolute value
ceil(metric)                # Round up
floor(metric)               # Round down
round(metric)               # Round

# Comparison
metric > 100                # Greater than
metric < 50                 # Less than
metric == 1                 # Equal to
metric != 0                 # Not equal to
```

### Common Queries

```promql
# CPU usage
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory usage
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# Disk usage
(node_filesystem_size_bytes - node_filesystem_avail_bytes) / node_filesystem_size_bytes * 100

# Request rate
sum(rate(http_requests_total[5m]))

# Error rate
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))

# 95th percentile latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# Availability
avg_over_time(up[24h])
```

### Configuration Snippets

```yaml
# Basic scrape config
scrape_configs:
  - job_name: 'my-app'
    static_configs:
      - targets: ['localhost:9090']

# Kubernetes service discovery
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod

# Alert rule
groups:
  - name: alerts
    rules:
      - alert: HighErrorRate
        expr: rate(errors[5m]) > 0.05
        for: 5m
        labels:
          severity: critical

# Recording rule
groups:
  - name: rules
    rules:
      - record: job:requests:rate5m
        expr: sum by (job) (rate(requests[5m]))
```

### Troubleshooting Commands

```bash
# Check configuration
promtool check config prometheus.yml

# Validate rules
promtool check rules rules.yml

# Query from CLI
promtool query instant http://localhost:9090 'up'

# Check targets
curl http://localhost:9090/api/v1/targets

# Check metrics
curl http://localhost:9090/metrics

# Reload configuration
curl -X POST http://localhost:9090/-/reload
```

---

## Final Interview Tips

### What Interviewers Look For

1. **Technical Depth**
   - Understanding of time-series concepts
   - PromQL proficiency
   - Cardinality awareness
   - Scaling knowledge

2. **Production Experience**
   - Real-world examples
   - Troubleshooting stories
   - Performance optimization
   - Incident response

3. **Best Practices**
   - Metric design
   - Alert quality
   - Security awareness
   - Operational maturity

### Red Flags to Avoid

- ❌ Not understanding cardinality
- ❌ Overusing high-cardinality labels
- ❌ Creating noisy alerts
- ❌ No backup/recovery strategy
- ❌ Ignoring security
- ❌ No testing approach

### Success Factors

- ✅ Explain concepts clearly
- ✅ Provide production examples
- ✅ Discuss trade-offs
- ✅ Show systematic thinking
- ✅ Demonstrate PromQL skills
- ✅ Mention monitoring best practices

### Sample Interview Questions to Expect

1. "How would you design monitoring for a new microservice?"
2. "Explain how you'd troubleshoot high Prometheus memory usage"
3. "What's your approach to reducing alert fatigue?"
4. "How do you handle cardinality explosions?"
5. "Describe your experience with Prometheus at scale"

### Key Takeaways

- **Cardinality is critical** - Always consider label combinations
- **PromQL is powerful** - Master rate(), histogram_quantile(), and aggregations
- **Alerts should be actionable** - Focus on user impact, not just symptoms
- **Scale requires planning** - Use federation, remote write, or Thanos
- **Security matters** - Protect metrics and access to Prometheus

---

**Good luck with your interview! Remember: Focus on understanding concepts deeply, practice PromQL queries, and always think about production implications.**

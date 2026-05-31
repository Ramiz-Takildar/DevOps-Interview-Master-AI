# Senior DevOps Interview Questions and Answers

## Purpose
This document is a PDF-ready senior-level DevOps interview preparation guide. It is organised tool-wise and focuses on practical, production-grade answers that help crack senior DevOps, SRE, Platform Engineer, and Cloud Engineer interviews.

---

# 1. Linux

## Q1. How do you troubleshoot high CPU usage on a Linux production server?
**Answer:**  
I start by identifying whether the issue is system-wide or process-specific using `top`, `htop`, `uptime`, and `mpstat`. Then I check which process is consuming CPU with `ps aux --sort=-%cpu`. If it is application-related, I inspect logs, thread dumps, and recent deployments. If it is kernel or I/O wait related, I use `vmstat`, `iostat`, and `sar`. I also verify whether the spike is expected due to traffic or abnormal due to a runaway process, bad query, or infinite loop. Finally, I mitigate by scaling, restarting the faulty service if safe, or rolling back the recent change, and then perform root cause analysis.

## Q2. What is the difference between a process and a thread?
**Answer:**  
A process is an independent execution unit with its own memory space, file descriptors, and resources. A thread is a lightweight execution unit within a process and shares the process memory. Threads are faster to create and switch, but poor thread isolation can cause application instability. In interviews, I explain this in the context of debugging Java, Python, or web servers where thread contention or deadlocks affect performance.

## Q3. How do you find disk space issues quickly?
**Answer:**  
I use `df -h` to identify full filesystems and `du -sh /*` or `du -sh /var/*` to locate large directories. Then I inspect logs, temporary files, Docker layers, and old backups. I also check inode exhaustion using `df -i`, because sometimes disk appears full due to inode limits rather than actual storage usage.

## Q4. What is the difference between soft link and hard link?
**Answer:**  
A hard link points directly to the inode, so it remains valid even if the original filename is deleted. A soft link is a pointer to the file path, so it breaks if the target path is removed. Hard links cannot span filesystems and usually cannot link directories. Soft links are more flexible and commonly used in deployments and configuration management.

## Q5. How do you troubleshoot memory leaks in Linux?
**Answer:**  
I first confirm memory pressure using `free -m`, `vmstat`, and `top`. Then I identify the process consuming memory. For application-level leaks, I use language-specific tools such as heap dumps for Java, `tracemalloc` for Python, or profiling tools. I also check whether memory growth is due to cache, buffers, or actual leaks. If swap usage is increasing and OOM kills appear in `dmesg`, I treat it as urgent and mitigate by scaling, restarting, or limiting memory usage while root cause analysis continues.

---

# 2. Networking

## Q1. How do you troubleshoot a service that is unreachable?
**Answer:**  
I follow the path layer by layer: DNS resolution, routing, firewall/security groups, load balancer health, application port listening, and application logs. I use `nslookup`, `dig`, `ping`, `traceroute`, `curl`, `telnet`, `nc`, and `ss -tulpn`. In cloud environments, I also verify security groups, NACLs, ingress rules, and service mesh policies.

## Q2. What is the difference between TCP and UDP?
**Answer:**  
TCP is connection-oriented, reliable, ordered, and includes retransmission and flow control. UDP is connectionless, faster, and does not guarantee delivery or order. TCP is used for web traffic, APIs, and databases. UDP is used for DNS, streaming, and latency-sensitive workloads.

## Q3. What happens in DNS resolution?
**Answer:**  
The client checks local cache, then resolver cache, then recursive DNS server. If not found, the recursive server queries root, TLD, and authoritative name servers. The final IP is returned and cached based on TTL. In production, DNS issues often involve stale cache, wrong records, propagation delay, or expired certificates tied to DNS changes.

---

# 3. Git

## Q1. What is the difference between merge and rebase?
**Answer:**  
Merge preserves branch history and creates a merge commit. Rebase rewrites commit history to create a linear timeline. In team environments, I prefer merge for shared branches and rebase for cleaning up local feature branches before merging. I avoid rebasing public branches because it rewrites history and can disrupt collaborators.

## Q2. How do you recover from a bad commit pushed to production branch?
**Answer:**  
If the commit is already shared, I prefer `git revert` because it safely creates a new commit that undoes the change. I avoid `git reset --hard` on shared branches unless there is a controlled emergency and team agreement. I also verify CI status and deployment impact before reverting.

## Q3. What branching strategy do you prefer?
**Answer:**  
For most modern teams, trunk-based development works best with short-lived feature branches, strong CI, feature flags, and frequent integration. For regulated or release-heavy environments, GitFlow may still be useful. My preference depends on release frequency, team maturity, and rollback strategy.

---

# 4. Docker

## Q1. What is the difference between a container and a virtual machine?
**Answer:**  
A VM virtualises hardware and runs a full guest OS, while a container shares the host kernel and isolates processes using namespaces and cgroups. Containers are lighter, faster to start, and better suited for microservices and CI/CD pipelines. VMs provide stronger isolation and are useful for mixed OS workloads.

## Q2. How do you reduce Docker image size?
**Answer:**  
I use minimal base images such as Alpine or distroless where appropriate, multi-stage builds, `.dockerignore`, and avoid unnecessary packages. I also combine layers carefully, remove build-time dependencies, and avoid copying secrets or temporary files into the image.

## Q3. How do you troubleshoot a crashing container?
**Answer:**  
I inspect logs using `docker logs`, check exit codes, verify environment variables, mounted volumes, entrypoint commands, and resource limits. I also run the image interactively if needed. Common causes are missing dependencies, wrong startup commands, permission issues, or application crashes.

## Q4. What is the difference between CMD and ENTRYPOINT?
**Answer:**  
`ENTRYPOINT` defines the main executable, while `CMD` provides default arguments. If both are used, CMD acts as arguments to ENTRYPOINT. This is useful when building reusable images where the executable is fixed but arguments may vary.

---

# 5. Kubernetes

## Q1. What happens when you create a Deployment in Kubernetes?
**Answer:**  
The Deployment creates a ReplicaSet, which creates Pods. The scheduler assigns Pods to nodes based on resource availability and constraints. Kubelet starts containers through the container runtime. Services and ingress expose the application. Controllers continuously reconcile desired and actual state.

## Q2. How do you troubleshoot a Pod stuck in CrashLoopBackOff?
**Answer:**  
I inspect `kubectl describe pod`, `kubectl logs`, previous container logs, events, probes, config maps, secrets, and resource limits. I verify whether the application is failing due to bad config, missing dependency, startup timing, or OOM kill. If needed, I compare with the previous working version and recent deployment changes.

## Q3. What is the difference between liveness, readiness, and startup probes?
**Answer:**  
Liveness checks whether the container should be restarted. Readiness checks whether it is ready to receive traffic. Startup probe is used for slow-starting applications and prevents premature liveness failures. Proper probe design is critical to avoid cascading failures during deployments.

## Q4. How do you secure a Kubernetes cluster?
**Answer:**  
I use RBAC with least privilege, network policies, pod security standards, image scanning, secret management, audit logging, admission controls, and restricted API access. I also secure etcd, rotate credentials, enforce TLS, and monitor suspicious activity.

## Q5. What is etcd and why is it important?
**Answer:**  
etcd is the distributed key-value store that holds Kubernetes cluster state. If etcd is unhealthy or corrupted, the control plane becomes unreliable. Backup and restore strategy for etcd is critical for disaster recovery.

## Q6. How do you perform zero-downtime deployment in Kubernetes?
**Answer:**  
I use rolling updates with proper readiness probes, PodDisruptionBudgets, resource requests, and surge/unavailable settings. I also validate backward compatibility, database migration strategy, and rollback readiness. For higher safety, I use canary or blue-green deployment patterns.

---

# 6. Terraform

## Q1. What is Terraform state and why is it important?
**Answer:**  
Terraform state maps real infrastructure to configuration. It allows Terraform to know what exists, what changed, and what needs to be updated. Without proper state management, infrastructure drift and accidental recreation become major risks.

## Q2. Why should Terraform state be stored remotely?
**Answer:**  
Remote state enables collaboration, locking, versioning, and recovery. For example, S3 with DynamoDB locking or Terraform Cloud prevents concurrent modifications and reduces the risk of state corruption.

## Q3. How do you handle Terraform drift?
**Answer:**  
I detect drift using `terraform plan`, scheduled drift checks, and cloud-native config monitoring. Then I decide whether to import the manual change into code, revert the manual change, or redesign the module. The goal is to restore infrastructure as code as the source of truth.

## Q4. What are modules in Terraform?
**Answer:**  
Modules are reusable building blocks that standardise infrastructure patterns. They improve consistency, reduce duplication, and enforce best practices. In senior roles, I focus on module versioning, input validation, outputs, and secure defaults.

## Q5. How do you recover from corrupted Terraform state?
**Answer:**  
I first stop all changes, back up the current state, inspect remote backend history, and restore the last known good version if possible. Then I reconcile drift using `terraform state` commands or imports. I never rush state repair in production because it can cause destructive changes.

---

# 7. AWS

## Q1. How do you design a highly available application in AWS?
**Answer:**  
I distribute workloads across multiple Availability Zones, use load balancers, auto scaling groups, managed databases with Multi-AZ, and store static assets in S3 with CloudFront. I also design for failure by using health checks, backups, monitoring, and tested recovery procedures.

## Q2. What is the difference between Security Group and NACL?
**Answer:**  
Security Groups are stateful and operate at the instance or ENI level. NACLs are stateless and operate at the subnet level. Security Groups are usually the primary control, while NACLs provide an additional coarse-grained network boundary.

## Q3. How do you secure IAM in AWS?
**Answer:**  
I enforce least privilege, avoid long-lived access keys, use roles instead of users where possible, enable MFA, rotate credentials, monitor CloudTrail, and use SCPs in AWS Organizations. I also review wildcard permissions and privilege escalation paths.

## Q4. What is the difference between ALB and NLB?
**Answer:**  
ALB works at Layer 7 and supports host/path-based routing, HTTP/HTTPS, and web applications. NLB works at Layer 4 and is designed for very high performance and TCP/UDP traffic. Choice depends on protocol and routing needs.

## Q5. How do you troubleshoot an EC2 instance that is unreachable?
**Answer:**  
I check instance status checks, security groups, NACLs, route tables, subnet association, SSH key, SSM access, and system logs. If the issue is OS-level, I inspect boot logs, disk usage, and network config. If needed, I detach the root volume and inspect it from another instance.

---

# 8. Azure

## Q1. What is the difference between Azure VM Scale Sets and AKS?
**Answer:**  
VM Scale Sets manage scalable virtual machines, while AKS is a managed Kubernetes service for container orchestration. AKS is preferred for microservices and container platforms, while VMSS is useful for VM-based workloads.

## Q2. How do you secure Azure resources?
**Answer:**  
I use Managed Identities, RBAC, NSGs, Key Vault, Defender for Cloud, Azure Policy, and private endpoints. I also enforce tagging, governance, and logging through Azure Monitor and Activity Logs.

## Q3. What is Azure Key Vault used for?
**Answer:**  
Azure Key Vault stores secrets, certificates, and keys securely. It helps remove secrets from code and supports controlled access, rotation, and auditability.

---

# 9. CI/CD

## Q1. What are the stages of a mature CI/CD pipeline?
**Answer:**  
A mature pipeline includes source validation, unit tests, static analysis, security scanning, build, artifact versioning, integration tests, deployment, smoke tests, and rollback or progressive delivery controls. For senior roles, I also discuss policy gates, approvals, and observability after deployment.

## Q2. What is blue-green deployment?
**Answer:**  
Blue-green deployment maintains two environments: current production and new version. Traffic is switched only after validation. It reduces downtime and simplifies rollback, but requires duplicate environment capacity.

## Q3. What is canary deployment?
**Answer:**  
Canary deployment releases changes to a small subset of users first, monitors health metrics, and gradually increases traffic if stable. It reduces blast radius and is ideal for high-risk changes.

## Q4. How do you secure a CI/CD pipeline?
**Answer:**  
I secure secrets, isolate runners, sign artifacts, scan dependencies and images, enforce branch protection, use least privilege for deployment credentials, and maintain audit trails. I also prevent secret leakage in logs and avoid running untrusted code with privileged access.

---

# 10. Jenkins

## Q1. How do you scale Jenkins for enterprise use?
**Answer:**  
I keep the controller lightweight and offload builds to dynamic agents using Kubernetes or cloud agents. I use pipeline as code, shared libraries, RBAC, backups, monitoring, and plugin governance. I also minimise plugin sprawl because it creates security and stability risks.

## Q2. What is the difference between scripted and declarative pipeline?
**Answer:**  
Scripted pipeline is more flexible and Groovy-heavy. Declarative pipeline is more structured, readable, and easier to standardise. For most teams, declarative is preferred unless advanced control flow is required.

---

# 11. GitHub Actions

## Q1. What are GitHub Actions runners?
**Answer:**  
Runners are the compute environments that execute workflows. They can be GitHub-hosted or self-hosted. Self-hosted runners provide more control but require stronger security and lifecycle management.

## Q2. How do you optimise GitHub Actions workflows?
**Answer:**  
I use caching, matrix builds carefully, reusable workflows, concurrency controls, and path filters. I also separate fast feedback checks from slower integration jobs to improve developer productivity.

---

# 12. Monitoring and Observability

## Q1. What is the difference between monitoring and observability?
**Answer:**  
Monitoring tells you whether known signals are healthy. Observability helps you understand unknown failures by correlating metrics, logs, and traces. Monitoring is alerting-focused; observability is diagnosis-focused.

## Q2. What are the four golden signals?
**Answer:**  
Latency, traffic, errors, and saturation. These are core indicators of service health and are widely used in SRE and production operations.

## Q3. How do you reduce alert fatigue?
**Answer:**  
I remove noisy alerts, tune thresholds, use symptom-based alerting, add routing and deduplication, and ensure every alert is actionable. Alerts should indicate customer impact or urgent operational risk, not just raw metric fluctuation.

---

# 13. Prometheus

## Q1. How does Prometheus work?
**Answer:**  
Prometheus pulls metrics from instrumented targets at intervals, stores them as time-series data, and evaluates alert rules. It is strong for Kubernetes-native monitoring and integrates well with Alertmanager and Grafana.

## Q2. What are labels in Prometheus?
**Answer:**  
Labels are key-value pairs attached to metrics. They enable filtering and aggregation, but high-cardinality labels can create performance and storage issues. Senior engineers must control label design carefully.

---

# 14. Grafana

## Q1. What is Grafana used for?
**Answer:**  
Grafana visualises metrics, logs, and traces from multiple data sources. It is used for dashboards, alerting, and operational visibility. Good Grafana dashboards focus on service health, business impact, and drill-down capability.

---

# 15. ELK / Logging

## Q1. What makes a good logging strategy?
**Answer:**  
Logs should be structured, searchable, correlated with request IDs, and free from secrets. I define log levels clearly, centralise logs, set retention policies, and ensure logs support incident investigation rather than just verbose output.

## Q2. Why are structured logs better than plain text logs?
**Answer:**  
Structured logs are machine-readable and easier to query, aggregate, and correlate. They improve troubleshooting speed and support automation in observability platforms.

---

# 16. Security

## Q1. How do you manage secrets securely in DevOps?
**Answer:**  
I never hardcode secrets in code or images. I use secret managers such as Vault, AWS Secrets Manager, or Azure Key Vault. I rotate secrets, restrict access, audit usage, and inject them at runtime.

## Q2. What is least privilege?
**Answer:**  
Least privilege means granting only the minimum permissions required to perform a task. It reduces blast radius and is essential for IAM, Kubernetes RBAC, CI/CD credentials, and database access.

## Q3. How do you secure container images?
**Answer:**  
I use trusted base images, scan for vulnerabilities, minimise packages, run as non-root, sign images where possible, and enforce admission policies. I also patch regularly and remove unused tools from runtime images.

## Q4. What is shift-left security?
**Answer:**  
Shift-left security means integrating security earlier in the development lifecycle through code scanning, dependency checks, IaC scanning, secret detection, and policy validation before deployment.

---

# 17. SRE and Incident Management

## Q1. What is an SLI, SLO, and SLA?
**Answer:**  
SLI is a measurable indicator of service performance, such as latency or availability. SLO is the target for that indicator, such as 99.9% uptime. SLA is the formal agreement with customers and may include penalties. SLOs guide engineering priorities and error budget decisions.

## Q2. What is an error budget?
**Answer:**  
An error budget is the acceptable amount of unreliability based on the SLO. If the budget is exhausted, teams should slow feature releases and focus on reliability improvements.

## Q3. How do you handle a Sev-1 incident?
**Answer:**  
I first stabilise the service and reduce customer impact. Then I establish clear communication, assign roles, gather evidence, and avoid random changes. After mitigation, I lead root cause analysis and a blameless postmortem with preventive actions.

---

# 18. System Design for DevOps Interviews

## Q1. How would you design a highly available CI/CD platform?
**Answer:**  
I would separate control plane and execution plane, use stateless services where possible, store artifacts in durable object storage, use autoscaling runners, centralised secrets management, audit logging, and observability. I would also design for rollback, queue durability, and regional resilience.

## Q2. How would you design observability for a microservices platform?
**Answer:**  
I would standardise metrics, logs, and traces across services, enforce correlation IDs, centralise dashboards, define SLOs, and create service ownership boundaries. I would also ensure alert routing, retention policies, and cost control for telemetry data.

---

# 19. Scenario-Based Questions

## Q1. Production Kubernetes cluster is down after a deployment. What do you do?
**Answer:**  
I assess blast radius, identify whether control plane or workloads are affected, pause further deployments, inspect recent changes, check events, node health, ingress, DNS, and application logs. I roll back if needed, restore service first, and then perform root cause analysis.

## Q2. Terraform apply failed midway and infrastructure is inconsistent. What next?
**Answer:**  
I stop further changes, inspect state, compare actual resources with expected plan, and reconcile carefully. I may import resources, remove stale state entries, or restore backend state version depending on the issue. I avoid repeated blind applies.

## Q3. CI pipeline suddenly becomes very slow. How do you investigate?
**Answer:**  
I compare recent changes in runners, dependencies, caching, network, artifact storage, and test duration. I identify whether slowdown is global or job-specific. Then I optimise bottlenecks such as dependency downloads, serial stages, or overloaded runners.

---

# 20. Senior-Level Interview Tips

## Tip 1: Answer with structure
Use this pattern:
1. Identify the issue  
2. Assess impact  
3. Investigate with tools  
4. Mitigate safely  
5. Prevent recurrence  

## Tip 2: Mention trade-offs
Senior interviews expect trade-offs, not only definitions. Example:  
- Blue-green is safer but costs more.  
- Canary reduces blast radius but needs strong observability.  
- Managed services reduce ops burden but may reduce low-level control.

## Tip 3: Speak in production language
Use terms like:
- blast radius  
- rollback  
- observability  
- least privilege  
- high availability  
- disaster recovery  
- root cause analysis  
- error budget  
- customer impact  

## Tip 4: Always include security and monitoring
For almost every answer, mention:
- access control  
- logging  
- metrics  
- alerts  
- backup/recovery  
- auditability  

---

# 21. Rapid-Fire Senior DevOps Questions

1. What is the difference between horizontal and vertical scaling?  
2. Why is immutable infrastructure useful?  
3. What is the purpose of a service mesh?  
4. How do you rotate secrets without downtime?  
5. What is the difference between RPO and RTO?  
6. How do you prevent configuration drift?  
7. What is the use of admission controllers in Kubernetes?  
8. How do you secure self-hosted CI runners?  
9. What is the difference between push and pull deployment models?  
10. Why are runbooks important in operations?  

---

# 22. Final Preparation Strategy

## 7-day plan
**Day 1:** Linux, networking, Git  
**Day 2:** Docker and Kubernetes basics + troubleshooting  
**Day 3:** Advanced Kubernetes + security  
**Day 4:** Terraform + AWS/Azure  
**Day 5:** CI/CD, Jenkins, GitHub Actions  
**Day 6:** Monitoring, observability, logging, SRE  
**Day 7:** Mock interviews, scenario questions, system design  

## How to use this document
- Read each answer aloud.
- Convert each answer into your own words.
- Practise scenario-based responses.
- Add examples from your real projects.
- Focus on troubleshooting, scale, security, and trade-offs.

---

## End Note
If you explain concepts clearly, answer with structure, and connect tools to production outcomes, you will perform strongly in senior DevOps interviews.
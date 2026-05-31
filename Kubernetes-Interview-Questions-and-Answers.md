# Kubernetes Interview Questions and Answers

> **Senior DevOps Interview Pack**
>
> **Domain:** Kubernetes concepts, orchestration, troubleshooting, security, scaling, and platform operations  
> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  
> **Format:** 100 real-interview-style questions with concise, practical answers  
> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export

---

## Executive Summary

This guide is designed for senior-level Kubernetes interviews where interviewers expect more than object definitions. You should be able to explain cluster architecture, workload behaviour, networking, security, scaling, troubleshooting, and safe production operations.

### What this pack helps you demonstrate
- Strong Kubernetes fundamentals
- Platform and workload management judgement
- Security and reliability awareness
- Troubleshooting and upgrade discipline
- Clear, structured interview communication

---

## Navigation

| Section | Focus Area |
|---|---|
| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |
| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |
| [Kubernetes Foundations](#kubernetes-foundations) | Cluster architecture and core concepts |
| [Core Objects and Workload Management](#core-objects-and-workload-management) | Pods, Deployments, Services, and rollout behaviour |
| [Networking, Storage, and Security](#networking-storage-and-security) | Connectivity, persistence, access control, and isolation |
| [Troubleshooting, Scaling, and Production Practice](#troubleshooting-scaling-and-production-practice) | Debugging, autoscaling, upgrades, and operations |
| [Production Interview Mindset](#production-interview-mindset) | Senior-level decision and risk approach |
| [Rapid Revision Sheet](#rapid-revision-sheet) | Last-minute interview refresh |
| [Final Interview Advice](#final-interview-advice) | What interviewers remember most |

---

## How to Use This Guide

### Recommended preparation flow
1. Read **10 to 15 questions per day**
2. Answer each question once **without looking**
3. Re-answer using a **production example**
4. Revise weak areas using the **Rapid Revision Sheet**

### What senior interviewers usually expect
- Correct fundamentals
- Clear explanation, not just keywords
- Real production context
- Safe troubleshooting sequence
- Awareness of security, reliability, and rollback

## Interview Answer Framework

Use this structure for most interview answers:

| Step | What to say |
|---|---|
| 1. Define | Explain what the Kubernetes concept or object does |
| 2. Importance | Explain why it matters in cluster operations |
| 3. Practical example | Give a realistic deployment or incident example |
| 4. Troubleshooting angle | Mention events, logs, metrics, or validation steps |
| 5. Safe action | Explain how you reduce risk during changes or incidents |

### Example senior-style answer
> “I first explain the Kubernetes concept clearly, then connect it to workload behaviour and production impact, and finally describe how I would validate, troubleshoot, secure, or roll back it in a real cluster.”

## Kubernetes Foundations

### 1) What is Kubernetes?
**Answer:** Kubernetes is a container orchestration platform that automates deployment, scaling, networking, self-healing, and lifecycle management of containerised applications.

### 2) Why is Kubernetes used?
**Answer:** It helps run containers reliably at scale by managing scheduling, service discovery, rolling updates, health checks, and recovery across clusters.

### 3) What is a cluster in Kubernetes?
**Answer:** A cluster is a group of control plane and worker nodes that run and manage containerised workloads.

### 4) What is the control plane?
**Answer:** The control plane manages cluster state, scheduling, API operations, and reconciliation through components like the API server, scheduler, controller manager, and etcd.

### 5) What is a worker node?
**Answer:** A worker node runs application workloads using kubelet, container runtime, and kube-proxy or equivalent networking components.

### 6) What is kube-apiserver?
**Answer:** It is the central API entry point for all Kubernetes operations and the main interface used by users, controllers, and tools.

### 7) What is etcd?
**Answer:** etcd is the distributed key-value store that holds the cluster’s desired and actual state.

### 8) Why is etcd important?
**Answer:** If etcd is unavailable or corrupted, the control plane cannot reliably manage cluster state, making backup and restore critical.

### 9) What is kube-scheduler?
**Answer:** The scheduler assigns unscheduled Pods to suitable nodes based on resources, constraints, affinity rules, taints, and policies.

### 10) What is kube-controller-manager?
**Answer:** It runs controllers that continuously reconcile desired state, such as Deployments, ReplicaSets, Nodes, and Jobs.

### 11) What is kubelet?
**Answer:** kubelet is the agent on each node that ensures containers described in Pod specs are running correctly.

### 12) What is kube-proxy?
**Answer:** kube-proxy manages network rules that enable Service-based traffic routing to Pods.

### 13) What is a Pod?
**Answer:** A Pod is the smallest deployable unit in Kubernetes and can contain one or more tightly coupled containers sharing network and storage.

### 14) Why can a Pod have multiple containers?
**Answer:** Multiple containers in one Pod are used when they must share lifecycle, localhost networking, or volumes, such as sidecar patterns.

### 15) What is a Deployment?
**Answer:** A Deployment manages stateless application rollout, scaling, and updates through ReplicaSets.

### 16) What is a ReplicaSet?
**Answer:** A ReplicaSet ensures a specified number of Pod replicas are running at any time.

### 17) What is a StatefulSet?
**Answer:** A StatefulSet manages stateful applications requiring stable identities, ordered rollout, and persistent storage.

### 18) What is a DaemonSet?
**Answer:** A DaemonSet ensures a Pod runs on all or selected nodes, commonly used for logging, monitoring, or security agents.

### 19) What is a Job?
**Answer:** A Job runs one-time or finite tasks until completion.

### 20) What is a CronJob?
**Answer:** A CronJob schedules Jobs to run periodically based on cron syntax.

### 21) What is a Namespace?
**Answer:** A Namespace logically separates resources within a cluster for organisation, access control, and multi-team isolation.

### 22) What is a Service in Kubernetes?
**Answer:** A Service provides stable networking and load balancing for a set of Pods.

### 23) What is ClusterIP?
**Answer:** ClusterIP is the default Service type that exposes an internal virtual IP reachable only inside the cluster.

### 24) What is NodePort?
**Answer:** NodePort exposes a Service on a static port on each node, allowing external access through node IPs.

### 25) What is LoadBalancer?
**Answer:** LoadBalancer provisions an external load balancer through the cloud provider to expose a Service publicly or privately.

## Core Objects and Workload Management

### 26) What is an ExternalName Service?
**Answer:** It maps a Service name to an external DNS name instead of proxying traffic to Pods.

### 27) What is Ingress?
**Answer:** Ingress provides HTTP and HTTPS routing to Services based on hostnames and paths, usually through an Ingress controller.

### 28) What is an Ingress controller?
**Answer:** It is the component that implements Ingress rules, such as NGINX Ingress or cloud-native ingress controllers.

### 29) What is the difference between Service and Ingress?
**Answer:** A Service exposes Pods internally or externally, while Ingress manages Layer 7 HTTP/HTTPS routing to Services.

### 30) What is a ConfigMap?
**Answer:** A ConfigMap stores non-sensitive configuration data for applications.

### 31) What is a Secret?
**Answer:** A Secret stores sensitive data such as passwords, tokens, or certificates, though it should still be protected with encryption and access controls.

### 32) Are Kubernetes Secrets encrypted by default?
**Answer:** They are base64-encoded by default, not strongly protected unless encryption at rest and proper RBAC are configured.

### 33) What is a volume in Kubernetes?
**Answer:** A volume provides storage accessible to containers in a Pod and can be ephemeral or persistent.

### 34) What is a PersistentVolume?
**Answer:** A PersistentVolume is a cluster storage resource provisioned manually or dynamically.

### 35) What is a PersistentVolumeClaim?
**Answer:** A PersistentVolumeClaim is a request for storage by a workload.

### 36) What is a StorageClass?
**Answer:** A StorageClass defines how dynamic storage should be provisioned, including backend type and parameters.

### 37) What is dynamic provisioning?
**Answer:** It automatically creates storage volumes when a PVC is requested.

### 38) What is a label?
**Answer:** A label is a key-value pair attached to resources for selection, grouping, and organisation.

### 39) What is a selector?
**Answer:** A selector matches resources based on labels, commonly used by Services and controllers.

### 40) What is an annotation?
**Answer:** An annotation stores non-identifying metadata used by tools, controllers, or humans.

### 41) What is the difference between labels and annotations?
**Answer:** Labels are used for selection and grouping, while annotations are for metadata not used in selectors.

### 42) What is desired state in Kubernetes?
**Answer:** Desired state is the configuration declared in manifests, which controllers continuously try to enforce.

### 43) What is reconciliation?
**Answer:** Reconciliation is the control loop process of comparing actual state with desired state and correcting drift.

### 44) What happens when you create a Deployment?
**Answer:** The API server stores it, the Deployment controller creates a ReplicaSet, the scheduler assigns Pods to nodes, and kubelet starts containers.

### 45) What is rolling update?
**Answer:** A rolling update gradually replaces old Pods with new ones while maintaining service availability.

### 46) What is rollback in Kubernetes?
**Answer:** Rollback reverts a Deployment to a previous revision if a release causes issues.

### 47) How do you check rollout status?
**Answer:** Use `kubectl rollout status deployment/<name>`.

### 48) How do you roll back a Deployment?
**Answer:** Use `kubectl rollout undo deployment/<name>`.

### 49) What is a readiness probe?
**Answer:** A readiness probe checks whether a container is ready to receive traffic.

### 50) What is a liveness probe?
**Answer:** A liveness probe checks whether a container is healthy enough to keep running; failure triggers restart.

## Networking, Storage, and Security

### 51) What is a startup probe?
**Answer:** A startup probe is used for slow-starting applications to prevent premature liveness failures.

### 52) Why are probes important?
**Answer:** They improve reliability by ensuring traffic goes only to healthy Pods and unhealthy containers are restarted appropriately.

### 53) What is resource request?
**Answer:** A resource request is the minimum CPU or memory Kubernetes uses for scheduling decisions.

### 54) What is resource limit?
**Answer:** A resource limit is the maximum CPU or memory a container can use before throttling or termination.

### 55) Why should requests and limits be set?
**Answer:** They improve scheduling accuracy, cluster stability, and protection against noisy-neighbour issues.

### 56) What happens if memory limit is exceeded?
**Answer:** The container may be OOM-killed.

### 57) What happens if CPU limit is exceeded?
**Answer:** CPU usage is throttled rather than killed.

### 58) What is Horizontal Pod Autoscaler?
**Answer:** HPA automatically scales Pod replicas based on metrics such as CPU, memory, or custom metrics.

### 59) What is Vertical Pod Autoscaler?
**Answer:** VPA adjusts resource requests and limits for Pods based on observed usage.

### 60) What is Cluster Autoscaler?
**Answer:** Cluster Autoscaler adds or removes nodes based on pending Pods and cluster utilisation.

### 61) What is taint in Kubernetes?
**Answer:** A taint repels Pods from a node unless they have a matching toleration.

### 62) What is toleration?
**Answer:** A toleration allows a Pod to be scheduled onto a tainted node.

### 63) What is node affinity?
**Answer:** Node affinity influences or requires scheduling onto nodes with specific labels.

### 64) What is pod affinity?
**Answer:** Pod affinity attracts Pods to nodes where matching Pods already run.

### 65) What is pod anti-affinity?
**Answer:** Pod anti-affinity spreads Pods apart to improve availability and fault tolerance.

### 66) What is cordon?
**Answer:** Cordoning marks a node unschedulable so no new Pods are placed on it.

### 67) What is drain?
**Answer:** Draining safely evicts workloads from a node before maintenance.

### 68) What is eviction?
**Answer:** Eviction is the controlled removal of Pods, often during drain or resource pressure events.

### 69) What is a PodDisruptionBudget?
**Answer:** A PodDisruptionBudget limits how many Pods can be voluntarily disrupted at once.

### 70) Why is PDB important?
**Answer:** It protects application availability during maintenance, upgrades, or autoscaling events.

### 71) What is RBAC?
**Answer:** RBAC controls access to Kubernetes resources using Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.

### 72) What is the difference between Role and ClusterRole?
**Answer:** A Role applies within a namespace, while a ClusterRole can apply cluster-wide or be bound within namespaces.

### 73) What is a ServiceAccount?
**Answer:** A ServiceAccount provides an identity for Pods to interact with the Kubernetes API or integrated cloud services.

### 74) Why should default ServiceAccount usage be avoided?
**Answer:** Because it may grant broader permissions than needed and violates least privilege principles.

### 75) What is a NetworkPolicy?
**Answer:** A NetworkPolicy controls allowed ingress and egress traffic between Pods and namespaces.

## Troubleshooting, Scaling, and Production Practice

### 76) Why are NetworkPolicies important?
**Answer:** They reduce lateral movement risk and enforce zero-trust style segmentation inside the cluster.

### 77) What is admission control?
**Answer:** Admission control validates or mutates requests before objects are persisted in the cluster.

### 78) What is an admission controller example?
**Answer:** Examples include Pod Security Admission, image policy checks, and custom validating webhooks.

### 79) What is Pod Security Admission?
**Answer:** It enforces security standards such as restricted privilege, host access limits, and safer container settings.

### 80) What is a sidecar container?
**Answer:** A sidecar is a helper container in the same Pod that adds capabilities like logging, proxying, or secrets refresh.

### 81) What is init container?
**Answer:** An init container runs before app containers and is used for setup tasks such as migrations or dependency checks.

### 82) How do you troubleshoot a Pod stuck in Pending?
**Answer:** Check scheduling events, resource requests, node capacity, taints, affinity rules, PVC binding, and quota limits.

### 83) How do you troubleshoot CrashLoopBackOff?
**Answer:** Inspect `kubectl describe pod`, logs, previous logs, probes, config, secrets, dependencies, and recent image changes.

### 84) How do you troubleshoot ImagePullBackOff?
**Answer:** Verify image name, tag, registry access, imagePullSecrets, network connectivity, and registry rate limits.

### 85) How do you inspect Pod logs?
**Answer:** Use `kubectl logs <pod>` and `kubectl logs <pod> -c <container>` for multi-container Pods.

### 86) How do you inspect Pod events?
**Answer:** Use `kubectl describe pod <pod>`.

### 87) How do you execute a command inside a Pod?
**Answer:** Use `kubectl exec -it <pod> -- sh` or `bash` if available.

### 88) How do you debug DNS issues in Kubernetes?
**Answer:** Check CoreDNS health, Service discovery, Pod DNS config, network policies, and test resolution from inside Pods.

### 89) What is CoreDNS?
**Answer:** CoreDNS is the DNS server used in most Kubernetes clusters for internal service discovery.

### 90) How do you secure a Kubernetes cluster?
**Answer:** Use RBAC, NetworkPolicies, Pod Security standards, image scanning, secret protection, audit logs, restricted API access, and least privilege everywhere.

### 91) What is audit logging in Kubernetes?
**Answer:** Audit logging records API requests and responses for security, compliance, and incident investigation.

### 92) Why should etcd backups be tested?
**Answer:** Because backup without restore validation is not a reliable disaster recovery strategy.

### 93) What is a Helm chart?
**Answer:** A Helm chart is a package of Kubernetes manifests with templating and values for reusable application deployment.

### 94) What is the difference between Kubernetes and Docker?
**Answer:** Docker is a container runtime and packaging ecosystem, while Kubernetes orchestrates containers across clusters.

### 95) What is the difference between Deployment and StatefulSet?
**Answer:** Deployment is for stateless workloads with interchangeable Pods, while StatefulSet is for stateful workloads needing stable identity and storage.

### 96) How do you perform zero-downtime deployment?
**Answer:** Use rolling updates, readiness probes, proper surge settings, backward-compatible changes, and strong observability with rollback readiness.

### 97) What is your approach to Kubernetes troubleshooting in production?
**Answer:** I check impact first, then inspect events, rollout history, Pod health, node health, networking, storage, and recent changes before mitigating safely.

### 98) What is your approach to Kubernetes security?
**Answer:** I enforce least privilege, isolate workloads, scan images, restrict privileges, secure secrets, monitor audit logs, and standardise secure defaults.

### 99) What is your approach to Kubernetes upgrades?
**Answer:** I review compatibility, test in lower environments, upgrade control plane and nodes carefully, validate workloads, and maintain rollback and backup plans.

## Production Interview Mindset

### 100) What is your practical senior-level approach in interviews?
**Answer:** Standardise manifests and policies, automate deployments, enforce security and observability, design for failure, and treat cluster operations as a disciplined platform engineering practice.

### Senior interview checklist
- Confirm the business or operational context
- Explain trade-offs, not only definitions
- Mention validation and troubleshooting steps
- Prefer safe, reversible actions first
- Show reliability, security, and maintainability thinking

## Rapid Revision Sheet

### Last-minute revision reminders
- Explain concepts in context, not in isolation
- Mention logs, metrics, and validation together
- Show safe mitigation thinking
- Highlight trade-offs where relevant
- Speak like an operator, not only like an exam candidate

### Best answer pattern to remember
1. **Define the concept**
2. **Explain why it matters**
3. **Give a production example**
4. **Mention one troubleshooting or implementation approach**

## Final Interview Advice

> In senior Kubernetes interviews, explain not only object definitions but also scheduling, networking, security, rollout safety, troubleshooting, and disaster recovery in real production environments.
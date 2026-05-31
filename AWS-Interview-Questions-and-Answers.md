# AWS Interview Questions and Answers

> **Senior DevOps Interview Pack**
>
> **Domain:** AWS concepts, architecture, security, reliability, cost, and cloud operations  
> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  
> **Format:** 100 real-interview-style questions with concise, practical answers  
> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export

---

## Executive Summary

This guide is designed for senior-level AWS interviews where interviewers expect more than service definitions. You should be able to explain architecture trade-offs, IAM and networking controls, high availability, observability, cost optimisation, and governance across accounts.

### What this pack helps you demonstrate
- Strong AWS fundamentals
- Cloud architecture and operations judgement
- Security and governance awareness
- Reliability and cost optimisation thinking
- Clear, structured interview communication

---

## Navigation

| Section | Focus Area |
|---|---|
| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |
| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |
| [AWS Foundations](#aws-foundations) | Core AWS concepts and platform basics |
| [Compute, Networking, and Storage](#compute-networking-and-storage) | Core infrastructure services and design choices |
| [Identity, Security, and Operations](#identity-security-and-operations) | IAM, encryption, monitoring, and operational controls |
| [Reliability, Cost, and Production Practice](#reliability-cost-and-production-practice) | HA, DR, governance, and cost-aware operations |
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
- Awareness of security, reliability, and cost trade-offs

## Interview Answer Framework

Use this structure for most interview answers:

| Step | What to say |
|---|---|
| 1. Define | Explain what the AWS service or concept does |
| 2. Importance | Explain why it matters in cloud operations |
| 3. Practical example | Give a realistic architecture or incident example |
| 4. Troubleshooting angle | Mention logs, metrics, IAM, or network validation steps |
| 5. Safe action | Explain how you reduce risk in production |

### Example senior-style answer
> “I first explain the AWS service clearly, then connect it to architecture and operational impact, and finally describe how I would validate, troubleshoot, secure, or optimise it in a real environment.”

## AWS Foundations

### 1) What is AWS?
**Answer:** AWS is Amazon Web Services, a cloud platform offering compute, storage, networking, databases, security, analytics, and managed services for building scalable systems.

### 2) What are the main AWS service categories used in DevOps?
**Answer:** Compute, storage, networking, IAM, databases, monitoring, security, CI/CD, and container orchestration are the most common categories.

### 3) What is a Region in AWS?
**Answer:** A Region is a geographic area containing multiple isolated Availability Zones.

### 4) What is an Availability Zone?
**Answer:** An Availability Zone is an isolated data centre location within a Region, designed for fault tolerance and high availability.

### 5) Why should production workloads span multiple Availability Zones?
**Answer:** It reduces the risk of single data centre failure and improves resilience and uptime.

### 6) What is EC2?
**Answer:** EC2 is AWS’s virtual machine service used to run compute workloads with flexible instance types and scaling options.

### 7) What is the difference between EC2 and Lambda?
**Answer:** EC2 provides server-based compute you manage, while Lambda is serverless and runs code on demand without server management.

### 8) What is an AMI?
**Answer:** An AMI is an Amazon Machine Image used as the template for launching EC2 instances.

### 9) What is an instance type?
**Answer:** An instance type defines the CPU, memory, storage, and networking capacity of an EC2 instance.

### 10) What is an Auto Scaling Group?
**Answer:** An Auto Scaling Group automatically adjusts the number of EC2 instances based on policies, health checks, or schedules.

### 11) Why is Auto Scaling important?
**Answer:** It improves availability, handles traffic variation, and optimises cost by scaling capacity up or down.

### 12) What is an Elastic Load Balancer?
**Answer:** ELB distributes incoming traffic across multiple targets such as EC2 instances, containers, or IPs.

### 13) What is the difference between ALB and NLB?
**Answer:** ALB works at Layer 7 for HTTP/HTTPS routing, while NLB works at Layer 4 for TCP/UDP and very high performance traffic.

### 14) When would you use an ALB?
**Answer:** Use ALB for web applications needing host-based or path-based routing, TLS termination, or HTTP-aware features.

### 15) When would you use an NLB?
**Answer:** Use NLB for TCP/UDP workloads, static IP needs, or very high throughput and low latency requirements.

### 16) What is a VPC?
**Answer:** A VPC is a logically isolated virtual network in AWS where you define subnets, routing, and security boundaries.

### 17) What is a subnet?
**Answer:** A subnet is a segmented IP range inside a VPC, usually classified as public or private based on routing.

### 18) What is the difference between public and private subnet?
**Answer:** A public subnet has a route to an Internet Gateway, while a private subnet does not expose resources directly to the internet.

### 19) What is an Internet Gateway?
**Answer:** An Internet Gateway enables internet connectivity for resources in public subnets.

### 20) What is a NAT Gateway?
**Answer:** A NAT Gateway allows instances in private subnets to access the internet outbound without being directly reachable inbound.

### 21) Why place application servers in private subnets?
**Answer:** It reduces exposure to the internet and improves security posture.

### 22) What is a route table?
**Answer:** A route table defines how traffic is directed within a VPC and to external destinations.

### 23) What is a Security Group?
**Answer:** A Security Group is a stateful virtual firewall attached to instances or ENIs controlling inbound and outbound traffic.

### 24) What is a Network ACL?
**Answer:** A Network ACL is a stateless subnet-level firewall controlling inbound and outbound traffic.

### 25) What is the difference between Security Group and NACL?
**Answer:** Security Groups are stateful and attached to resources, while NACLs are stateless and applied at the subnet level.

## Compute, Networking, and Storage

### 26) What is IAM?
**Answer:** IAM is AWS Identity and Access Management, used to control authentication and authorisation for users, roles, and services.

### 27) What is an IAM user?
**Answer:** An IAM user is a long-term identity for a person or application, though roles are preferred for workloads.

### 28) What is an IAM role?
**Answer:** An IAM role is an assumable identity with temporary credentials, commonly used by AWS services and applications.

### 29) Why are IAM roles preferred over access keys?
**Answer:** Roles provide temporary credentials, reduce secret sprawl, and improve security and rotation practices.

### 30) What is an IAM policy?
**Answer:** An IAM policy is a JSON document defining allowed or denied actions on AWS resources.

### 31) What is least privilege in AWS?
**Answer:** It means granting only the minimum permissions required for a task, reducing blast radius and privilege escalation risk.

### 32) What is an IAM trust policy?
**Answer:** A trust policy defines who can assume a role.

### 33) What is STS?
**Answer:** AWS Security Token Service issues temporary credentials for assumed roles and federated access.

### 34) What is MFA in AWS?
**Answer:** Multi-factor authentication adds an extra verification factor for stronger account security.

### 35) Why should root account usage be avoided?
**Answer:** The root account has unrestricted privileges and should be protected tightly and used only for exceptional account-level tasks.

### 36) What is AWS Organizations?
**Answer:** AWS Organizations helps manage multiple AWS accounts centrally with governance and billing controls.

### 37) What is an SCP?
**Answer:** A Service Control Policy sets permission guardrails across accounts in AWS Organizations.

### 38) What is S3?
**Answer:** S3 is AWS object storage used for backups, static assets, logs, data lakes, and many other storage use cases.

### 39) What is the difference between object storage and block storage?
**Answer:** Object storage stores data as objects with metadata, while block storage presents raw volumes for filesystems and databases.

### 40) What is EBS?
**Answer:** EBS is block storage for EC2 instances, commonly used for operating systems, databases, and persistent application data.

### 41) What is EFS?
**Answer:** EFS is a managed shared file storage service that can be mounted by multiple instances.

### 42) When would you use EBS vs EFS?
**Answer:** Use EBS for single-instance block storage and EFS for shared file storage across multiple instances.

### 43) What is S3 versioning?
**Answer:** S3 versioning keeps multiple versions of objects, helping recovery from accidental deletion or overwrite.

### 44) What is S3 lifecycle policy?
**Answer:** It automates object transition to cheaper storage classes or deletion after defined retention periods.

### 45) What is an S3 bucket policy?
**Answer:** It is a resource-based policy controlling access to an S3 bucket and its objects.

### 46) What is pre-signed URL in S3?
**Answer:** A pre-signed URL grants temporary access to a specific object without exposing permanent credentials.

### 47) What is RDS?
**Answer:** RDS is a managed relational database service supporting engines like MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.

### 48) What is Multi-AZ in RDS?
**Answer:** Multi-AZ provides high availability by maintaining a synchronous standby in another Availability Zone.

### 49) What is the difference between Multi-AZ and read replica?
**Answer:** Multi-AZ is for high availability, while read replicas are mainly for read scaling and sometimes disaster recovery.

### 50) What is DynamoDB?
**Answer:** DynamoDB is AWS’s managed NoSQL key-value and document database service.

## Identity, Security, and Operations

### 51) When would you choose DynamoDB over RDS?
**Answer:** Choose DynamoDB for massive scale, low-latency key-value access, and flexible schema requirements.

### 52) What is Route 53?
**Answer:** Route 53 is AWS’s DNS and traffic routing service.

### 53) What is CloudFront?
**Answer:** CloudFront is AWS’s CDN used to cache and deliver content globally with low latency.

### 54) Why use CloudFront with S3?
**Answer:** It improves performance, reduces origin load, and adds security features like TLS and signed access patterns.

### 55) What is CloudWatch?
**Answer:** CloudWatch is AWS’s monitoring and observability service for metrics, logs, alarms, dashboards, and events.

### 56) What is a CloudWatch alarm?
**Answer:** A CloudWatch alarm triggers actions or notifications when a metric crosses a threshold.

### 57) What is CloudWatch Logs?
**Answer:** It is a managed log ingestion and storage service for applications, systems, and AWS services.

### 58) What is CloudTrail?
**Answer:** CloudTrail records AWS API activity for auditing, security analysis, and compliance.

### 59) Why is CloudTrail important?
**Answer:** It provides visibility into who did what, when, and from where across AWS accounts.

### 60) What is AWS Config?
**Answer:** AWS Config tracks resource configuration changes and evaluates compliance against rules.

### 61) What is AWS Systems Manager?
**Answer:** Systems Manager provides operational tools such as Session Manager, Patch Manager, Parameter Store, and automation.

### 62) What is Session Manager?
**Answer:** Session Manager allows secure shell-like access to instances without opening SSH ports or managing bastion hosts.

### 63) What is Parameter Store?
**Answer:** Parameter Store stores configuration values and secrets, though Secrets Manager is often preferred for advanced secret rotation.

### 64) What is Secrets Manager?
**Answer:** Secrets Manager securely stores and rotates secrets such as database credentials and API keys.

### 65) What is KMS?
**Answer:** AWS Key Management Service manages encryption keys used across AWS services and applications.

### 66) Why is KMS important?
**Answer:** It centralises encryption key management, access control, and auditability.

### 67) What is encryption at rest?
**Answer:** It means data is encrypted while stored on disk or in storage services.

### 68) What is encryption in transit?
**Answer:** It means data is encrypted while moving across networks, typically using TLS.

### 69) What is ECS?
**Answer:** ECS is AWS’s managed container orchestration service for running containers on EC2 or Fargate.

### 70) What is EKS?
**Answer:** EKS is AWS’s managed Kubernetes service.

### 71) What is Fargate?
**Answer:** Fargate is serverless compute for containers, removing the need to manage underlying EC2 instances.

### 72) When would you choose ECS over EKS?
**Answer:** ECS is simpler for AWS-native container workloads, while EKS is preferred when Kubernetes ecosystem compatibility is required.

### 73) What is Lambda?
**Answer:** Lambda is AWS’s serverless compute service that runs code in response to events.

### 74) What are common Lambda limitations?
**Answer:** Execution time limits, cold starts, package size constraints, and stateless runtime behaviour are common considerations.

### 75) What is API Gateway?
**Answer:** API Gateway is a managed service for creating, securing, and scaling APIs.

## Reliability, Cost, and Production Practice

### 76) What is SQS?
**Answer:** SQS is a managed message queue service used to decouple systems and smooth traffic spikes.

### 77) What is SNS?
**Answer:** SNS is a pub/sub messaging service used for notifications and fan-out patterns.

### 78) What is the difference between SQS and SNS?
**Answer:** SQS is queue-based point-to-point buffering, while SNS is publish-subscribe fan-out messaging.

### 79) What is EventBridge?
**Answer:** EventBridge is an event bus service for routing events between AWS services and applications.

### 80) What is an EC2 instance profile?
**Answer:** It is the mechanism that attaches an IAM role to an EC2 instance.

### 81) How do you troubleshoot an unreachable EC2 instance?
**Answer:** Check instance status, security groups, NACLs, route tables, subnet, SSH or SSM access, system logs, and OS-level issues.

### 82) How do you troubleshoot high latency in an AWS application?
**Answer:** Check load balancer metrics, instance health, database performance, network paths, scaling behaviour, and recent deployments.

### 83) How do you design a highly available web application in AWS?
**Answer:** Use multiple AZs, load balancers, Auto Scaling, managed databases with failover, object storage, monitoring, backups, and tested recovery plans.

### 84) What is disaster recovery in AWS?
**Answer:** Disaster recovery is the strategy for restoring services after major failure using backups, replication, failover, and recovery procedures.

### 85) What is the difference between RPO and RTO?
**Answer:** RPO is the acceptable data loss window, while RTO is the acceptable recovery time window.

### 86) What is cost optimisation in AWS?
**Answer:** It means designing and operating workloads efficiently using right-sizing, autoscaling, reserved pricing, storage lifecycle policies, and waste reduction.

### 87) What are Reserved Instances or Savings Plans?
**Answer:** They are pricing models that reduce compute cost in exchange for usage commitment.

### 88) What is tagging in AWS?
**Answer:** Tagging adds metadata to resources for ownership, cost allocation, automation, and governance.

### 89) Why is tagging important?
**Answer:** It improves visibility, cost tracking, automation, and operational accountability.

### 90) What is a landing zone?
**Answer:** A landing zone is a preconfigured multi-account AWS environment with baseline networking, security, logging, and governance.

### 91) What is shared responsibility model in AWS?
**Answer:** AWS secures the cloud infrastructure, while customers secure what they run and configure in the cloud.

### 92) What is GuardDuty?
**Answer:** GuardDuty is a threat detection service that analyses logs and events for suspicious activity.

### 93) What is AWS WAF?
**Answer:** AWS WAF protects web applications by filtering malicious HTTP requests.

### 94) What is Shield?
**Answer:** AWS Shield provides DDoS protection for AWS workloads.

### 95) How do you secure AWS in production?
**Answer:** Use least privilege IAM, MFA, logging, encryption, private networking, patching, guardrails, and continuous monitoring.

### 96) How do you use Terraform with AWS safely?
**Answer:** Use remote state, locking, least-privilege roles, reviewed plans, tagging standards, and separate environments or accounts.

### 97) What is your approach to AWS troubleshooting?
**Answer:** I start with impact, then inspect networking, IAM, scaling, logs, metrics, recent changes, and service health before mitigation.

### 98) What is your approach to AWS governance?
**Answer:** I use multi-account design, SCPs, tagging, central logging, IAM standards, encryption defaults, and policy-driven automation.

### 99) What is your approach to AWS reliability?
**Answer:** I design across AZs, automate recovery, monitor SLOs, test failover, and reduce single points of failure.

## Production Interview Mindset

### 100) What is your practical senior-level approach in interviews?
**Answer:** Standardise account structure, secure IAM and networking, automate infrastructure, enforce observability and governance, and optimise for resilience, cost, and operational simplicity.

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

> In senior AWS interviews, explain not only service definitions but also architecture trade-offs, security, high availability, cost control, troubleshooting, and governance across accounts.
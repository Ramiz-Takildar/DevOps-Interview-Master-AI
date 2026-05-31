# Terraform Interview Questions and Answers

> **Senior DevOps Interview Pack**
>
> **Domain:** Terraform concepts, state management, modules, governance, security, and infrastructure operations  
> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  
> **Format:** 100 real-interview-style questions with concise, practical answers  
> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export

---

## Executive Summary

This guide is designed for senior-level Terraform interviews where interviewers expect more than command recall. You should be able to explain state safety, module design, drift handling, governance controls, CI/CD integration, and how to reduce infrastructure blast radius in production.

### What this pack helps you demonstrate
- Strong Terraform fundamentals
- State and backend management judgement
- Governance and security awareness
- Drift, recovery, and rollout discipline
- Clear, structured interview communication

---

## Navigation

| Section | Focus Area |
|---|---|
| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |
| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |
| [Terraform Foundations](#terraform-foundations) | Core Terraform concepts and workflow |
| [State, Modules, and Workflow](#state-modules-and-workflow) | State handling, modules, variables, and execution flow |
| [Security, Governance, and Collaboration](#security-governance-and-collaboration) | Team controls, secrets, policy, and safe collaboration |
| [Troubleshooting, Drift, and Production Practice](#troubleshooting-drift-and-production-practice) | Recovery, upgrades, drift, and operational discipline |
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
- Safe change and rollback thinking
- Awareness of governance, security, and blast radius

## Interview Answer Framework

Use this structure for most interview answers:

| Step | What to say |
|---|---|
| 1. Define | Explain what the Terraform concept or command does |
| 2. Importance | Explain why it matters in infrastructure operations |
| 3. Practical example | Give a realistic provisioning or recovery scenario |
| 4. Troubleshooting angle | Mention plan output, state checks, or validation steps |
| 5. Safe action | Explain how you reduce risk before apply |

### Example senior-style answer
> “I first explain the Terraform concept clearly, then connect it to state safety and operational impact, and finally describe how I would validate, troubleshoot, govern, or recover it in a real environment.”

## Terraform Foundations

### 1) What is Terraform?
**Answer:** Terraform is an infrastructure as code tool that lets you define, provision, and manage infrastructure using declarative configuration files.

### 2) What is infrastructure as code?
**Answer:** Infrastructure as code means managing infrastructure through version-controlled code instead of manual console changes, improving consistency, auditability, and repeatability.

### 3) Why is Terraform popular in DevOps?
**Answer:** It supports multiple cloud providers, encourages reusable modules, enables automation, and helps standardise infrastructure provisioning across environments.

### 4) What language does Terraform use?
**Answer:** Terraform uses HCL, HashiCorp Configuration Language, which is designed to be human-readable and declarative.

### 5) What is a provider in Terraform?
**Answer:** A provider is a plugin that allows Terraform to interact with a specific platform such as AWS, Azure, GCP, Kubernetes, or GitHub.

### 6) What is a resource in Terraform?
**Answer:** A resource is a managed infrastructure object such as a VM, VPC, subnet, security group, or database instance.

### 7) What is a data source in Terraform?
**Answer:** A data source lets Terraform read existing information from a provider without creating or managing that object.

### 8) What is a module in Terraform?
**Answer:** A module is a reusable collection of Terraform resources and logic used to standardise infrastructure patterns.

### 9) What is the root module?
**Answer:** The root module is the main working directory where Terraform commands are executed.

### 10) What is a child module?
**Answer:** A child module is any module called by another module.

### 11) What is Terraform state?
**Answer:** Terraform state is the mapping between configuration and real infrastructure, allowing Terraform to track what exists and what changed.

### 12) Why is state important?
**Answer:** Without state, Terraform cannot reliably determine what to create, update, or destroy.

### 13) Where is Terraform state stored by default?
**Answer:** By default, it is stored locally in a `terraform.tfstate` file.

### 14) Why is local state risky for teams?
**Answer:** Local state makes collaboration difficult, lacks locking, and increases the risk of drift, corruption, or accidental loss.

### 15) What is remote state?
**Answer:** Remote state stores the Terraform state file in a shared backend such as S3, Terraform Cloud, or Azure Storage.

### 16) Why should remote state be used?
**Answer:** It improves collaboration, enables locking, supports recovery, and reduces the risk of conflicting changes.

### 17) What is state locking?
**Answer:** State locking prevents multiple users or pipelines from modifying the same state at the same time.

### 18) How is state locking commonly implemented in AWS?
**Answer:** A common pattern is S3 for state storage and DynamoDB for state locking.

### 19) What is `terraform init`?
**Answer:** `terraform init` initialises the working directory, downloads providers and modules, and configures the backend.

### 20) What is `terraform plan`?
**Answer:** `terraform plan` shows the proposed changes Terraform will make without applying them.

### 21) What is `terraform apply`?
**Answer:** `terraform apply` executes the planned changes and updates infrastructure and state.

### 22) What is `terraform destroy`?
**Answer:** `terraform destroy` removes all resources managed by the current configuration.

### 23) What is `terraform validate`?
**Answer:** `terraform validate` checks whether the configuration syntax and structure are valid.

### 24) What is `terraform fmt`?
**Answer:** `terraform fmt` formats Terraform code consistently according to standard style rules.

### 25) What is `terraform output`?
**Answer:** `terraform output` displays output values defined in the configuration.

## State, Modules, and Workflow

### 26) What is `terraform show`?
**Answer:** `terraform show` displays human-readable details of state or plan files.

### 27) What is `terraform refresh`?
**Answer:** Historically it updated state from real infrastructure, but modern workflows usually rely on `plan` and `apply` instead.

### 28) What is drift in Terraform?
**Answer:** Drift occurs when real infrastructure changes outside Terraform and no longer matches the code or state.

### 29) How do you detect drift?
**Answer:** Use `terraform plan`, scheduled drift detection, and compare actual infrastructure with declared configuration.

### 30) How do you handle drift?
**Answer:** Decide whether to import the manual change into code, revert the manual change, or redesign the module so code remains the source of truth.

### 31) What is `terraform import`?
**Answer:** `terraform import` brings an existing resource under Terraform state management.

### 32) When is import useful?
**Answer:** It is useful when adopting existing infrastructure or recovering state alignment after manual creation.

### 33) What is `terraform taint` conceptually?
**Answer:** It marks a resource for forced recreation, though newer workflows often use `-replace` during planning or apply.

### 34) What is `-replace` in Terraform?
**Answer:** It tells Terraform to recreate a specific resource during the next apply.

### 35) What is a backend in Terraform?
**Answer:** A backend defines where state is stored and how operations like locking are handled.

### 36) Can backend configuration use variables directly?
**Answer:** Not in the same flexible way as normal resources; backend configuration is handled early during initialisation.

### 37) What is an output variable?
**Answer:** An output variable exposes useful values such as IDs, endpoints, or ARNs after apply.

### 38) What is an input variable?
**Answer:** An input variable parameterises Terraform code so the same module can be reused across environments.

### 39) How do you define a variable?
**Answer:** Use a `variable` block with type, description, and optionally default and validation.

### 40) How do you pass variable values?
**Answer:** Through `terraform.tfvars`, CLI flags, environment variables, or workspace-specific configuration.

### 41) What is variable validation?
**Answer:** Variable validation enforces rules on input values to prevent invalid or unsafe configurations.

### 42) What is a local value?
**Answer:** A local value stores reusable expressions inside a module to improve readability and reduce duplication.

### 43) What is interpolation in Terraform?
**Answer:** It is the use of expressions to reference variables, resources, functions, and computed values.

### 44) What is dependency graph in Terraform?
**Answer:** Terraform builds a dependency graph to determine resource creation and update order automatically.

### 45) When do you use `depends_on`?
**Answer:** Use it only when Terraform cannot infer the dependency automatically and explicit ordering is required.

### 46) What is the risk of overusing `depends_on`?
**Answer:** It can make plans slower, less clear, and more tightly coupled than necessary.

### 47) What is `count` in Terraform?
**Answer:** `count` creates multiple instances of a resource based on a numeric value.

### 48) What is `for_each` in Terraform?
**Answer:** `for_each` creates multiple instances based on a map or set, giving more stable addressing than `count` in many cases.

### 49) When is `for_each` better than `count`?
**Answer:** It is better when resources are keyed by names or identifiers and you want stable resource addressing.

### 50) What is the difference between `count.index` and `each.key`?
**Answer:** `count.index` is numeric, while `each.key` refers to the key of the current map or set element.

## Security, Governance, and Collaboration

### 51) What are Terraform workspaces?
**Answer:** Workspaces allow multiple state instances for the same configuration, often used for environment separation.

### 52) Are workspaces enough for full environment isolation?
**Answer:** Not always. Separate directories, repos, or backends are often safer for strong isolation and clearer governance.

### 53) What is a provisioner in Terraform?
**Answer:** A provisioner runs scripts or commands on local or remote systems, but should be used sparingly.

### 54) Why are provisioners discouraged?
**Answer:** They reduce declarative clarity, are harder to test, and can make infrastructure less predictable.

### 55) What is the difference between `null_resource` and real resources?
**Answer:** `null_resource` is often used to trigger actions without managing actual infrastructure, but it should be used carefully.

### 56) What is a Terraform plan file?
**Answer:** A plan file is a saved execution plan that can be reviewed and later applied exactly as generated.

### 57) Why use saved plan files in CI/CD?
**Answer:** They improve approval workflows and ensure the applied changes match the reviewed plan.

### 58) What is `terraform graph`?
**Answer:** It outputs the dependency graph of resources, useful for understanding relationships.

### 59) What is state corruption?
**Answer:** State corruption means the state file is damaged, inconsistent, or no longer accurately reflects infrastructure.

### 60) How do you recover from corrupted state?
**Answer:** Stop changes, back up current state, inspect backend history, restore a known good version if possible, and reconcile carefully.

### 61) Why is state recovery risky?
**Answer:** Incorrect recovery can cause Terraform to recreate or destroy production resources unexpectedly.

### 62) What is `terraform state list`?
**Answer:** It lists resources currently tracked in state.

### 63) What is `terraform state show`?
**Answer:** It displays detailed state information for a specific resource.

### 64) What is `terraform state rm`?
**Answer:** It removes a resource from state without deleting the real infrastructure.

### 65) When is `terraform state rm` useful?
**Answer:** It is useful when you want Terraform to stop managing a resource or prepare for re-import.

### 66) What is `terraform state mv`?
**Answer:** It moves resource addresses in state, useful during refactoring or module restructuring.

### 67) What is module versioning?
**Answer:** Module versioning pins reusable modules to known versions so changes are controlled and reproducible.

### 68) Why should module versions be pinned?
**Answer:** Pinning avoids unexpected behaviour from upstream changes and improves repeatability.

### 69) What makes a good Terraform module?
**Answer:** A good module is reusable, well-documented, secure by default, versioned, and exposes only necessary inputs and outputs.

### 70) What are common Terraform anti-patterns?
**Answer:** Large monolithic modules, excessive provisioners, poor variable naming, no remote state, no locking, and mixing unrelated environments.

### 71) How do you structure Terraform for multiple environments?
**Answer:** Use reusable modules with separate environment configurations, isolated state, and clear promotion workflows.

### 72) How do you secure Terraform code?
**Answer:** Avoid hardcoded secrets, use secret managers, enforce least privilege, scan IaC, and review plans before apply.

### 73) Why should secrets not be stored in Terraform code?
**Answer:** Because code and state may expose them, creating long-term security risk.

### 74) Can secrets appear in Terraform state?
**Answer:** Yes, sensitive values can still exist in state even if marked sensitive in outputs.

### 75) What does `sensitive = true` do?
**Answer:** It hides values from normal CLI output, but does not remove them from state storage.

## Troubleshooting, Drift, and Production Practice

### 76) How do you scan Terraform for security issues?
**Answer:** Use tools like Checkov, tfsec, Terrascan, or policy-as-code platforms.

### 77) What is policy as code in Terraform workflows?
**Answer:** It enforces governance rules such as tagging, encryption, network restrictions, and approved instance types before apply.

### 78) What is Terraform Cloud?
**Answer:** Terraform Cloud is a managed service for remote execution, state management, policy enforcement, and collaboration.

### 79) What is the difference between local execution and remote execution?
**Answer:** Local execution runs Terraform on the user or CI machine, while remote execution runs it in a managed or centralised environment.

### 80) What is the benefit of remote execution?
**Answer:** It centralises credentials, improves auditability, and standardises workflow controls.

### 81) How do you use Terraform in CI/CD?
**Answer:** Run fmt, validate, security scans, plan, approval, and apply in controlled stages with remote state and least-privilege credentials.

### 82) Why should apply be restricted in CI/CD?
**Answer:** To prevent unauthorised or accidental infrastructure changes and enforce review gates.

### 83) What is idempotency in Terraform?
**Answer:** Idempotency means repeated applies should converge to the same desired state without unintended changes.

### 84) What breaks idempotency?
**Answer:** Manual changes, unstable inputs, poor module design, or external scripts that change infrastructure unpredictably.

### 85) What is the difference between declarative and imperative provisioning?
**Answer:** Declarative provisioning defines the desired end state, while imperative provisioning defines step-by-step actions.

### 86) Why is Terraform considered declarative?
**Answer:** Because you describe what infrastructure should exist, and Terraform determines how to achieve it.

### 87) What is a lifecycle block?
**Answer:** A lifecycle block customises resource behaviour, such as preventing destroy or ignoring certain changes.

### 88) What does `prevent_destroy` do?
**Answer:** It blocks accidental destruction of critical resources unless explicitly overridden.

### 89) What does `ignore_changes` do?
**Answer:** It tells Terraform to ignore updates to specified attributes, useful in limited cases where external systems manage them.

### 90) What is the risk of overusing `ignore_changes`?
**Answer:** It can hide drift and reduce Terraform’s ability to enforce the declared state.

### 91) How do you manage Terraform code reviews?
**Answer:** Review module design, naming, security, blast radius, plan output, tagging, and whether changes align with architecture standards.

### 92) What is blast radius in Terraform changes?
**Answer:** Blast radius is the scope of infrastructure impact a change can cause if applied incorrectly.

### 93) How do you reduce Terraform blast radius?
**Answer:** Use smaller modules, isolated states, targeted environments, reviewed plans, and staged rollouts.

### 94) What is targeted apply and why is it risky?
**Answer:** Targeted apply changes only selected resources, which can be useful for recovery but risky because it may bypass full dependency context.

### 95) When would you use targeted apply?
**Answer:** Only in controlled troubleshooting or recovery scenarios, not as a normal workflow.

### 96) How do you handle Terraform upgrades?
**Answer:** Review provider and Terraform version changes, test in lower environments, update lock files, and validate plans carefully.

### 97) What is `.terraform.lock.hcl`?
**Answer:** It records provider dependency selections to ensure consistent provider versions across environments.

### 98) What is your approach to Terraform troubleshooting in production?
**Answer:** I inspect plan output, state alignment, provider errors, credentials, dependencies, and recent changes before making any corrective action.

### 99) What is your approach to Terraform governance?
**Answer:** I enforce remote state, locking, module standards, policy checks, security scanning, peer review, and controlled CI/CD execution.

## Production Interview Mindset

### 100) What is your practical senior-level approach in interviews?
**Answer:** Keep infrastructure modular, versioned, secure, and reviewable; isolate state properly; automate plan and apply workflows; and treat state management as a critical operational concern.

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

> In senior Terraform interviews, explain not only commands but also state safety, module design, drift handling, governance, CI/CD integration, and how to reduce infrastructure blast radius.
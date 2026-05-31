# GitHub Actions Interview Questions and Answers

> **Senior DevOps Interview Pack**
>
> **Domain:** GitHub Actions concepts, workflow design, runner strategy, security, and CI/CD operations  
> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  
> **Format:** 100 real-interview-style questions with concise, practical answers  
> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export

---

## Executive Summary

This guide is designed for senior-level GitHub Actions interviews where interviewers expect more than YAML syntax. You should be able to explain security, runner strategy, reusable workflow design, deployment governance, and supply-chain risk control.

### What this pack helps you demonstrate
- Strong GitHub Actions fundamentals
- Workflow and runner design judgement
- Security and governance awareness
- Delivery reliability and troubleshooting discipline
- Clear, structured interview communication

---

## Navigation

| Section | Focus Area |
|---|---|
| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |
| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |
| [GitHub Actions Foundations](#github-actions-foundations) | Core GitHub Actions concepts and workflow basics |
| [Workflows, Runners, and Automation](#workflows-runners-and-automation) | Job design, execution flow, and automation patterns |
| [Security, Reuse, and Governance](#security-reuse-and-governance) | Secrets, OIDC, reusable workflows, and controls |
| [Troubleshooting and Production Practice](#troubleshooting-and-production-practice) | Debugging, optimisation, and deployment discipline |
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
- Awareness of security, reliability, and governance trade-offs

## Interview Answer Framework

Use this structure for most interview answers:

| Step | What to say |
|---|---|
| 1. Define | Explain what the GitHub Actions concept or feature does |
| 2. Importance | Explain why it matters in CI/CD operations |
| 3. Practical example | Give a realistic workflow or deployment example |
| 4. Troubleshooting angle | Mention logs, runner state, permissions, or validation steps |
| 5. Safe action | Explain how you reduce risk in production |

### Example senior-style answer
> “I first explain the GitHub Actions concept clearly, then connect it to delivery reliability and security impact, and finally describe how I would validate, troubleshoot, secure, or optimise it in a real environment.”

## GitHub Actions Foundations

### 1) What is GitHub Actions?
**Answer:** GitHub Actions is GitHub’s native CI/CD and automation platform used to build, test, scan, release, and automate repository workflows.

### 2) Why is GitHub Actions popular in DevOps?
**Answer:** It is tightly integrated with GitHub repositories, supports workflow as code, has a strong marketplace ecosystem, and simplifies CI/CD for teams already using GitHub.

### 3) What is a workflow in GitHub Actions?
**Answer:** A workflow is an automated process defined in YAML under `.github/workflows` that runs one or more jobs based on triggers.

### 4) What is a job?
**Answer:** A job is a set of steps executed on the same runner within a workflow.

### 5) What is a step?
**Answer:** A step is an individual task inside a job, such as running a shell command or invoking an action.

### 6) What is an action?
**Answer:** An action is a reusable unit of automation that performs a specific task inside a workflow.

### 7) What is a runner?
**Answer:** A runner is the compute environment that executes workflow jobs.

### 8) What is the difference between GitHub-hosted and self-hosted runners?
**Answer:** GitHub-hosted runners are managed by GitHub, while self-hosted runners are managed by the user and provide more control but require stronger security and maintenance.

### 9) Where are workflow files stored?
**Answer:** Workflow files are stored in the `.github/workflows` directory of the repository.

### 10) What format do workflow files use?
**Answer:** They use YAML format.

### 11) What is the `on` key in a workflow?
**Answer:** It defines the events that trigger the workflow, such as push, pull request, workflow_dispatch, or schedule.

### 12) What is `workflow_dispatch`?
**Answer:** It allows a workflow to be triggered manually from the GitHub UI or API.

### 13) What is a scheduled workflow?
**Answer:** It is a workflow triggered on a cron schedule using the `schedule` event.

### 14) What is the `push` trigger?
**Answer:** It runs the workflow when commits are pushed to specified branches or tags.

### 15) What is the `pull_request` trigger?
**Answer:** It runs the workflow when pull request events occur, such as open, synchronize, or reopen.

### 16) Why are pull request workflows important?
**Answer:** They provide early validation before code is merged into protected branches.

### 17) What is the difference between `pull_request` and `pull_request_target`?
**Answer:** `pull_request` runs in the context of the PR branch, while `pull_request_target` runs in the base repository context and is more sensitive from a security perspective.

### 18) Why is `pull_request_target` risky?
**Answer:** It can expose secrets or elevated permissions to untrusted pull request code if used incorrectly.

### 19) What is `workflow_call`?
**Answer:** It allows one workflow to be reused and invoked by another workflow.

### 20) What are reusable workflows?
**Answer:** Reusable workflows are centrally defined workflows that can be called by other workflows to standardise CI/CD patterns.

### 21) Why use reusable workflows?
**Answer:** They reduce duplication, improve consistency, and simplify governance across repositories.

### 22) What is the difference between reusable workflows and composite actions?
**Answer:** Reusable workflows orchestrate jobs and workflow logic, while composite actions bundle reusable step logic.

### 23) What is a composite action?
**Answer:** A composite action is a custom action made of multiple workflow steps packaged for reuse.

### 24) What is the `uses` keyword?
**Answer:** It references an action or reusable workflow to be executed.

### 25) What is the `run` keyword?
**Answer:** It executes shell commands directly in a workflow step.

## Workflows, Runners, and Automation

### 26) What is `runs-on`?
**Answer:** It specifies the runner environment for a job, such as `ubuntu-latest` or a self-hosted label.

### 27) What is a matrix strategy?
**Answer:** A matrix strategy runs the same job across multiple combinations such as OS versions, language versions, or environments.

### 28) Why is matrix build useful?
**Answer:** It improves coverage by validating software across multiple runtime combinations efficiently.

### 29) What is `needs` in GitHub Actions?
**Answer:** It defines job dependencies so one job waits for another to complete.

### 30) What is job parallelism?
**Answer:** Jobs without dependency relationships can run in parallel to reduce workflow duration.

### 31) What is `if` condition in workflows?
**Answer:** It controls whether a job or step runs based on expressions and context values.

### 32) What is the `env` key?
**Answer:** It defines environment variables at workflow, job, or step level.

### 33) What is the `defaults` key?
**Answer:** It sets default shell or working-directory behaviour for workflow steps.

### 34) What is `permissions` in GitHub Actions?
**Answer:** It controls the access level of the workflow token for repository operations.

### 35) Why should workflow permissions be minimised?
**Answer:** Least privilege reduces the blast radius if a workflow or action is compromised.

### 36) What is `GITHUB_TOKEN`?
**Answer:** It is an automatically generated token used by workflows to authenticate against GitHub APIs and repository operations.

### 37) What are GitHub Actions secrets?
**Answer:** Secrets are encrypted values stored in GitHub and injected into workflows securely when needed.

### 38) What is the difference between secrets and variables?
**Answer:** Secrets are sensitive encrypted values, while variables are non-sensitive configuration values.

### 39) Why should secrets never be echoed in logs?
**Answer:** They may leak into build logs and compromise systems or environments.

### 40) What is secret masking?
**Answer:** GitHub masks known secret values in logs, though it is not a substitute for safe secret handling.

### 41) What is an environment in GitHub Actions?
**Answer:** An environment is a deployment target configuration that can include secrets, protection rules, and approvals.

### 42) Why use environments?
**Answer:** They help control deployments with approvals, scoped secrets, and environment-specific governance.

### 43) What are environment protection rules?
**Answer:** They are controls such as required reviewers or wait timers before deployment jobs can proceed.

### 44) What is concurrency in GitHub Actions?
**Answer:** Concurrency controls how many workflow runs or jobs can execute simultaneously for a defined group.

### 45) Why is concurrency useful?
**Answer:** It prevents overlapping deployments, reduces race conditions, and avoids wasted compute.

### 46) What does `cancel-in-progress` do?
**Answer:** It cancels older in-progress runs in the same concurrency group when a newer run starts.

### 47) What is caching in GitHub Actions?
**Answer:** Caching stores dependencies or build outputs between runs to improve performance.

### 48) What is the `actions/cache` action used for?
**Answer:** It restores and saves cached files such as package dependencies or build tool caches.

### 49) What is the risk of poor cache key design?
**Answer:** It can cause stale dependencies, inconsistent builds, or low cache hit rates.

### 50) What is an artifact in GitHub Actions?
**Answer:** An artifact is a file or bundle uploaded from a workflow for later download or use.

## Security, Reuse, and Governance

### 51) What is the difference between cache and artifact?
**Answer:** Cache is for speeding up repeated runs, while artifacts are for preserving outputs such as reports or build packages.

### 52) What is `actions/upload-artifact`?
**Answer:** It uploads files generated during a workflow run.

### 53) What is `actions/download-artifact`?
**Answer:** It downloads artifacts produced earlier in the same workflow or run context.

### 54) What is a self-hosted runner group?
**Answer:** It is a logical grouping of self-hosted runners used for access control and workload routing.

### 55) Why are self-hosted runners security-sensitive?
**Answer:** They may have network access, persistent state, and credentials that untrusted code could abuse.

### 56) How do you secure self-hosted runners?
**Answer:** Use isolation, ephemeral runners where possible, least privilege, network segmentation, patching, and avoid exposing them to untrusted pull requests.

### 57) What is an ephemeral runner?
**Answer:** It is a short-lived runner created for a single job or limited use, then destroyed.

### 58) Why are ephemeral runners preferred?
**Answer:** They reduce persistence risk, contamination between jobs, and secret leakage across runs.

### 59) What is OIDC in GitHub Actions?
**Answer:** OpenID Connect allows workflows to obtain short-lived cloud credentials without storing long-lived secrets.

### 60) Why is OIDC better than static cloud credentials?
**Answer:** It reduces secret sprawl, improves rotation, and enables trust-based temporary access.

### 61) How do GitHub Actions integrate with AWS using OIDC?
**Answer:** GitHub issues an identity token, AWS trusts GitHub as an identity provider, and the workflow assumes a role with temporary credentials.

### 62) How do GitHub Actions integrate with Azure using OIDC?
**Answer:** The workflow exchanges an identity token with Azure AD or Entra ID to obtain temporary access for a service principal or federated identity.

### 63) How do GitHub Actions integrate with GCP using OIDC?
**Answer:** The workflow uses workload identity federation to exchange GitHub identity for temporary GCP credentials.

### 64) What is branch protection in relation to GitHub Actions?
**Answer:** Branch protection can require successful workflow checks before allowing merges into protected branches.

### 65) Why are required status checks important?
**Answer:** They enforce quality gates and prevent unvalidated code from being merged.

### 66) What is a status check?
**Answer:** A status check is the reported result of a workflow or job used to indicate pass, fail, or pending state.

### 67) What is a workflow run?
**Answer:** A workflow run is one execution instance of a workflow triggered by an event.

### 68) What is a job output?
**Answer:** A job output is a value produced by one job and consumed by downstream jobs.

### 69) What is a step output?
**Answer:** A step output is a value emitted by a step for later use in the same job or exported upward.

### 70) What is the `outputs` keyword?
**Answer:** It defines values exposed from steps or jobs for reuse.

### 71) What is the `strategy.fail-fast` option?
**Answer:** It controls whether matrix jobs should stop early when one variation fails.

### 72) When should fail-fast be disabled?
**Answer:** Disable it when you want full visibility into all matrix failures instead of stopping at the first one.

### 73) What is `continue-on-error`?
**Answer:** It allows a step or job to fail without failing the entire workflow.

### 74) When should `continue-on-error` be used carefully?
**Answer:** It should be used only for non-critical checks, because it can hide real problems if overused.

### 75) What is a service container in GitHub Actions?
**Answer:** A service container provides supporting services such as databases or caches for a job during execution.

## Troubleshooting and Production Practice

### 76) Why are service containers useful?
**Answer:** They simplify integration testing by providing disposable dependencies close to the runner.

### 77) What is the difference between hosted runners and container jobs?
**Answer:** Hosted runners provide a VM environment, while container jobs run steps inside a specified container image on the runner.

### 78) What is a container job?
**Answer:** A container job runs the job steps inside a Docker container for consistent tooling and environment control.

### 79) What is the benefit of container jobs?
**Answer:** They improve reproducibility and reduce dependency drift across runs.

### 80) What is the GitHub Actions marketplace?
**Answer:** It is a catalog of reusable actions published by GitHub and the community.

### 81) What is the risk of using third-party actions blindly?
**Answer:** They may introduce supply-chain risk, insecure code, or unexpected behaviour.

### 82) How do you use third-party actions safely?
**Answer:** Pin versions, prefer trusted publishers, review source code where possible, and minimise permissions.

### 83) Why should actions be pinned to commit SHA?
**Answer:** Pinning to a commit SHA prevents unexpected changes from mutable tags and improves supply-chain security.

### 84) What is Dependabot’s role with GitHub Actions?
**Answer:** Dependabot can update action versions and dependencies to keep workflows current and secure.

### 85) What is a deployment workflow?
**Answer:** It is a workflow that promotes and deploys validated artifacts to target environments.

### 86) Why should the same artifact be promoted across environments?
**Answer:** It improves traceability and avoids differences caused by rebuilding separately for each environment.

### 87) What is a release workflow?
**Answer:** A release workflow automates versioning, packaging, tagging, publishing, and release notes generation.

### 88) What is `workflow_run`?
**Answer:** It triggers one workflow based on the completion of another workflow.

### 89) When is `workflow_run` useful?
**Answer:** It is useful for chaining workflows such as build followed by deployment or security scanning.

### 90) How do you troubleshoot a failed GitHub Actions workflow?
**Answer:** Check logs, runner environment, permissions, secrets, dependency availability, recent workflow changes, and whether the failure is deterministic or transient.

### 91) How do you troubleshoot slow workflows?
**Answer:** Review cache usage, matrix size, dependency installation time, runner performance, unnecessary steps, and serial bottlenecks.

### 92) How do you optimise GitHub Actions workflows?
**Answer:** Use caching, reusable workflows, path filters, concurrency controls, smaller matrices, and separate fast feedback from slower jobs.

### 93) What are path filters?
**Answer:** Path filters limit workflow execution to changes in specific files or directories.

### 94) Why are path filters useful?
**Answer:** They reduce unnecessary workflow runs and save time and compute cost.

### 95) What is your approach to GitHub Actions security?
**Answer:** Minimise token permissions, use OIDC instead of static secrets, pin actions, isolate runners, protect environments, and avoid exposing secrets to untrusted code.

### 96) What is your approach to GitHub Actions governance?
**Answer:** Standardise reusable workflows, enforce branch protection, review workflow changes carefully, and centralise secure patterns across repositories.

### 97) What is your approach to GitHub Actions troubleshooting?
**Answer:** I start with impact, then inspect logs, event context, permissions, runner state, secrets, and recent workflow or dependency changes.

### 98) What is your approach to GitHub Actions scaling?
**Answer:** Use hosted runners where suitable, self-hosted or ephemeral runners for specialised workloads, and optimise workflows to reduce queue time and cost.

### 99) What is your approach to deployment design in GitHub Actions?
**Answer:** Build once, promote the same artifact, use protected environments, approvals, rollback readiness, and strong observability after deployment.

## Production Interview Mindset

### 100) What is your practical senior-level approach in interviews?
**Answer:** Treat workflows as governed code, standardise reusable patterns, secure identities and runners, enforce branch and environment protections, and optimise for reliability, traceability, and speed.

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

> In senior GitHub Actions interviews, explain not only YAML syntax but also security, runner strategy, reusable workflow design, deployment governance, and supply-chain risk control.
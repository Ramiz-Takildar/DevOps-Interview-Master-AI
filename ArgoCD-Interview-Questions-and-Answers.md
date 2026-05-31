# ArgoCD Interview Questions & Answers

## 📋 Table of Contents

- [Overview](#overview)
- [Interview Preparation Strategy](#interview-preparation-strategy)
- [Core Concepts & Architecture](#core-concepts--architecture)
- [GitOps Principles](#gitops-principles)
- [Applications & Sync](#applications--sync)
- [Projects & RBAC](#projects--rbac)
- [ApplicationSets & Patterns](#applicationsets--patterns)
- [Multi-Cluster Management](#multi-cluster-management)
- [Security & Secrets](#security--secrets)
- [Troubleshooting & Operations](#troubleshooting--operations)
- [Production Best Practices](#production-best-practices)
- [Quick Reference Guide](#quick-reference-guide)

---

## Overview

### Purpose
This comprehensive guide provides 100 carefully curated ArgoCD interview questions designed for **Senior DevOps Engineers, SREs, and Platform Engineers**. Each question includes practical, production-ready answers demonstrating real-world GitOps expertise.

### Target Audience
- **Senior DevOps Engineers** implementing GitOps workflows
- **Site Reliability Engineers** managing Kubernetes deployments
- **Platform Engineers** building deployment platforms
- **Technical Leads** conducting interviews

### What Makes This Guide Different
- ✅ **Production-focused answers** with real GitOps scenarios
- ✅ **Architecture patterns** for scalable deployments
- ✅ **Security best practices** for enterprise environments
- ✅ **Multi-cluster strategies** for complex infrastructures
- ✅ **Troubleshooting approaches** for common issues

---

## Interview Preparation Strategy

### Recommended Study Approach

#### Week 1-2: Foundation Building
1. **Core Concepts** (Questions 1-25)
   - Understand GitOps principles
   - Learn ArgoCD architecture
   - Master application basics

2. **Daily Practice**
   - Read 10-15 questions per day
   - Set up local ArgoCD instance
   - Practice with sample applications

#### Week 3-4: Advanced Topics
1. **Applications & Sync** (Questions 26-50)
   - Master sync strategies
   - Learn ApplicationSets
   - Understand hooks and waves

2. **Multi-Cluster** (Questions 51-75)
   - Learn cluster management
   - Practice RBAC configuration
   - Understand project isolation

#### Week 5-6: Production Readiness
1. **Security & Operations** (Questions 76-100)
   - Understand security patterns
   - Learn troubleshooting approaches
   - Practice production scenarios

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
- Explain **GitOps principles**
- Demonstrate **sync strategies**
- Discuss **security patterns**
- Show **multi-cluster awareness**

#### Red Flags to Avoid
- ❌ Not understanding GitOps principles
- ❌ Ignoring security implications
- ❌ No rollback strategy
- ❌ Lack of production experience
- ❌ Not knowing troubleshooting approaches

---

## Core Concepts & Architecture

### 1. What is ArgoCD?

**Answer:**

**ArgoCD** is a declarative, GitOps continuous delivery tool for Kubernetes that automatically synchronizes cluster state with configurations stored in Git.

**Key Features:**
- **Declarative GitOps:** Git as source of truth
- **Automated sync:** Continuous reconciliation
- **Visual UI:** Application status and health
- **Multi-cluster:** Manage multiple clusters
- **RBAC:** Fine-grained access control

**Architecture:**
```
┌─────────────────────────────────────────┐
│           ArgoCD Components              │
│  ┌──────────────┐  ┌──────────────┐    │
│  │  API Server  │  │ Repo Server  │    │
│  └──────────────┘  └──────────────┘    │
│  ┌──────────────┐  ┌──────────────┐    │
│  │ Application  │  │    Redis     │    │
│  │ Controller   │  │              │    │
│  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────┘
         ↓                    ↓
    ┌─────────┐          ┌─────────┐
    │   Git   │          │Kubernetes│
    │  Repo   │          │ Cluster  │
    └─────────┘          └─────────┘
```

---

### 2. What is GitOps?

**Answer:**

**GitOps** is an operational model where infrastructure and application configurations are stored in Git, and automated processes ensure the actual state matches the desired state.

**Core Principles:**
1. **Declarative:** Describe desired state
2. **Versioned:** Git as single source of truth
3. **Immutable:** Changes through Git commits
4. **Automated:** Continuous reconciliation

**Benefits:**
- Audit trail through Git history
- Easy rollback via Git revert
- Collaboration through pull requests
- Disaster recovery from Git

---

### 3. What are the main ArgoCD components?

**Answer:**

**Components:**

| Component | Purpose |
|-----------|---------|
| **API Server** | Exposes UI, CLI, and API |
| **Repository Server** | Fetches and renders manifests |
| **Application Controller** | Monitors and syncs applications |
| **Redis** | Caching and temporary storage |
| **Dex (optional)** | SSO integration |

---

### 4. What is an ArgoCD Application?

**Answer:**

An **Application** is a Kubernetes custom resource that defines what to deploy, from where (Git), and to which cluster/namespace.

**Example:**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/repo
    targetRevision: main
    path: k8s/overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

---

### 5. What is the difference between desired state and live state?

**Answer:**

- **Desired State:** Configuration in Git repository
- **Live State:** Actual resources in Kubernetes cluster

**ArgoCD continuously compares these states and syncs when differences are detected.**

---

## GitOps Principles

### 6. What is drift in ArgoCD?

**Answer:**

**Drift** occurs when live cluster state differs from desired Git state.

**Causes:**
- Manual kubectl changes
- External controllers modifying resources
- Cluster autoscaling
- Operator modifications

**Detection:**
```bash
# Check sync status
argocd app get my-app

# View differences
argocd app diff my-app
```

---

### 7. What is sync in ArgoCD?

**Answer:**

**Sync** is the process of applying Git manifests to the Kubernetes cluster to match desired state.

**Sync Types:**
- **Manual:** User-triggered
- **Automated:** Automatic on Git changes
- **Selective:** Sync specific resources

---

### 8. What is self-heal?

**Answer:**

**Self-heal** automatically reverts manual changes to match Git state.

**Configuration:**
```yaml
syncPolicy:
  automated:
    selfHeal: true
```

**Use Cases:**
- Prevent configuration drift
- Enforce GitOps compliance
- Automatic recovery from manual changes

---

### 9. What is prune?

**Answer:**

**Prune** removes resources from the cluster that are no longer defined in Git.

**Configuration:**
```yaml
syncPolicy:
  automated:
    prune: true
```

**⚠️ Caution:** Can delete resources if Git configuration is incorrect.

---

### 10. What is sync status?

**Answer:**

**Sync Status** indicates if live state matches desired state.

**States:**
- **Synced:** Matches Git
- **OutOfSync:** Differs from Git
- **Unknown:** Cannot determine

---

## Applications & Sync

### 11. What is health status?

**Answer:**

**Health Status** indicates operational health of deployed resources.

**States:**
- **Healthy:** All resources running correctly
- **Progressing:** Deployment in progress
- **Degraded:** Some resources unhealthy
- **Suspended:** Intentionally paused
- **Missing:** Resources not found
- **Unknown:** Cannot determine

---

### 12. What are sync waves?

**Answer:**

**Sync waves** control the order of resource application during sync.

**Example:**
```yaml
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "0"  # CRDs first
---
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"  # Custom resources second
---
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "2"  # Applications last
```

**Use Cases:**
- Install CRDs before CRs
- Deploy databases before applications
- Manage dependencies

---

### 13. What are ArgoCD hooks?

**Answer:**

**Hooks** are resources that run at specific sync lifecycle phases.

**Hook Types:**
- **PreSync:** Before sync
- **Sync:** During sync
- **PostSync:** After sync
- **SyncFail:** On sync failure
- **Skip:** Skip resource

**Example:**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
  annotations:
    argocd.argoproj.io/hook: PreSync
    argocd.argoproj.io/hook-delete-policy: HookSucceeded
spec:
  template:
    spec:
      containers:
      - name: migrate
        image: migrate:latest
      restartPolicy: Never
```

---

### 14. What are sync options?

**Answer:**

**Sync options** customize sync behavior.

**Common Options:**
```yaml
syncPolicy:
  syncOptions:
  - CreateNamespace=true      # Auto-create namespace
  - PruneLast=true            # Prune after sync
  - ApplyOutOfSyncOnly=true   # Only apply changed resources
  - ServerSideApply=true      # Use server-side apply
  - Validate=false            # Skip validation
```

---

### 15. What is selective sync?

**Answer:**

**Selective sync** applies only specific resources instead of the entire application.

**Use Cases:**
- Emergency fixes
- Partial deployments
- Testing specific resources

**⚠️ Caution:** Can break GitOps consistency if overused.

---

## Projects & RBAC

### 16. What is an ArgoCD Project?

**Answer:**

A **Project** provides logical grouping and access control for applications.

**Example:**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: production
  namespace: argocd
spec:
  description: Production applications
  sourceRepos:
  - 'https://github.com/org/*'
  destinations:
  - namespace: 'prod-*'
    server: https://kubernetes.default.svc
  clusterResourceWhitelist:
  - group: ''
    kind: Namespace
  namespaceResourceBlacklist:
  - group: ''
    kind: ResourceQuota
```

**Benefits:**
- Multi-tenancy
- Access control
- Resource restrictions
- Compliance enforcement

---

### 17. What is RBAC in ArgoCD?

**Answer:**

**RBAC** controls user and group permissions for applications and projects.

**Permission Levels:**
- **Read:** View applications
- **Sync:** Trigger sync
- **Override:** Override sync policies
- **Action:** Execute actions
- **Delete:** Delete applications
- **Create:** Create applications

**Example:**
```csv
p, role:dev-team, applications, get, production/*, allow
p, role:dev-team, applications, sync, production/*, allow
p, role:dev-team, applications, delete, production/*, deny
g, dev-group, role:dev-team
```

---

### 18. How do you implement SSO in ArgoCD?

**Answer:**

**SSO Integration** via Dex or direct OIDC.

**Configuration:**
```yaml
# argocd-cm ConfigMap
data:
  url: https://argocd.example.com
  dex.config: |
    connectors:
    - type: oidc
      id: google
      name: Google
      config:
        issuer: https://accounts.google.com
        clientID: $GOOGLE_CLIENT_ID
        clientSecret: $GOOGLE_CLIENT_SECRET
```

---

### 19. What authentication methods does ArgoCD support?

**Answer:**

**Authentication Methods:**
- Local users (built-in)
- SSO via Dex (OIDC, SAML, LDAP, GitHub, GitLab)
- Direct OIDC
- Webhook authentication

---

### 20. How do you secure repository access?

**Answer:**

**Repository Credentials:**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: private-repo
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  type: git
  url: https://github.com/org/private-repo
  password: $GITHUB_TOKEN
  username: not-used
```

**Methods:**
- HTTPS with tokens
- SSH keys
- GitHub App credentials

---

## ApplicationSets & Patterns

### 21. What is an ApplicationSet?

**Answer:**

**ApplicationSet** generates multiple Applications from templates using generators.

**Example:**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: cluster-apps
spec:
  generators:
  - list:
      elements:
      - cluster: prod-us-east
        url: https://prod-us-east.k8s.local
      - cluster: prod-eu-west
        url: https://prod-eu-west.k8s.local
  template:
    metadata:
      name: '{{cluster}}-app'
    spec:
      project: default
      source:
        repoURL: https://github.com/org/repo
        path: apps
      destination:
        server: '{{url}}'
        namespace: default
```

---

### 22. What generators does ApplicationSet support?

**Answer:**

**Generator Types:**

| Generator | Purpose |
|-----------|---------|
| **List** | Static list of parameters |
| **Cluster** | Registered clusters |
| **Git** | Directories or files in Git |
| **Matrix** | Combine multiple generators |
| **Merge** | Merge generator outputs |
| **SCM Provider** | GitHub/GitLab repositories |
| **Pull Request** | Open pull requests |

---

### 23. What is the Git directory generator?

**Answer:**

**Git Directory Generator** creates Applications for each directory in a Git path.

**Example:**
```yaml
generators:
- git:
    repoURL: https://github.com/org/apps
    revision: HEAD
    directories:
    - path: apps/*
```

**Use Case:** Monorepo with multiple applications.

---

### 24. What is the cluster generator?

**Answer:**

**Cluster Generator** creates Applications for each registered cluster.

**Example:**
```yaml
generators:
- clusters:
    selector:
      matchLabels:
        environment: production
```

---

### 25. What is the app-of-apps pattern?

**Answer:**

**App-of-Apps** is a pattern where one Application manages multiple child Applications.

**Example:**
```yaml
# parent-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: parent-app
spec:
  source:
    repoURL: https://github.com/org/repo
    path: apps
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
```

**Directory Structure:**
```
apps/
├── app1.yaml
├── app2.yaml
└── app3.yaml
```

**Benefits:**
- Bootstrap entire environments
- Manage related applications
- Hierarchical organization

---

## Multi-Cluster Management

### 26. How do you add a cluster to ArgoCD?

**Answer:**

**Add Cluster:**
```bash
# Using kubeconfig context
argocd cluster add prod-cluster

# List clusters
argocd cluster list

# Remove cluster
argocd cluster rm https://prod-cluster.k8s.local
```

**What Happens:**
- Creates ServiceAccount in target cluster
- Stores credentials in ArgoCD
- Registers cluster for deployment

---

### 27. What are cluster credentials?

**Answer:**

**Cluster credentials** are stored as Kubernetes Secrets in ArgoCD namespace.

**Secret Structure:**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cluster-prod
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: cluster
stringData:
  name: prod-cluster
  server: https://prod.k8s.local
  config: |
    {
      "bearerToken": "...",
      "tlsClientConfig": {...}
    }
```

---

### 28. How do you implement multi-tenancy?

**Answer:**

**Multi-Tenancy Strategies:**

1. **Project-based:**
```yaml
# Team A project
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: team-a
spec:
  destinations:
  - namespace: 'team-a-*'
    server: '*'
  sourceRepos:
  - 'https://github.com/org/team-a-*'
```

2. **Namespace-based:** Separate namespaces per team
3. **Cluster-based:** Dedicated clusters per team

---

### 29. What is namespace auto-creation?

**Answer:**

**Namespace auto-creation** automatically creates target namespaces during sync.

**Configuration:**
```yaml
syncPolicy:
  syncOptions:
  - CreateNamespace=true
```

---

### 30. How do you handle cluster-scoped resources?

**Answer:**

**Cluster-scoped resources** (Namespaces, CRDs, ClusterRoles) require special permissions.

**Project Configuration:**
```yaml
spec:
  clusterResourceWhitelist:
  - group: ''
    kind: Namespace
  - group: 'apiextensions.k8s.io'
    kind: CustomResourceDefinition
```

---

## Security & Secrets

### 31. How do you handle secrets in GitOps?

**Answer:**

**Secret Management Strategies:**

1. **Sealed Secrets:**
```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: my-secret
spec:
  encryptedData:
    password: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq...
```

2. **External Secrets Operator:**
```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: my-secret
spec:
  secretStoreRef:
    name: aws-secrets-manager
  target:
    name: my-secret
  data:
  - secretKey: password
    remoteRef:
      key: prod/db/password
```

3. **SOPS:** Encrypt files in Git
4. **Vault:** HashiCorp Vault integration

---

### 32. What is Sealed Secrets?

**Answer:**

**Sealed Secrets** encrypts secrets that can be safely stored in Git.

**Workflow:**
```bash
# Install controller
kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.18.0/controller.yaml

# Seal a secret
kubeseal < secret.yaml > sealed-secret.yaml

# Commit sealed-secret.yaml to Git
```

---

### 33. What is External Secrets Operator?

**Answer:**

**External Secrets Operator** syncs secrets from external secret managers to Kubernetes.

**Supported Backends:**
- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager
- HashiCorp Vault
- 1Password

---

### 34. How do you secure ArgoCD itself?

**Answer:**

**Security Measures:**

1. **Enable TLS:**
```yaml
server:
  extraArgs:
  - --insecure=false
```

2. **Implement RBAC:**
```yaml
# Restrict permissions
policy.csv: |
  p, role:readonly, applications, get, */*, allow
  g, readonly-group, role:readonly
```

3. **Use SSO:** Integrate with identity provider
4. **Network Policies:** Restrict access
5. **Audit Logging:** Track all actions

---

### 35. What are ArgoCD security best practices?

**Answer:**

**Best Practices:**
- ✅ Enable SSO authentication
- ✅ Implement least-privilege RBAC
- ✅ Use TLS for all connections
- ✅ Encrypt secrets (Sealed Secrets, SOPS)
- ✅ Restrict repository access
- ✅ Enable audit logging
- ✅ Regular security updates
- ✅ Network segmentation

---

## Troubleshooting & Operations

### 36. How do you troubleshoot OutOfSync status?

**Answer:**

**Troubleshooting Steps:**

1. **View Differences:**
```bash
argocd app diff my-app
```

2. **Check Ignored Differences:**
```yaml
spec:
  ignoreDifferences:
  - group: apps
    kind: Deployment
    jsonPointers:
    - /spec/replicas
```

3. **Verify Git Source:**
```bash
argocd app get my-app --show-params
```

4. **Check Manual Changes:**
```bash
kubectl get deployment my-app -o yaml
```

---

### 37. How do you troubleshoot Degraded status?

**Answer:**

**Investigation:**

1. **Check Resource Health:**
```bash
argocd app get my-app --show-operation
```

2. **View Pod Status:**
```bash
kubectl get pods -n production
kubectl describe pod my-app-xxx
```

3. **Check Events:**
```bash
kubectl get events -n production --sort-by='.lastTimestamp'
```

4. **Review Logs:**
```bash
kubectl logs -n production deployment/my-app
```

---

### 38. How do you troubleshoot sync failures?

**Answer:**

**Common Causes:**

1. **Invalid Manifests:**
```bash
# Validate locally
kubectl apply --dry-run=client -f manifest.yaml
```

2. **RBAC Issues:**
```bash
# Check ArgoCD permissions
kubectl auth can-i create deployment --as=system:serviceaccount:argocd:argocd-application-controller -n production
```

3. **Missing CRDs:**
```bash
kubectl get crd
```

4. **Hook Failures:**
```bash
argocd app get my-app --show-operation
```

---

### 39. How do you troubleshoot repository connection issues?

**Answer:**

**Troubleshooting:**

1. **Test Connectivity:**
```bash
# From ArgoCD pod
kubectl exec -n argocd argocd-repo-server-xxx -- git ls-remote https://github.com/org/repo
```

2. **Verify Credentials:**
```bash
argocd repo list
argocd repo get https://github.com/org/repo
```

3. **Check Logs:**
```bash
kubectl logs -n argocd deployment/argocd-repo-server
```

---

### 40. How do you debug ApplicationSet issues?

**Answer:**

**Debugging Steps:**

1. **Check Generated Applications:**
```bash
kubectl get applications -n argocd
```

2. **View ApplicationSet Status:**
```bash
kubectl get applicationset my-appset -o yaml
```

3. **Check Controller Logs:**
```bash
kubectl logs -n argocd deployment/argocd-applicationset-controller
```

4. **Validate Generator:**
```bash
# Test Git generator
git ls-remote https://github.com/org/repo
```

---

## Production Best Practices

### 41. What are ArgoCD deployment best practices?

**Answer:**

**Best Practices:**

1. **High Availability:**
```yaml
# Multiple replicas
replicaCount: 3

# Pod anti-affinity
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchLabels:
          app.kubernetes.io/name: argocd-server
      topologyKey: kubernetes.io/hostname
```

2. **Resource Limits:**
```yaml
resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi
```

3. **Monitoring:** Prometheus metrics
4. **Backup:** Regular backups of ArgoCD data

---

### 42. What are Git repository best practices?

**Answer:**

**Repository Structure:**
```
repo/
├── apps/
│   ├── production/
│   │   ├── app1/
│   │   └── app2/
│   └── staging/
│       ├── app1/
│       └── app2/
├── base/
│   └── common-resources/
└── overlays/
    ├── production/
    └── staging/
```

**Best Practices:**
- ✅ Separate environments
- ✅ Use Kustomize overlays
- ✅ Protected branches
- ✅ Pull request reviews
- ✅ Clear commit messages
- ✅ Tag releases

---

### 43. What are application design best practices?

**Answer:**

**Best Practices:**

1. **Clear Naming:**
```yaml
metadata:
  name: production-api-v2
```

2. **Proper Project Assignment:**
```yaml
spec:
  project: production
```

3. **Automated Sync (with caution):**
```yaml
syncPolicy:
  automated:
    prune: true
    selfHeal: true
  syncOptions:
  - CreateNamespace=true
```

4. **Health Checks:**
```yaml
spec:
  ignoreDifferences:
  - group: apps
    kind: Deployment
    jsonPointers:
    - /spec/replicas  # Ignore HPA changes
```

---

### 44. How do you implement progressive delivery?

**Answer:**

**Progressive Delivery Strategies:**

1. **Blue-Green:**
```yaml
# Deploy new version
- name: app-green
  image: app:v2

# Switch traffic
service:
  selector:
    version: green
```

2. **Canary with Argo Rollouts:**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: my-app
spec:
  strategy:
    canary:
      steps:
      - setWeight: 20
      - pause: {duration: 5m}
      - setWeight: 50
      - pause: {duration: 5m}
```

3. **Feature Flags:** External feature flag system

---

### 45. How do you handle rollbacks?

**Answer:**

**Rollback Strategies:**

1. **ArgoCD Rollback:**
```bash
# Rollback to previous version
argocd app rollback my-app

# Rollback to specific revision
argocd app rollback my-app 123
```

2. **Git Revert (Preferred):**
```bash
git revert HEAD
git push origin main
# ArgoCD auto-syncs
```

**Why Git Revert is Better:**
- Maintains GitOps principles
- Audit trail in Git
- Reproducible
- Team visibility

---

### 46. How do you monitor ArgoCD?

**Answer:**

**Monitoring:**

1. **Prometheus Metrics:**
```yaml
# ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: argocd-metrics
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: argocd-server
  endpoints:
  - port: metrics
```

2. **Key Metrics:**
```promql
# Application sync status
argocd_app_info

# Sync failures
rate(argocd_app_sync_total{phase="Failed"}[5m])

# API request duration
argocd_api_request_duration_seconds
```

3. **Alerts:**
```yaml
- alert: ArgoCDSyncFailed
  expr: argocd_app_sync_total{phase="Failed"} > 0
  annotations:
    summary: "ArgoCD sync failed for {{ $labels.name }}"
```

---

### 47. How do you backup ArgoCD?

**Answer:**

**Backup Strategy:**

1. **Export Applications:**
```bash
# Backup all applications
argocd app list -o yaml > apps-backup.yaml

# Backup specific app
argocd app get my-app -o yaml > my-app-backup.yaml
```

2. **Backup ArgoCD Configuration:**
```bash
# ConfigMaps and Secrets
kubectl get configmap -n argocd -o yaml > argocd-config-backup.yaml
kubectl get secret -n argocd -o yaml > argocd-secrets-backup.yaml
```

3. **Automated Backup:**
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: argocd-backup
spec:
  schedule: "0 2 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: argocd:latest
            command:
            - /bin/sh
            - -c
            - argocd app list -o yaml > /backup/apps.yaml
```

---

### 48. What is your disaster recovery strategy?

**Answer:**

**DR Strategy:**

1. **Git as Source of Truth:** All configurations in Git
2. **Regular Backups:** Automated ArgoCD backups
3. **Documentation:** Recovery procedures
4. **Testing:** Regular DR drills
5. **Multi-Region:** Deploy ArgoCD in multiple regions

**Recovery Steps:**
```bash
# 1. Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# 2. Restore configuration
kubectl apply -f argocd-config-backup.yaml

# 3. Restore applications
kubectl apply -f apps-backup.yaml

# 4. Sync all applications
argocd app sync --all
```

---

### 49. How do you handle CRDs in GitOps?

**Answer:**

**CRD Management:**

1. **Separate Application for CRDs:**
```yaml
# crds-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: crds
spec:
  syncPolicy:
    syncOptions:
    - Replace=true  # Replace instead of apply
```

2. **Use Sync Waves:**
```yaml
# CRD
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "-1"

# CR
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "0"
```

3. **Skip Pruning:**
```yaml
metadata:
  annotations:
    argocd.argoproj.io/sync-options: Prune=false
```

---

### 50. What are common ArgoCD anti-patterns?

**Answer:**

**Anti-Patterns:**

- ❌ Manual kubectl changes instead of Git
- ❌ Storing secrets in plain text in Git
- ❌ No RBAC configuration
- ❌ Single cluster for all environments
- ❌ No backup strategy
- ❌ Overly complex ApplicationSets
- ❌ Ignoring too many diffs
- ❌ No monitoring or alerting

---

## Quick Reference Guide

### Essential Commands

```bash
# Application Management
argocd app create my-app --repo https://github.com/org/repo --path k8s --dest-server https://kubernetes.default.svc --dest-namespace default
argocd app list
argocd app get my-app
argocd app sync my-app
argocd app delete my-app

# Sync Operations
argocd app sync my-app --prune
argocd app sync my-app --dry-run
argocd app diff my-app
argocd app rollback my-app

# Cluster Management
argocd cluster add prod-cluster
argocd cluster list
argocd cluster rm https://prod.k8s.local

# Repository Management
argocd repo add https://github.com/org/repo --username user --password token
argocd repo list

# Project Management
argocd proj create production
argocd proj list
argocd proj get production
```

### Application YAML Template

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
  finalizers:
  - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/org/repo
    targetRevision: HEAD
    path: k8s/overlays/production
    kustomize:
      images:
      - my-app:v1.2.3
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

### ApplicationSet Template

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: cluster-apps
spec:
  generators:
  - list:
      elements:
      - cluster: prod
        url: https://prod.k8s.local
      - cluster: staging
        url: https://staging.k8s.local
  template:
    metadata:
      name: '{{cluster}}-app'
    spec:
      project: default
      source:
        repoURL: https://github.com/org/repo
        targetRevision: HEAD
        path: 'apps/{{cluster}}'
      destination:
        server: '{{url}}'
        namespace: default
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

---

## Final Interview Tips

### What Interviewers Look For

1. **Technical Depth**
   - Understanding of GitOps principles
   - ArgoCD architecture knowledge
   - Sync strategy expertise
   - Security awareness

2. **Production Experience**
   - Real-world examples
   - Troubleshooting stories
   - Multi-cluster management
   - Incident response

3. **Best Practices**
   - Git workflow design
   - RBAC implementation
   - Secret management
   - Operational maturity

### Red Flags to Avoid

- ❌ Not understanding GitOps
- ❌ Manual cluster changes
- ❌ Ignoring security
- ❌ No rollback strategy
- ❌ Lack of production experience

### Success Factors

- ✅ Explain concepts clearly
- ✅ Provide production examples
- ✅ Discuss trade-offs
- ✅ Show systematic thinking
- ✅ Demonstrate troubleshooting skills
- ✅ Mention best practices

### Key Takeaways

- **Git is source of truth** - All changes through Git
- **Automation with safety** - Automated sync with proper controls
- **Security matters** - Protect secrets and access
- **Monitor everything** - Track sync status and health
- **Plan for failure** - Have rollback and DR strategies

---

**Good luck with your interview! Remember: Focus on understanding GitOps principles deeply, practice with real ArgoCD deployments, and always think about production implications.**
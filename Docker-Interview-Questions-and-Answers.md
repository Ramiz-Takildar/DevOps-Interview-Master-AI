# Docker Interview Questions and Answers

> **Senior DevOps Interview Pack**
>
> **Domain:** Docker concepts, image design, runtime behaviour, troubleshooting, security, and operations  
> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  
> **Format:** 100 real-interview-style questions with concise, practical answers  
> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export

---

## Executive Summary

This guide is designed for senior-level Docker interviews where interviewers expect more than command recall. You should be able to explain container fundamentals, image design, runtime isolation, security controls, troubleshooting flow, and how Docker fits into CI/CD and production platforms.

### What this pack helps you demonstrate
- Strong Docker fundamentals
- Image build and runtime judgement
- Security and operational awareness
- Troubleshooting and rollback thinking
- Clear, structured interview communication

---

## Navigation

| Section | Focus Area |
|---|---|
| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |
| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |
| [Docker Foundations](#docker-foundations) | Core Docker concepts and architecture |
| [Images, Containers, and Builds](#images-containers-and-builds) | Dockerfiles, layers, builds, and packaging |
| [Networking, Storage, and Runtime](#networking-storage-and-runtime) | Runtime behaviour, networking, and persistence |
| [Security, Troubleshooting, and Production Practice](#security-troubleshooting-and-production-practice) | Hardening, debugging, and production usage |
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
| 1. Define | Explain what the Docker concept or command does |
| 2. Importance | Explain why it matters in delivery or operations |
| 3. Practical example | Give a realistic build, deployment, or incident example |
| 4. Troubleshooting angle | Mention logs, inspection steps, or runtime validation |
| 5. Safe action | Explain how you reduce risk in production |

### Example senior-style answer
> “I first explain the Docker concept clearly, then connect it to runtime behaviour and operational impact, and finally describe how I would validate, troubleshoot, secure, or roll back it in a real environment.”

## Docker Foundations

### 1) What is Docker?
**Answer:** Docker is a containerisation platform that packages applications and their dependencies into portable containers that run consistently across environments.

### 2) What is the difference between a container and a virtual machine?
**Answer:** A VM virtualises hardware and runs a full guest OS, while a container shares the host kernel and isolates processes using namespaces and cgroups.

### 3) Why are containers faster than VMs?
**Answer:** Containers do not boot a full guest OS, so they start faster, use fewer resources, and are more efficient for microservices and CI/CD workloads.

### 4) What is a Docker image?
**Answer:** A Docker image is a read-only template containing application code, runtime, libraries, and metadata used to create containers.

### 5) What is a Docker container?
**Answer:** A container is a running instance of a Docker image with its own isolated process space, filesystem view, and network stack.

### 6) What is a Dockerfile?
**Answer:** A Dockerfile is a declarative file containing instructions to build a Docker image layer by layer.

### 7) What is Docker Engine?
**Answer:** Docker Engine is the runtime that builds, runs, and manages containers and images on a host.

### 8) What is Docker Hub?
**Answer:** Docker Hub is a public and private image registry used to store and distribute container images.

### 9) What is a registry?
**Answer:** A registry is a service that stores and serves container images, such as Docker Hub, ECR, GCR, or ACR.

### 10) What is the difference between image and container?
**Answer:** An image is the packaged blueprint, while a container is the live running instance created from that image.

### 11) How do you build a Docker image?
**Answer:** Use `docker build -t image-name:tag .`.

### 12) How do you run a container?
**Answer:** Use `docker run image-name` with required flags for ports, environment variables, volumes, and restart behaviour.

### 13) How do you list running containers?
**Answer:** Use `docker ps`.

### 14) How do you list all containers including stopped ones?
**Answer:** Use `docker ps -a`.

### 15) How do you list images?
**Answer:** Use `docker images`.

### 16) How do you stop a running container?
**Answer:** Use `docker stop <container>` for graceful shutdown.

### 17) How do you force stop a container?
**Answer:** Use `docker kill <container>` if graceful stop fails.

### 18) How do you remove a container?
**Answer:** Use `docker rm <container>`.

### 19) How do you remove an image?
**Answer:** Use `docker rmi <image>`.

### 20) What is the difference between CMD and ENTRYPOINT?
**Answer:** ENTRYPOINT defines the main executable, while CMD provides default arguments or fallback command values.

### 21) When should you use ENTRYPOINT?
**Answer:** Use ENTRYPOINT when the container should always run a specific executable.

### 22) When should you use CMD?
**Answer:** Use CMD when you want to provide default arguments or a default command that users can override.

### 23) What does `FROM` do in a Dockerfile?
**Answer:** It defines the base image for the build.

### 24) What does `RUN` do in a Dockerfile?
**Answer:** It executes commands during image build and creates a new image layer.

### 25) What does `COPY` do?
**Answer:** It copies files from the build context into the image.

## Images, Containers, and Builds

### 26) What does `ADD` do?
**Answer:** It copies files like COPY but also supports remote URLs and automatic archive extraction, though COPY is usually preferred for clarity.

### 27) What does `WORKDIR` do?
**Answer:** It sets the working directory for subsequent Dockerfile instructions.

### 28) What does `EXPOSE` do?
**Answer:** It documents which port the containerised application listens on, but does not publish the port by itself.

### 29) What does `ENV` do?
**Answer:** It sets environment variables inside the image or container.

### 30) What does `ARG` do?
**Answer:** ARG defines build-time variables available only during image build unless explicitly persisted.

### 31) What is the difference between ARG and ENV?
**Answer:** ARG is for build-time configuration, while ENV persists into the final image and runtime container.

### 32) What is a Docker layer?
**Answer:** Each Dockerfile instruction creates a cached filesystem layer, helping reuse unchanged build steps.

### 33) Why does layer ordering matter?
**Answer:** Proper ordering improves build cache efficiency and reduces rebuild time when source code changes.

### 34) How do you reduce Docker image size?
**Answer:** Use minimal base images, multi-stage builds, `.dockerignore`, fewer layers, and avoid unnecessary packages and tools.

### 35) What is a multi-stage build?
**Answer:** It uses multiple `FROM` stages so build dependencies stay in earlier stages and only the final runtime artifacts are copied into the final image.

### 36) Why are multi-stage builds useful?
**Answer:** They reduce image size, improve security, and keep runtime images cleaner.

### 37) What is `.dockerignore`?
**Answer:** It excludes files from the build context, reducing build time and preventing unwanted files from entering the image.

### 38) Why should secrets never be copied into an image?
**Answer:** Because image layers are persistent and secrets can be extracted later even if deleted in later layers.

### 39) How do you pass environment variables to a container?
**Answer:** Use `docker run -e KEY=value` or environment files.

### 40) How do you map ports in Docker?
**Answer:** Use `-p hostPort:containerPort`.

### 41) What is the difference between EXPOSE and `-p`?
**Answer:** EXPOSE is documentation inside the image, while `-p` actually publishes the port to the host.

### 42) What is a bind mount?
**Answer:** A bind mount maps a host path directly into the container.

### 43) What is a Docker volume?
**Answer:** A volume is Docker-managed persistent storage decoupled from the container lifecycle.

### 44) What is the difference between bind mount and volume?
**Answer:** Bind mounts use host filesystem paths directly, while volumes are managed by Docker and are more portable and safer for persistent data.

### 45) When should you use volumes?
**Answer:** Use volumes for databases, persistent application data, and stateful workloads.

### 46) How do you inspect container logs?
**Answer:** Use `docker logs <container>`.

### 47) How do you inspect a running container?
**Answer:** Use `docker inspect <container>` for metadata and configuration details.

### 48) How do you enter a running container?
**Answer:** Use `docker exec -it <container> sh` or `bash` if available.

### 49) What is the difference between `docker exec` and `docker attach`?
**Answer:** `docker exec` starts a new process inside the container, while `docker attach` connects to the main running process.

### 50) How do you troubleshoot a container that exits immediately?
**Answer:** Check `docker logs`, entrypoint command, missing dependencies, environment variables, permissions, and whether the main process is terminating.

## Networking, Storage, and Runtime

### 51) What does exit code 137 usually indicate?
**Answer:** It often indicates the container was killed, commonly due to OOM or forced termination.

### 52) What does exit code 143 usually indicate?
**Answer:** It usually means the container received SIGTERM and shut down gracefully.

### 53) How do you check resource usage of containers?
**Answer:** Use `docker stats`.

### 54) How do you limit CPU and memory for a container?
**Answer:** Use flags like `--memory`, `--cpus`, and related resource constraints during `docker run`.

### 55) Why should containers have resource limits?
**Answer:** Limits prevent noisy-neighbour issues, improve host stability, and reduce blast radius during failures.

### 56) What is Docker networking?
**Answer:** Docker networking provides isolated communication between containers, hosts, and external systems using drivers like bridge, host, and overlay.

### 57) What is the default Docker network?
**Answer:** The default is the bridge network for standalone containers.

### 58) What is bridge networking?
**Answer:** Bridge networking creates an isolated virtual network on the host for containers to communicate.

### 59) What is host networking?
**Answer:** Host networking makes the container share the host network namespace, removing network isolation.

### 60) What is overlay networking?
**Answer:** Overlay networking connects containers across multiple Docker hosts, commonly used in Swarm or clustered environments.

### 61) How do containers communicate on the same custom bridge network?
**Answer:** They can resolve each other by container name or service name using Docker’s embedded DNS.

### 62) What is Docker Compose?
**Answer:** Docker Compose defines and runs multi-container applications using a YAML file.

### 63) Why is Docker Compose useful?
**Answer:** It simplifies local development and integration testing by managing multiple services, networks, and volumes together.

### 64) How do you start services with Compose?
**Answer:** Use `docker compose up -d`.

### 65) How do you stop Compose services?
**Answer:** Use `docker compose down`.

### 66) What is the difference between `docker compose up` and `down`?
**Answer:** `up` creates and starts services, while `down` stops and removes containers, networks, and optionally volumes.

### 67) How do you rebuild services in Compose?
**Answer:** Use `docker compose up --build`.

### 68) What is the difference between image immutability and mutable containers?
**Answer:** Images should be treated as immutable build artifacts, while containers are disposable runtime instances created from them.

### 69) Why should containers be ephemeral?
**Answer:** Ephemeral containers improve reproducibility, simplify scaling, and reduce configuration drift.

### 70) What is container drift?
**Answer:** Container drift happens when runtime changes are made manually inside containers, causing them to differ from the source image.

### 71) Why is running as root inside a container risky?
**Answer:** It increases security risk because a container breakout or misconfiguration can have greater impact on the host or cluster.

### 72) How do you run a container as non-root?
**Answer:** Create a non-root user in the image and use the `USER` instruction.

### 73) What is a distroless image?
**Answer:** A distroless image contains only the application runtime and required libraries, reducing attack surface and size.

### 74) What are the trade-offs of distroless images?
**Answer:** They improve security and size but make debugging harder because common shell tools are absent.

### 75) How do you scan Docker images for vulnerabilities?
**Answer:** Use tools like Trivy, Grype, Docker Scout, or registry-native scanners.

## Security, Troubleshooting, and Production Practice

### 76) Why is image scanning important?
**Answer:** It helps detect vulnerable packages, outdated dependencies, and insecure base images before deployment.

### 77) What is image signing?
**Answer:** Image signing verifies image authenticity and integrity using tools like Cosign or Notary.

### 78) Why is image provenance important?
**Answer:** It helps ensure the image came from a trusted build pipeline and was not tampered with.

### 79) What is the difference between container runtime and orchestration?
**Answer:** The runtime executes containers on a host, while orchestration platforms like Kubernetes manage scheduling, scaling, networking, and lifecycle across many hosts.

### 80) What is Docker Swarm?
**Answer:** Docker Swarm is Docker’s native clustering and orchestration solution for managing services across multiple nodes.

### 81) Why is Kubernetes more common than Swarm now?
**Answer:** Kubernetes offers broader ecosystem support, richer orchestration features, and stronger adoption in enterprise environments.

### 82) How do you clean unused Docker resources?
**Answer:** Use `docker system prune`, `docker image prune`, `docker container prune`, and related commands carefully.

### 83) What is the risk of aggressive prune commands?
**Answer:** They can remove images, networks, or volumes still needed for rollback, debugging, or persistent data.

### 84) How do you debug DNS issues inside a container?
**Answer:** Check `/etc/resolv.conf`, test with `nslookup` or `dig`, inspect network settings, and verify upstream DNS reachability.

### 85) How do you debug connectivity between two containers?
**Answer:** Verify they are on the same network, inspect DNS resolution, test ports with `nc` or `curl`, and review firewall or service binding issues.

### 86) Why should one container usually run one main process?
**Answer:** It keeps lifecycle management simple, improves observability, and aligns with container design principles.

### 87) Can a container run multiple processes?
**Answer:** Yes, but it is usually discouraged unless there is a strong reason and proper supervision is in place.

### 88) What is PID 1 behaviour in containers?
**Answer:** PID 1 handles signals differently and may not reap child processes correctly unless the application or init wrapper is designed for it.

### 89) Why are signal handling and graceful shutdown important in containers?
**Answer:** They allow clean termination, proper connection draining, and safe shutdown during deployments or scaling events.

### 90) What is health checking in Docker?
**Answer:** A health check runs a command inside the container to determine whether the application is healthy.

### 91) How do health checks help operations?
**Answer:** They improve automation by allowing platforms to detect unhealthy containers and restart or replace them.

### 92) What is the difference between build-time and runtime dependencies?
**Answer:** Build-time dependencies are needed only to compile or package the app, while runtime dependencies are required when the container actually runs.

### 93) Why should build tools be excluded from runtime images?
**Answer:** It reduces image size, attack surface, and unnecessary complexity.

### 94) How do you optimise Docker builds in CI/CD?
**Answer:** Use layer caching, multi-stage builds, deterministic dependencies, smaller contexts, and parallel pipeline steps where possible.

### 95) What is a common mistake in Dockerfiles for Node or Python apps?
**Answer:** Copying the full source before dependency installation, which breaks cache reuse and slows builds.

### 96) How do you handle secrets in Docker-based deployments?
**Answer:** Inject them at runtime using secret managers, environment injection, or orchestrator-native secret mechanisms instead of baking them into images.

### 97) What is your approach to troubleshooting a crashing production container?
**Answer:** Check logs, exit codes, recent image changes, environment variables, resource limits, health checks, and dependency reachability before deciding whether to restart, roll back, or scale.

### 98) What is your approach to securing Docker in production?
**Answer:** Use minimal trusted images, run as non-root, scan and sign images, restrict capabilities, use read-only filesystems where possible, and avoid mounting the Docker socket unnecessarily.

### 99) What is your approach to Docker image versioning?
**Answer:** Use immutable version tags tied to build IDs or Git SHAs, avoid relying only on `latest`, and keep rollback-friendly tagging conventions.

## Production Interview Mindset

### 100) What is your practical senior-level approach in interviews?
**Answer:** Build small immutable images, secure them early, standardise Dockerfiles, enforce scanning and tagging in CI/CD, keep containers disposable, and integrate observability and rollback into deployment workflows.

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

> In senior Docker interviews, explain not only commands but also image design, security, runtime behaviour, troubleshooting, and how Docker fits into CI/CD and Kubernetes-based production systems.
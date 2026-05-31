from pathlib import Path
import re

ROOT = Path("/Users/ramiz/IBM-BOB/DevOps-Interview-Master-AI")

FILES = [
    "Git-Interview-Questions-and-Answers.md",
    "Docker-Interview-Questions-and-Answers.md",
    "Kubernetes-Interview-Questions-and-Answers.md",
    "Terraform-Interview-Questions-and-Answers.md",
    "AWS-Interview-Questions-and-Answers.md",
    "Azure-Interview-Questions-and-Answers.md",
    "Jenkins-Interview-Questions-and-Answers.md",
    "GitHub-Actions-Interview-Questions-and-Answers.md",
    "Ansible-Interview-Questions-and-Answers.md",
    "Prometheus-Interview-Questions-and-Answers.md",
    "Grafana-Interview-Questions-and-Answers.md",
    "ELK-Interview-Questions-and-Answers.md",
    "ArgoCD-Interview-Questions-and-Answers.md",
    "Helm-Interview-Questions-and-Answers.md",
    "Security-Interview-Questions-and-Answers.md",
]

SECTION_MAP = {
    "Git": [
        "Git Fundamentals and Workflow",
        "Branching, Merging, and History",
        "Collaboration, Recovery, and Governance",
        "Troubleshooting and Production Practice",
    ],
    "Docker": [
        "Docker Foundations",
        "Images, Containers, and Builds",
        "Networking, Storage, and Runtime",
        "Security, Troubleshooting, and Production Practice",
    ],
    "Kubernetes": [
        "Kubernetes Foundations",
        "Core Objects and Workload Management",
        "Networking, Storage, and Security",
        "Troubleshooting, Scaling, and Production Practice",
    ],
    "Terraform": [
        "Terraform Foundations",
        "State, Modules, and Workflow",
        "Security, Governance, and Collaboration",
        "Troubleshooting, Drift, and Production Practice",
    ],
    "AWS": [
        "AWS Foundations",
        "Compute, Networking, and Storage",
        "Identity, Security, and Operations",
        "Reliability, Cost, and Production Practice",
    ],
    "Azure": [
        "Azure Foundations",
        "Compute, Networking, and Storage",
        "Identity, Security, and Operations",
        "Reliability, Governance, and Production Practice",
    ],
    "Jenkins": [
        "Jenkins Foundations",
        "Pipelines, Agents, and Workflow",
        "Security, Scaling, and Governance",
        "Troubleshooting and Production Practice",
    ],
    "GitHub Actions": [
        "GitHub Actions Foundations",
        "Workflows, Runners, and Automation",
        "Security, Reuse, and Governance",
        "Troubleshooting and Production Practice",
    ],
    "Ansible": [
        "Ansible Foundations",
        "Playbooks, Roles, and Automation",
        "Variables, Security, and Best Practices",
        "Troubleshooting and Production Practice",
    ],
    "Prometheus": [
        "Prometheus Foundations",
        "Metrics, PromQL, and Alerting",
        "Scaling, Cardinality, and Operations",
        "Troubleshooting and Production Practice",
    ],
    "Grafana": [
        "Grafana Foundations",
        "Dashboards, Queries, and Visualisation",
        "Alerting, Governance, and Security",
        "Troubleshooting and Production Practice",
    ],
    "ELK": [
        "ELK Foundations",
        "Elasticsearch, Logstash, and Kibana",
        "Scaling, Retention, and Security",
        "Troubleshooting and Production Practice",
    ],
    "ArgoCD": [
        "ArgoCD Foundations",
        "Applications, Sync, and GitOps Workflow",
        "Security, Multi-Cluster, and Governance",
        "Troubleshooting and Production Practice",
    ],
    "Helm": [
        "Helm Foundations",
        "Charts, Values, and Releases",
        "Hooks, Security, and Best Practices",
        "Troubleshooting and Production Practice",
    ],
    "Security": [
        "Security Foundations",
        "Identity, Secrets, and Protection Controls",
        "Cloud, CI/CD, and Governance",
        "Incident Response and Production Practice",
    ],
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def normalise_text(value: str) -> str:
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def clean_inline(value: str) -> str:
    value = normalise_text(value)
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"^>+\s*", "", value)
    return value.strip()


def extract_qas(text: str) -> list[tuple[int, str, str]]:
    lines = normalise_text(text).split("\n")
    qas: list[tuple[int, str, str]] = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        match = re.match(r"^###\s+(\d+)\)\s+(.*)$", line)
        if not match:
            i += 1
            continue

        number = int(match.group(1))
        question = clean_inline(match.group(2))
        i += 1

        while i < len(lines) and not lines[i].strip():
            i += 1

        if i >= len(lines) or not lines[i].lstrip().startswith("**Answer:**"):
            raise ValueError(f"Question {number} is missing an answer block")

        answer_lines = [lines[i].split("**Answer:**", 1)[1].strip()]
        i += 1

        while i < len(lines):
            stripped = lines[i].strip()
            if re.match(r"^###\s+\d+\)\s+", stripped):
                break
            if stripped.startswith("## "):
                break
            answer_lines.append(lines[i])
            i += 1

        answer = clean_inline("\n".join(answer_lines))
        qas.append((number, question, answer))

    return qas


def extract_final_tip(text: str, topic: str) -> str:
    match = re.search(r"## Final Interview (?:Tip|Advice)\s*(.*)$", text, re.S)
    if match:
        return clean_inline(match.group(1))
    return (
        f"For senior {topic} interviews, explain not only definitions but also how you would "
        f"implement, troubleshoot, secure, and improve the topic in production."
    )


def build_document(title: str, topic: str, qas: list[tuple[int, str, str]], final_tip: str) -> str:
    sections = SECTION_MAP[topic]
    groups = [qas[0:25], qas[25:50], qas[50:75], qas[75:99]]
    q100_answer = qas[99][2]

    out = [
        title,
        "",
        "> **Senior DevOps Interview Pack**",
        ">",
        f"> **Domain:** {topic} concepts, implementation, troubleshooting, security, and operations  ",
        "> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  ",
        "> **Format:** 100 real-interview-style questions with concise, practical answers  ",
        "> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        f"This guide is designed for senior-level {topic} interviews where interviewers expect more than definitions. You should be able to explain fundamentals, connect them to production impact, troubleshoot issues methodically, and justify safe operational decisions.",
        "",
        "### What this pack helps you demonstrate",
        f"- Strong {topic} fundamentals",
        "- Production troubleshooting mindset",
        "- Operational decision-making under pressure",
        "- Security and reliability awareness",
        "- Clear, structured interview communication",
        "",
        "---",
        "",
        "## Navigation",
        "",
        "| Section | Focus Area |",
        "|---|---|",
        "| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |",
        "| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |",
    ]

    for section in sections:
        out.append(f"| [{section}](#{slugify(section)}) | Core interview coverage for this area |")

    out.extend(
        [
            "| [Production Interview Mindset](#production-interview-mindset) | Senior-level incident and decision approach |",
            "| [Rapid Revision Sheet](#rapid-revision-sheet) | Last-minute interview refresh |",
            "| [Final Interview Advice](#final-interview-advice) | What interviewers remember most |",
            "",
            "---",
            "",
            "## How to Use This Guide",
            "",
            "### Recommended preparation flow",
            "1. Read **10 to 15 questions per day**",
            "2. Answer each question once **without looking**",
            "3. Re-answer using a **production example**",
            "4. Revise weak areas using the **Rapid Revision Sheet**",
            "",
            "### What senior interviewers usually expect",
            "- Correct fundamentals",
            "- Clear explanation, not just keywords",
            "- Real production context",
            "- Safe troubleshooting sequence",
            "- Awareness of impact, risk, and rollback",
            "",
            "## Interview Answer Framework",
            "",
            "Use this structure for most interview answers:",
            "",
            "| Step | What to say |",
            "|---|---|",
            "| 1. Define | Explain what the concept is |",
            "| 2. Importance | Explain why it matters in production |",
            "| 3. Practical example | Give a real or realistic scenario |",
            "| 4. Troubleshooting angle | Mention commands, logs, metrics, or validation steps |",
            "| 5. Safe action | Explain how you would mitigate without causing more impact |",
            "",
            "### Example senior-style answer",
            "> “I first explain the concept clearly, then connect it to production impact, and finally describe how I would validate, troubleshoot, secure, or improve it in a real environment.”",
            "",
        ]
    )

    for section, items in zip(sections, groups):
        out.append(f"## {section}")
        out.append("")
        for number, question, answer in items:
            out.append(f"### {number}) {question}")
            out.append(f"**Answer:** {answer}")
            out.append("")

    out.extend(
        [
            "## Production Interview Mindset",
            "",
            "### 100) What is your practical senior-level approach in interviews?",
            f"**Answer:** {q100_answer}",
            "",
            "### Senior interview checklist",
            "- Confirm the business or operational context",
            "- Explain trade-offs, not only definitions",
            "- Mention validation and troubleshooting steps",
            "- Prefer safe, reversible actions first",
            "- Show reliability, security, and maintainability thinking",
            "",
            "## Rapid Revision Sheet",
            "",
            "### Last-minute revision reminders",
            "- Explain concepts in context, not in isolation",
            "- Mention logs, metrics, and validation together",
            "- Show safe mitigation thinking",
            "- Highlight trade-offs where relevant",
            "- Speak like an operator, not only like an exam candidate",
            "",
            "### Best answer pattern to remember",
            "1. **Define the concept**",
            "2. **Explain why it matters**",
            "3. **Give a production example**",
            "4. **Mention one troubleshooting or implementation approach**",
            "",
            "## Final Interview Advice",
            "",
            f"> {final_tip}",
            "",
        ]
    )

    return "\n".join(out)


restyled = 0

for filename in FILES:
    path = ROOT / filename
    text = path.read_text()
    title = text.splitlines()[0].strip()
    topic = title.replace("# ", "").replace(" Interview Questions and Answers", "").strip()
    qas = extract_qas(text)

    if len(qas) != 100:
        raise ValueError(f"{filename}: expected 100 QAs, found {len(qas)}")

    expected_numbers = list(range(1, 101))
    actual_numbers = [number for number, _, _ in qas]
    if actual_numbers != expected_numbers:
        raise ValueError(f"{filename}: question numbering is not sequential from 1 to 100")

    final_tip = extract_final_tip(text, topic)
    path.write_text(build_document(title, topic, qas, final_tip))
    restyled += 1

print(f"Restyled {restyled} files successfully")
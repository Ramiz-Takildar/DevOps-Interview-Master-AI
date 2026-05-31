# Git Interview Questions and Answers

> **Senior DevOps Interview Pack**
>
> **Domain:** Git concepts, collaboration workflows, recovery, governance, and operations  
> **Level:** Senior / Lead DevOps / SRE / Platform Engineering  
> **Format:** 100 real-interview-style questions with concise, practical answers  
> **Best for:** interview preparation, mock interviews, rapid revision, and PDF export

---

## Executive Summary

This guide is designed for senior-level Git interviews where interviewers expect more than command recall. You should be able to explain collaboration strategy, history management, rollback safety, repository governance, and how Git supports reliable delivery workflows.

### What this pack helps you demonstrate
- Strong Git fundamentals
- Safe collaboration and branching judgement
- Recovery and rollback awareness
- Governance and CI/CD integration thinking
- Clear, structured interview communication

---

## Navigation

| Section | Focus Area |
|---|---|
| [How to Use This Guide](#how-to-use-this-guide) | Best way to prepare with this file |
| [Interview Answer Framework](#interview-answer-framework) | How to answer like a senior engineer |
| [Git Fundamentals and Workflow](#git-fundamentals-and-workflow) | Core Git concepts and daily usage |
| [Branching, Merging, and History](#branching-merging-and-history) | Branch strategy, merge models, and history control |
| [Collaboration, Recovery, and Governance](#collaboration-recovery-and-governance) | Team workflows, rollback, and repository controls |
| [Troubleshooting and Production Practice](#troubleshooting-and-production-practice) | Real-world Git operations in delivery pipelines |
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
- Safe rollback and recovery thinking
- Awareness of collaboration risk and governance

## Interview Answer Framework

Use this structure for most interview answers:

| Step | What to say |
|---|---|
| 1. Define | Explain what the Git concept or command does |
| 2. Importance | Explain why it matters in team delivery |
| 3. Practical example | Give a realistic workflow or incident example |
| 4. Troubleshooting angle | Mention how you inspect, recover, or validate safely |
| 5. Safe action | Explain how you avoid damaging shared history |

### Example senior-style answer
> “I first explain the Git concept clearly, then connect it to collaboration safety and delivery impact, and finally describe how I would validate, recover, or roll back changes in a shared repository.”

## Git Fundamentals and Workflow

### 1) What is Git?
**Answer:** Git is a distributed version control system that tracks source code changes, supports branching and merging, and enables collaboration with full local history.

### 2) What is the difference between Git and GitHub?
**Answer:** Git is the version control tool, while GitHub is a hosting and collaboration platform built around Git repositories.

### 3) What is a repository?
**Answer:** A repository is the project storage area containing tracked files, commit history, branches, and metadata.

### 4) What is a commit?
**Answer:** A commit is a snapshot of tracked changes with metadata such as author, timestamp, and message.

### 5) What is a branch?
**Answer:** A branch is a movable pointer to a sequence of commits, allowing isolated development work.

### 6) What is HEAD in Git?
**Answer:** HEAD points to the currently checked-out commit or branch reference.

### 7) What is the staging area?
**Answer:** The staging area, or index, is where changes are prepared before creating a commit.

### 8) What is the difference between working tree, staging area, and repository?
**Answer:** The working tree contains current file changes, the staging area holds selected changes for the next commit, and the repository stores committed history.

### 9) How do you initialise a Git repository?
**Answer:** Use `git init` to create a new local repository.

### 10) How do you clone a repository?
**Answer:** Use `git clone <repo-url>` to copy the repository and its history locally.

### 11) How do you check repository status?
**Answer:** Use `git status` to see modified, staged, and untracked files.

### 12) How do you view commit history?
**Answer:** Use `git log`, optionally with `--oneline`, `--graph`, or `--decorate`.

### 13) How do you stage a file?
**Answer:** Use `git add <file>`.

### 14) How do you stage all changes?
**Answer:** Use `git add .` or `git add -A`, depending on the scope you want.

### 15) How do you create a commit?
**Answer:** Use `git commit -m "message"` after staging the required changes.

### 16) What makes a good commit message?
**Answer:** A good commit message is clear, concise, and explains what changed and why, not just vague text like “fix stuff”.

### 17) What is the difference between `git add .` and `git add -A`?
**Answer:** `git add .` stages changes under the current directory, while `git add -A` stages all changes including deletions across the repository.

### 18) How do you unstage a file?
**Answer:** Use `git restore --staged <file>`.

### 19) How do you discard local changes in a file?
**Answer:** Use `git restore <file>` if you want to revert uncommitted changes.

### 20) How do you rename a branch?
**Answer:** Use `git branch -m old-name new-name` or `git branch -m new-name` for the current branch.

### 21) How do you create and switch to a new branch?
**Answer:** Use `git switch -c <branch-name>` or `git checkout -b <branch-name>`.

### 22) What is the difference between `git switch` and `git checkout`?
**Answer:** `git switch` is focused on branch operations, while `git checkout` is older and also handles file restoration and detached HEAD operations.

### 23) How do you merge a branch?
**Answer:** Switch to the target branch and run `git merge <source-branch>`.

### 24) What is a merge conflict?
**Answer:** A merge conflict happens when Git cannot automatically reconcile overlapping changes between branches.

### 25) How do you resolve a merge conflict?
**Answer:** Edit the conflicted files, remove conflict markers, test the result, stage the files, and complete the merge commit.

## Branching, Merging, and History

### 26) What is rebase?
**Answer:** Rebase reapplies commits from one branch onto another base to create a cleaner linear history.

### 27) What is the difference between merge and rebase?
**Answer:** Merge preserves branch history with a merge commit, while rebase rewrites commit history to make it linear.

### 28) When should you avoid rebase?
**Answer:** Avoid rebasing shared public branches because it rewrites history and can disrupt collaborators.

### 29) What is fast-forward merge?
**Answer:** A fast-forward merge happens when the target branch has no divergent commits and Git can simply move the branch pointer forward.

### 30) What is squash merge?
**Answer:** A squash merge combines multiple commits into one before merging, keeping history cleaner.

### 31) What is cherry-pick?
**Answer:** `git cherry-pick` applies a specific commit from one branch onto another.

### 32) When is cherry-pick useful?
**Answer:** It is useful for hotfixes, selective backports, or moving one specific change without merging the full branch.

### 33) What is `git fetch`?
**Answer:** `git fetch` downloads remote changes without merging them into the current branch.

### 34) What is `git pull`?
**Answer:** `git pull` is effectively `git fetch` followed by merge or rebase, depending on configuration.

### 35) What is `git push`?
**Answer:** `git push` uploads local commits to a remote repository.

### 36) What is the difference between fetch and pull?
**Answer:** Fetch only downloads updates, while pull downloads and integrates them into the current branch.

### 37) What is origin?
**Answer:** `origin` is the default name for the remote repository from which the project was cloned.

### 38) How do you list remotes?
**Answer:** Use `git remote -v`.

### 39) How do you add a remote?
**Answer:** Use `git remote add <name> <url>`.

### 40) How do you remove a remote?
**Answer:** Use `git remote remove <name>`.

### 41) What is a tag?
**Answer:** A tag is a named reference to a specific commit, commonly used for releases.

### 42) What is the difference between lightweight and annotated tags?
**Answer:** Lightweight tags are simple pointers, while annotated tags include metadata such as author, date, and message.

### 43) How do you create a tag?
**Answer:** Use `git tag v1.0.0` or `git tag -a v1.0.0 -m "release"`.

### 44) How do you push tags?
**Answer:** Use `git push origin <tag>` or `git push --tags`.

### 45) What is detached HEAD?
**Answer:** Detached HEAD means you are checked out to a commit directly instead of a branch.

### 46) Why is detached HEAD risky?
**Answer:** Commits made there can become hard to find unless you create a branch before moving away.

### 47) What is `git stash`?
**Answer:** `git stash` temporarily saves uncommitted changes so you can switch context cleanly.

### 48) How do you list stashes?
**Answer:** Use `git stash list`.

### 49) How do you apply a stash?
**Answer:** Use `git stash apply` or `git stash pop` if you want to apply and remove it.

### 50) What is the difference between stash apply and stash pop?
**Answer:** `apply` keeps the stash entry, while `pop` applies it and removes it from the stash list.

## Collaboration, Recovery, and Governance

### 51) How do you delete a stash?
**Answer:** Use `git stash drop` or `git stash clear`.

### 52) What is `git diff`?
**Answer:** `git diff` shows changes between working tree, staging area, commits, or branches.

### 53) How do you compare two branches?
**Answer:** Use `git diff branch1..branch2` or `git log branch1..branch2`.

### 54) How do you see who changed a line last?
**Answer:** Use `git blame <file>`.

### 55) What is `git reflog`?
**Answer:** `git reflog` records movements of HEAD and branch references, helping recover lost commits.

### 56) How do you recover a deleted branch?
**Answer:** Use `git reflog` to find the commit and recreate the branch with `git branch <name> <commit>`.

### 57) What is `git reset`?
**Answer:** `git reset` moves the current branch pointer and can also affect the staging area and working tree depending on mode.

### 58) What is the difference between soft, mixed, and hard reset?
**Answer:** Soft keeps changes staged, mixed keeps changes unstaged, and hard discards changes from both staging and working tree.

### 59) When is `git reset --hard` dangerous?
**Answer:** It permanently discards uncommitted changes and can cause data loss if used carelessly.

### 60) What is `git revert`?
**Answer:** `git revert` creates a new commit that undoes the changes introduced by an earlier commit.

### 61) When should you use revert instead of reset?
**Answer:** Use revert on shared branches because it preserves history safely.

### 62) How do you amend the last commit?
**Answer:** Use `git commit --amend`.

### 63) When is amend useful?
**Answer:** It is useful for fixing the last commit message or adding forgotten staged changes before pushing.

### 64) What is `.gitignore`?
**Answer:** `.gitignore` defines files and patterns Git should not track, such as logs, build outputs, and secrets.

### 65) Can `.gitignore` remove already tracked files?
**Answer:** No. If a file is already tracked, you must untrack it with `git rm --cached`.

### 66) How do you stop tracking a file but keep it locally?
**Answer:** Use `git rm --cached <file>`.

### 67) What is a bare repository?
**Answer:** A bare repository contains only Git metadata and no working tree, commonly used as a central remote.

### 68) What is the difference between local and remote branches?
**Answer:** Local branches exist in your repository, while remote-tracking branches reflect the state of branches on remotes.

### 69) How do you list branches?
**Answer:** Use `git branch` for local branches and `git branch -a` for all branches.

### 70) How do you delete a local branch?
**Answer:** Use `git branch -d <branch>` or `-D` to force deletion.

### 71) How do you delete a remote branch?
**Answer:** Use `git push origin --delete <branch>`.

### 72) What is branch protection?
**Answer:** Branch protection enforces rules such as pull requests, reviews, status checks, and restricted pushes on important branches.

### 73) Why is branch protection important in DevOps?
**Answer:** It reduces risky direct changes to production branches and enforces quality gates in CI/CD workflows.

### 74) What is trunk-based development?
**Answer:** It is a workflow where developers integrate frequently into a main branch using short-lived branches and strong automation.

### 75) What is GitFlow?
**Answer:** GitFlow is a branching model with dedicated feature, release, and hotfix branches, often used in structured release environments.

## Troubleshooting and Production Practice

### 76) Which branching strategy do you prefer?
**Answer:** Usually trunk-based development for faster delivery, but the right choice depends on release cadence, compliance, and team maturity.

### 77) What is a pull request?
**Answer:** A pull request is a review and merge workflow where proposed changes are discussed, validated, and approved before integration.

### 78) What should you review in a pull request?
**Answer:** Check correctness, readability, security, tests, rollback impact, deployment risk, and whether the change matches the intended scope.

### 79) How do you handle a bad commit pushed to main?
**Answer:** Prefer `git revert` on shared branches, validate CI, and communicate clearly before redeploying or rolling back.

### 80) What is force push?
**Answer:** Force push overwrites remote branch history with local history using `git push --force` or safer `--force-with-lease`.

### 81) Why is `--force-with-lease` safer?
**Answer:** It prevents overwriting remote changes you do not have locally by checking the remote state first.

### 82) What is submodule in Git?
**Answer:** A submodule is a repository embedded inside another repository at a specific commit reference.

### 83) What are the challenges with submodules?
**Answer:** They add complexity in cloning, updating, version alignment, and CI/CD workflows.

### 84) What is Git LFS?
**Answer:** Git Large File Storage stores large binary files outside normal Git history while keeping lightweight pointers in the repository.

### 85) Why should secrets never be committed to Git?
**Answer:** Because Git history is persistent and secrets can remain exposed even after deletion unless history is rewritten and credentials rotated.

### 86) How do you remove a secret accidentally committed?
**Answer:** Rotate the secret immediately, then clean history using tools like `git filter-repo` or BFG, and force-push carefully if required.

### 87) What is signed commit or signed tag?
**Answer:** It uses GPG or SSH signing to verify authorship and integrity of commits or tags.

### 88) Why are signed tags useful for releases?
**Answer:** They help verify that a release was created by a trusted source and was not tampered with.

### 89) How do you inspect one specific commit?
**Answer:** Use `git show <commit>`.

### 90) How do you search commit history by message?
**Answer:** Use `git log --grep="text"`.

### 91) How do you search history for code changes?
**Answer:** Use `git log -S "string"` or `git log -G "pattern"`.

### 92) What is bisect in Git?
**Answer:** `git bisect` performs a binary search through commits to identify which commit introduced a bug.

### 93) When is `git bisect` useful?
**Answer:** It is useful when a regression exists but the exact breaking commit is unknown.

### 94) How do you keep commit history clean?
**Answer:** Use meaningful commits, squash noisy work, avoid unrelated changes in one commit, and enforce review standards.

### 95) What is the difference between author and committer?
**Answer:** The author created the original change, while the committer is the person who actually committed or applied it.

### 96) How do you configure Git username and email?
**Answer:** Use `git config --global user.name "Name"` and `git config --global user.email "email@example.com"`.

### 97) What is the difference between global and local Git config?
**Answer:** Global config applies to the user account, while local config applies only to the current repository.

### 98) How do you troubleshoot “non-fast-forward” push errors?
**Answer:** Fetch the latest remote changes, inspect divergence, then merge or rebase before pushing again.

### 99) How do you handle long-lived branches in DevOps teams?
**Answer:** I try to avoid them where possible, because they increase drift, merge conflicts, and release risk. Short-lived branches with frequent integration are safer.

## Production Interview Mindset

### 100) What is your practical senior-level approach in interviews?
**Answer:** Protect main branches, require pull requests and CI checks, keep branches short-lived, use revert for shared rollback, avoid force pushes on protected branches, and treat Git history as an operational asset.

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

> In senior Git interviews, explain not only commands but also collaboration safety, rollback strategy, branch governance, and how Git supports reliable CI/CD.
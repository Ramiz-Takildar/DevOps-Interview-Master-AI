# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Directory Overview

This is a **DevOps Interview Preparation Repository** containing comprehensive interview question-and-answer guides for senior-level DevOps, SRE, and Platform Engineering roles. The repository is structured as a collection of standardized markdown documents covering essential DevOps technologies and practices.

### Purpose
- Provide production-focused interview preparation materials
- Cover 100 questions per technology domain
- Target senior/lead-level technical interviews
- Enable rapid revision and PDF export for interview candidates

## Repository Structure

### Interview Question Files
The repository contains 15 topic-specific interview guides:

**Core DevOps Tools:**
- `Git-Interview-Questions-and-Answers.md`
- `Docker-Interview-Questions-and-Answers.md`
- `Kubernetes-Interview-Questions-and-Answers.md`
- `Jenkins-Interview-Questions-and-Answers.md`
- `GitHub-Actions-Interview-Questions-and-Answers.md`

**Infrastructure & Cloud:**
- `Terraform-Interview-Questions-and-Answers.md`
- `AWS-Interview-Questions-and-Answers.md`
- `Azure-Interview-Questions-and-Answers.md`
- `Ansible-Interview-Questions-and-Answers.md`

**Observability:**
- `Prometheus-Interview-Questions-and-Answers.md`
- `Grafana-Interview-Questions-and-Answers.md`
- `ELK-Interview-Questions-and-Answers.md`

**Advanced Topics:**
- `ArgoCD-Interview-Questions-and-Answers.md`
- `Helm-Interview-Questions-and-Answers.md`
- `Security-Interview-Questions-and-Answers.md`

**Cross-Domain:**
- `Linux-Interview-Questions-and-Answers.md`
- `Senior-DevOps-Interview-Questions-and-Answers.md`

### Automation Script
- `restyle_interview_files.py` - Python script that enforces consistent formatting across all interview files

## Content Structure

### Standard Interview File Format
Each interview guide follows this consistent structure:

1. **Header Section**
   - Title with technology name
   - Senior DevOps Interview Pack metadata box
   - Domain, level, format, and best-use description

2. **Executive Summary**
   - Purpose and target audience
   - Key demonstration areas

3. **Navigation Table**
   - Links to all major sections
   - Quick access to specific topics

4. **Usage Guide**
   - Recommended preparation flow
   - Interview expectations

5. **Interview Answer Framework**
   - 5-step answer structure (Define, Importance, Example, Troubleshooting, Safe Action)
   - Senior-style answer examples

6. **Four Main Question Sections** (25 questions each)
   - Section 1: Foundations (Questions 1-25)
   - Section 2: Core Concepts (Questions 26-50)
   - Section 3: Advanced Topics (Questions 51-75)
   - Section 4: Production Practice (Questions 76-99)

7. **Production Interview Mindset**
   - Question 100: Practical senior-level approach
   - Senior interview checklist

8. **Rapid Revision Sheet**
   - Last-minute reminders
   - Best answer patterns

9. **Final Interview Advice**
   - Topic-specific closing guidance

### Question Format
Each question follows this pattern:
```markdown
### <number>) <question text>
**Answer:** <concise, production-focused answer>
```

## Working with This Repository

### Adding New Questions
When adding questions to existing files:
1. Maintain the numbering sequence (1-100)
2. Place questions in the appropriate section based on complexity
3. Write answers that are concise, practical, and production-focused
4. Include troubleshooting steps, commands, or validation approaches
5. Run `restyle_interview_files.py` to ensure formatting consistency

### Creating New Interview Files
To add a new technology domain:
1. Create a new markdown file: `<Technology>-Interview-Questions-and-Answers.md`
2. Add the filename to the `FILES` list in `restyle_interview_files.py`
3. Define four section names in the `SECTION_MAP` dictionary
4. Write 100 questions following the standard format
5. Run the restyle script to apply consistent formatting

### Using the Restyle Script
The `restyle_interview_files.py` script:
- Validates that each file has exactly 100 questions
- Ensures sequential numbering (1-100)
- Applies consistent section structure
- Generates navigation tables
- Adds standard header and footer content
- Normalizes text formatting

**To run:**
```bash
python restyle_interview_files.py
```

**Requirements:**
- Python 3.x
- Standard library only (no external dependencies)

### Content Guidelines

**Answer Quality Standards:**
- Focus on production scenarios, not just definitions
- Include troubleshooting commands and validation steps
- Mention security, reliability, and operational considerations
- Explain trade-offs and decision-making rationale
- Use clear, technical language appropriate for senior roles

**Avoid:**
- Generic textbook definitions without context
- Overly verbose explanations
- Theoretical concepts without practical application
- Answers that don't address "why" and "how" in production

## Key Conventions

### Section Organization
Each technology follows a progression:
1. **Foundations** - Core concepts and architecture
2. **Implementation** - Practical usage and configuration
3. **Advanced Topics** - Security, scaling, networking, storage
4. **Production Practice** - Troubleshooting, operations, best practices

### Answer Philosophy
Answers are designed to demonstrate:
- Strong fundamentals
- Production troubleshooting mindset
- Operational decision-making
- Security and reliability awareness
- Clear, structured communication

### Target Audience
- Senior DevOps Engineers
- Lead SRE Engineers
- Platform Engineers
- Cloud Engineers
- Technical Architects

## Maintenance Notes

### File Consistency
All interview files must:
- Have exactly 100 questions
- Follow sequential numbering
- Use the standard section structure
- Include the metadata header box
- Provide navigation tables
- End with revision and advice sections

### Quality Assurance
Before committing changes:
1. Run `restyle_interview_files.py` to validate and format
2. Verify all internal links work correctly
3. Check that answers are concise and production-focused
4. Ensure technical accuracy of commands and concepts
5. Confirm markdown renders correctly for PDF export

## Usage Scenarios for AI Agents

### When asked to add questions:
1. Identify the appropriate file and section
2. Maintain numbering and formatting consistency
3. Write production-focused answers
4. Run restyle script after changes

### When asked to create new content:
1. Follow the established structure and conventions
2. Update the restyle script configuration
3. Ensure 100 questions per file
4. Apply the standard answer framework

### When asked to improve existing content:
1. Preserve the question numbering
2. Enhance answers with production context
3. Add troubleshooting steps where missing
4. Maintain concise, technical tone

### When asked about the repository:
1. Explain it's an interview preparation resource
2. Describe the standardized structure
3. Reference the restyle script for automation
4. Highlight the senior-level focus

## Technical Details

### File Encoding
- UTF-8 encoding for all markdown files
- Unix-style line endings (LF)

### Markdown Features Used
- Headers (H1-H3)
- Blockquotes for metadata boxes
- Tables for navigation and frameworks
- Bold text for emphasis
- Code blocks for commands
- Internal anchor links

### Python Script Details
The restyle script uses:
- `pathlib` for file operations
- Regular expressions for parsing
- String manipulation for formatting
- No external dependencies required

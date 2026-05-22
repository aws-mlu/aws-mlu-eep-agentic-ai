# Agentic AI — Educator Enablement Program (EEP)

Modular curriculum content designed to teach the fundamentals and applications of Agentic AI, from core concepts to hands-on building with AI agents. Created by the Machine Learning University (MLU) team, this repository provides content needed to learn or teach a complete Agentic AI course.

## ⚠️ Disclaimer

This repository is educational material provided as-is for learning and teaching purposes. Labs and example code should not be deployed to production environments or used to process sensitive data without independent review. Any credentials, API keys, or personal data in this repository are synthetic and exist solely for educational demonstration. When running labs, we recommend any IAM credentials scoped to the minimum permissions required as needed - avoid using broad or administrative access. Additionally, we recommend always pulling the latest version to ensure you have the most current content and fixes.

## Who Is This For?

- **Students and self-learners** looking to understand and build with Agentic AI
- **Faculty members** at institutions adopting this curriculum — each module includes faculty support materials (design docs and embark guides) to help you prepare and deliver the content

## Curriculum Content Overview

The program is organized into five progressive modules:

| Module | Topic | Description |
|--------|-------|-------------|
| 1 | **Agentic AI Essentials** | Core concepts and foundations of Agentic AI |
| 2 | **Agentic AI Applications** | Building practical AI agent applications using tools like Strands Agents SDK, Amazon Bedrock, and guardrails |
| 3 | **Multi-agent Collaboration** | Designing systems where multiple AI agents work together (To be delived Q3 2026) |
| 4 | **Agentic RAG** | Retrieval-Augmented Generation in agentic architectures (To be delived Q3 2026) |
| 5 | **Building with Agentic AI** | End-to-end project building with agentic AI tools and workflows (To be delived Q4 2026) |

## Repository Structure

Each module follows a consistent layout:

```
Module N - <Topic>/
├── Lesson/              # Slide decks (.pptx) for lectures
├── Labs/
│   ├── code-free/       # No-code labs using Amazon Quick
│   └── code-based/      # Coding labs
│       ├── SageMaker/   # Jupyter notebooks for Amazon SageMaker
│       └── Kiro/        # Spec-driven labs using Kiro IDE
└── Faculty Support/     # Design docs and embark guides for instructors
```

## Lab Environments

Labs are offered in multiple formats to accommodate different skill levels and environments:

### Code-Free Labs
Step-by-step guides using Amazon Quick — no programming required. Each includes a setup guide and hands-on walkthrough with example outputs.

### Code-Based Labs (SageMaker)
Jupyter notebooks designed to run on Amazon SageMaker. Module 2, for example, includes:
- Comparing agent vs. non-agent approaches
- Building agents with the Strands Agents SDK
- Implementing guardrails for AI agents

### Code-Based Labs (Kiro)
Spec-driven development labs using Kiro IDE. These labs walk through building a full application (e.g., a Study Plan Assistant) using structured requirements, design documents, and implementation task lists.

## Getting Started

### For Students / Self-Learners

1. Start with **Module 1** to build foundational understanding
2. Progress sequentially — each module builds on the previous one
3. Choose the lab format that fits your experience:
   - New to coding? Start with the **code-free** labs
   - Comfortable with Python? Use the **SageMaker** notebooks
   - Want to try spec-driven development? Use the **Kiro** labs
4. For SageMaker labs, install dependencies from the `requirements.txt` file included in the lab folder

### For Faculty Members

Each module includes a `Faculty Support/` folder containing:
- **Design Document** — learning objectives, module structure, and pedagogical approach
- **Embark Guide** — step-by-step facilitation guide for delivering the module

The repository contains a `Lab Support/` folder containing the setup guide for both Amazon Quick and Kiro lab environments. 

We recommend reviewing these materials before the first session. The labs include example outputs you can use as reference when guiding students.

## Prerequisites

- An AWS account with access to Amazon Bedrock (for code-based labs)
- For SageMaker labs: a SageMaker notebook instance or SageMaker Studio
- For Kiro labs: [Kiro IDE](https://kiro.dev) installed
- For code-free labs: access to Amazon Quickuick
- Basic familiarity with AI/ML concepts is helpful but not required for Module 1

**Note**: The Jupyter notebooks will run anywhere you have Jupyter correctly configured, however the notebooks in this repo are tested to run on Amazon SageMaker using the `Python 3 (ipykernel)` kernel and `SageMaker Studio Image Distribution 3.9.0`.

## Key Technologies

- [Amazon Bedrock](https://aws.amazon.com/bedrock/) — foundation models and AI agents
- [Strands Agents SDK](https://github.com/strands-agents/sdk-python) — open-source SDK for building AI agents
- [Amazon SageMaker](https://aws.amazon.com/sagemaker/) — ML development environment
- [Kiro](https://kiro.dev) — AI-powered IDE with spec-driven development
- [Amazon Quick](https://quick.amazon.com/) — generative AI assistant

## Getting Started
Clone this repository:
git clone [repository-url]
### Running the labs
The cloned repository contains all lab folders with the respective setup istructions, as well as hands-on instructions to run the labs.

#### Environment Requirements:

##### For code-based Jupyter labs
✅ Python 3.12+
✅ Jupyter Notebook environment
✅ AWS CLI configured with appropriate credentials
✅ Amazon Bedrock access
✅ Required Python packages (specified within the notebooks)

__Note:__ Jupyter notebooks will run anywhere you have Jupyter correctly configured, however the notebooks in this repo are designed to run on Amazon SageMaker using the conda_python3 kernel.

##### For code-based Kiro labs
✅ An Amazon Quick account
✅ A web browser (Chrome, Edge, or Firefox)


##### For code-free Amazon Quick labs
✅ Kiro IDE installed in your local notebook. 
✅ AWS credentials with Amazon Bedrock access. 

__Note:__ If you are running this lab as part of the EEP MLU course hands-on, your faculty may provide the proper credentials and setup for running this lab.

## Start Learning:
Begin with the presentation materials in the Lessons folder
Follow along with the corresponding lab notebooks
Each notebook is self-contained with all necessary instructions and explanations


## License

This project is licensed under the terms included in this repository. See the [LICENSE](LICENSE) file for details.

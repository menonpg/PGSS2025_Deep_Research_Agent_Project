# PGSS 2025 CS Lab Meeting Notes

**Date:** June 26, 2025  
**Instructor:** Professor Prahlad Menon, PhD, PMP
**Meeting Type:** Recorded Zoom Session ([Fathom Recording Link](https://fathom.video/calls/337772343))  
**Total Participants:** 9 students
**Location** DH2315

## Meeting Overview

This was the first setup meeting for the PGSS 2025 Computer Science Lab focused on building a **Deep Research Agent** - a smart scientific literature analysis system.

## Key Resources Shared

### Essential Links

- **CS Lab Canvas** - [Course page access](https://canvas.cmu.edu/courses/47814/pages/p8-computer-science-building-smart-scientific-literature-analysis-systems)
- **Zoom Link** - Meeting access
- **PGSS 2025 Google Drive** - [Shared repository for code, videos, and project artifacts](https://drive.google.com/drive/folders/1D2NvPsFWrqODGf4pj7OEbA_EhIXvH53g?usp=sharing)
- **Google Drive with Python / R Resources** - [Access resources](https://drive.google.com/drive/folders/1D2NvPsFWrqODGf4pj7OEbA_EhIXvH53g?usp=sharing)
- **Master Google Sheet** - Central hub with links to all resources
- **Menon's Git Repository for LEARNING Material** - [CMU PGSS 2024 Learning Material](https://github.com/menonpg/CMU_PGSS_2024)
- **PROJECT GIT REPOSITORY** - [PGSS 2025 Deep Research Agent Project](https://github.com/menonpg/PGSS2025_Deep_Research_Agent_Project)
- **GitHub Student Developer Pack** - [Sign up for benefits](https://education.github.com/pack)
- **Slack Workspace** - Menon Lab Slack for team communication
- **Posit / RStudio Cloud** - [Access RStudio Cloud](https://posit.cloud/)

## Software Installation Requirements

### Required Downloads

1. **VS Code** - Primary development environment
2. **Git**
   - Windows: Direct download from git-scm.com
   - Mac: Install via Homebrew (`brew install git`)
3. **Homebrew** (Mac users) - Package manager from brew.sh
4. **Miniconda** - Python environment management
5. **Node.js** - For additional tools (`brew install node`)

### Python Packages to Install

```bash
pip install openai
pip install python-dotenv
pip install langchain
pip install langchain-community
pip install google-search-results
pip install serpapi
```

## Development Environment Setup

### Git Repository Setup

- Created public repository: `pgss-2025-deep-research-agent`
- Students will create individual branches for their work
- Main branch protected - changes via pull requests only

### Environment Configuration

- Create `.env` file in repository root (DO NOT commit to Git)
- Add `.env` to `.gitignore` file
- Store API keys and secrets in `.env` file only

### VS Code Extensions

- **GitHub Copilot** - AI coding assistance
- **Gemini CLI** - Google's command line LLM interface

## Project Development Process

### Coding Workflow Demonstrated

1. **Clone Repository**

   ```bash
   git clone [repository-url]
   ```

2. **Create Feature Branch**

   - Work on individual branches
   - Test code thoroughly before committing

3. **Commit and Push Changes**

   - Use descriptive commit messages
   - Create pull requests for code review

4. **Merge to Main**
   - Code review process
   - Merge approved changes

### AI-Assisted Development

- Use GitHub Copilot for code suggestions
- Iterative debugging process with AI assistance
- Copy error messages to AI chat for troubleshooting
- Always understand code before implementing

## Technical Implementation

### Azure OpenAI Integration

- Successfully implemented basic chat interface
- Uses Azure OpenAI GPT-4.0 endpoint
- Configured with proper API authentication
- Environment variables for secure key management

### Web Search Integration

- Integrated SERP API for Google search capabilities
- Used LangChain agents framework
- Created research agent with web access
- Implemented structured output with citations

### Example Code Structure

```python
# Basic chat with Azure OpenAI
def chat_with_ai(user_input):
    # API call to Azure OpenAI
    # Process response
    # Return formatted output

# Web-enabled research agent
def research_agent(query):
    # Search web for relevant information
    # Process search results
    # Generate comprehensive response with citations
```

## Action Items for Students

### By Next Meeting (Monday/Thursday)

1. **Complete Software Installation**

   - Install all required software (VS Code, Git, Miniconda, etc.)
   - Set up GitHub account with Andrew email
   - Join Menon Lab Slack workspace

2. **Environment Setup**

   - Clone the project repository
   - Create personal branch
   - Set up `.env` file with API keys
   - Install required Python packages

3. **Test Basic Functionality**

   - Run the Azure OpenAI chat example
   - Verify all installations work correctly
   - Test Git workflow (commit, push, pull request)

4. **API Key Setup**
   - Sign up for SERP API account (free tier)
   - Add SERP API key to `.env` file
   - Test web search integration

### Learning Objectives

- Understand Git workflow and collaboration
- Learn AI-assisted programming techniques
- Master environment configuration and security
- Develop systematic debugging approach

## Key Takeaways

### Programming Philosophy

- **Iterative Development** - Build, test, fix, repeat
- **AI as Assistant** - Use AI to help, but understand the code
- **Systematic Debugging** - Follow error messages methodically
- **Collaborative Development** - Use proper Git workflow

### Important Reminders

- Always test code before committing
- Never commit API keys or secrets
- Use descriptive commit messages
- Ask for help when stuck
- Read and understand AI-generated code

## Next Steps

The team will continue building the Deep Research Agent with enhanced capabilities for scientific literature analysis, including:

- PubMed integration
- Research paper analysis
- Citation management
- Advanced search capabilities

**Next Meeting:** Monday/Thursday (2:30 pm, DH-2315)

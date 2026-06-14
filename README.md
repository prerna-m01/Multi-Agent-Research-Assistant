# Multi-Agent Research Assistant

An AI-powered Multi-Agent Research Assistant built using FastAPI, Google Gemini, and Agentic AI principles. The system generates a structured research plan, gathers information, and produces a comprehensive report through collaboration between specialized agents.

## Features

* Multi-Agent Architecture
* Research Planning Agent
* Research Execution Agent
* Report Generation Agent
* FastAPI REST API
* Modular and Scalable Codebase
* Environment-Based Configuration
* Ready for LangGraph Integration
* Production-Friendly Project Structure

---

## Architecture

```text
User Query
     |
     v
+----------------+
| Planner Agent  |
+----------------+
     |
     v
Research Plan
     |
     v
+----------------+
| Research Agent |
+----------------+
     |
     v
Research Results
     |
     v
+----------------+
| Writer Agent   |
+----------------+
     |
     v
Final Research Report
```

---

## Project Structure

```text
multi_agent_research_assistant/
│
├── agent/
│   ├── planner_agent.py
│   ├── research_agent.py
│   └── writer_agent.py
│
├── api/
│   └── research.py
│
├── core/
│   └── config.py
│
├── orchestration/
│   └── workflow.py
│
├── schemas/
│   ├── request.py
│   └── state.py
│
├── services/
│   └── llm_service.py
│
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Tech Stack

### Backend

* FastAPI
* Uvicorn

### AI / LLM

* Google Gemini

### Agentic AI

* Multi-Agent Workflow
* Planner Agent
* Research Agent
* Writer Agent

### Future Integrations

* LangGraph
* Tavily Search
* LangSmith
* Vector Databases

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/multi-agent-research-assistant.git

cd multi-agent-research-assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## Run Application

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Generate Research Report

**POST**

```http
/research/
```

### Request

```json
{
    "query": "Applications of Quantum Computing"
}
```

### Response

```json
{
    "research_plan": [
        "Understand quantum computing fundamentals",
        "Review current industry applications",
        "Analyze challenges and limitations",
        "Study future research directions",
        "Prepare final report"
    ],
    "final_report": "Generated research report..."
}
```

---

## Workflow

1. User submits a research query.
2. Planner Agent creates a research plan.
3. Research Agent gathers information.
4. Writer Agent generates a final report.
5. API returns structured output.

---

## Learning Outcomes

This project demonstrates:

* Agentic AI Concepts
* FastAPI Development
* LLM Integration
* Multi-Agent System Design
* Modular Backend Architecture
* API Development
* Production-Oriented Project Structure

---



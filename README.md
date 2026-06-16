# Multi-Agent Research Assistant

## Overview

The Multi-Agent Research Assistant is an AI-powered research automation platform built using FastAPI, Gemini, Tavily Search, and Retrieval-Augmented Generation (RAG). The system utilizes multiple AI agents that work together to perform research planning, web information gathering, summarization, and report generation.

In addition to automated research, the application supports PDF uploads, document-based question answering, research history management, report downloads, and system health monitoring.

---

## Features

- Multi-Agent Research Workflow
- AI-Powered Research Planning
- Tavily Web Search Integration
- Gemini LLM Integration
- Automated Research Summarization
- Research Report Generation
- Research History Persistence
- PDF Upload and Processing
- Retrieval-Augmented Generation (RAG)
- Document Question Answering
- Report Export and Download
- System Statistics Dashboard
- Health Monitoring APIs
- Logging and Error Handling

---

## Architecture

```text
User Query
    │
    ▼
Planner Agent
    │
    ▼
Search Agent
    │
    ▼
Summarizer Agent
    │
    ▼
Writer Agent
    │
    ▼
Final Research Report
```

### Agent Responsibilities

- **Planner Agent** → Creates a research strategy and subtopics.
- **Search Agent** → Collects relevant information from the web.
- **Summarizer Agent** → Produces concise summaries from gathered data.
- **Writer Agent** → Generates the final structured research report.

---

## Tech Stack

### Backend

- FastAPI
- Python
- SQLAlchemy
- SQLite
- Pydantic

### AI & Search

- Google Gemini
- Tavily Search API

### RAG Components

- LangChain
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

### Utilities

- Logging
- Environment Variables
- PDF Processing

---

## Installation

Clone the repository:

```bash
git clone https://github.com/prerna-m01/Multi-Agent-Research-Assistant.git

cd Multi-Agent-Research-Assistant
```

Install dependencies:

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Research

```http
POST /research
```

Generate a complete research report.

---

### History

```http
GET /history
```

Retrieve all research reports.

```http
GET /history/{id}
```

Retrieve a specific report.

---

### Reports

```http
GET /report/{id}/download
```

Download a generated report.

---

### Document Upload

```http
POST /upload
```

Upload PDF documents for RAG processing.

---

### RAG Chat

```http
POST /chat
```

Ask questions about uploaded PDF documents.

---

### Statistics

```http
GET /stats
```

Retrieve system statistics and metrics.

---

### System Health

```http
GET /system-check
```

Verify:

- Database connectivity
- Vector Store availability
- Gemini API connectivity
- Tavily API connectivity

---

## Project Structure

```text
api/
agents/
core/
database/
orchestration/
schemas/
services/
uploads/
vectorstore/
main.py
```

---


# Agent Workflow Engine

A simple agent workflow engine built with FastAPI, supporting nodes, state, edges, branching, and looping.

## Features

- **Nodes**: Python functions that read and modify shared state
- **State**: Dictionary-based state that flows between nodes
- **Edges**: Define transitions between nodes
- **Branching**: Conditional routing based on state values
- **Looping**: Repeat nodes until conditions are met
- **Tool Registry**: Dictionary of callable tools
- **FastAPI Endpoints**:
  - `POST /graph/create`: Create a new graph
  - `POST /graph/run`: Run a graph with initial state
  - `GET /graph/state/{run_id}`: Get current state of a run

## Sample Workflows

Three sample workflows are pre-loaded:

1. **Code Review Mini-Agent** (Option A): Extracts functions, checks complexity, detects issues, suggests improvements, loops until quality_score >= 5
2. **Summarization + Refinement** (Option B): Splits text, generates summaries, merges, refines, stops when summary length < 200
3. **Data Quality Pipeline** (Option C): Profiles data, identifies anomalies, generates rules, applies rules, loops until anomalies <= 5

## How to Run

1. Install dependencies: `pip install -r app/requirements.txt`
2. Run the server: `uvicorn app.main:app --reload`
3. Access API docs at `http://localhost:8000/docs`

## Usage

### Create a Graph
```json
POST /graph/create
{
  "nodes": {
    "node1": {"id": "node1", "type": "function", "function_name": "extract_functions"}
  },
  "edges": [{"from_node": "node1", "to_node": "node2"}],
  "start_node": "node1"
}
```

### Run a Graph
```json
POST /graph/run
{
  "graph_id": "your-graph-id",
  "initial_state": {"code": "def hello(): pass"}
}
```

### Get Run State
```
GET /graph/state/your-run-id
```

## What the Engine Supports

- In-memory storage for graphs and runs
- Async execution of nodes
- Simple conditional branching and looping
- Tool registry for reusable functions

## Improvements for More Time

- Persistent storage (SQLite/Postgres)
- WebSocket for real-time logs
- More complex graph structures
- Error handling and retries
- Authentication and authorization
- Performance optimizations

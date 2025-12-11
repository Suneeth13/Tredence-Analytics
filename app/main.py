from .engine import WorkflowEngine
from .models import Node, Edge
from .workflows import (
    create_code_review_workflow,
    create_summarization_workflow,
    create_data_quality_workflow,
    create_simple_workflow,  # Add this line
)


from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from typing import Dict, Any, List

app = FastAPI(title="Agent Workflow Engine", description="A simple agent workflow engine with FastAPI")

engine = WorkflowEngine()

# Pre-load sample workflows
code_review_graph = create_code_review_workflow()
code_review_id = engine.create_graph(
    nodes=code_review_graph["nodes"],
    edges=code_review_graph["edges"],
    start_node=code_review_graph["start_node"]
)

simple_workflow_graph = create_simple_workflow()
simple_workflow_id = engine.create_graph(
    nodes=simple_workflow_graph["nodes"],
    edges=simple_workflow_graph["edges"],
    start_node=simple_workflow_graph["start_node"]
)


summarization_graph = create_summarization_workflow()
summarization_id = engine.create_graph(
    nodes=summarization_graph["nodes"],
    edges=summarization_graph["edges"],
    start_node=summarization_graph["start_node"]
)

data_quality_graph = create_data_quality_workflow()
data_quality_id = engine.create_graph(
    nodes=data_quality_graph["nodes"],
    edges=data_quality_graph["edges"],
    start_node=data_quality_graph["start_node"]
)

class CreateGraphRequest(BaseModel):
    nodes: Dict[str, Dict[str, Any]]
    edges: List[Dict[str, Any]]
    start_node: str

class RunGraphRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]

@app.post("/graph/create")
async def create_graph(request: CreateGraphRequest):
    try:
        nodes = {k: Node(**v) for k, v in request.nodes.items()}
        edges = [Edge(**e) for e in request.edges]
        graph_id = engine.create_graph(nodes, edges, request.start_node)
        return {"graph_id": graph_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/graph/run")
async def run_graph(request: RunGraphRequest):
    try:
        result = await engine.run_graph(request.graph_id, request.initial_state)
        return result  # Now includes run_id
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/graph/state/{run_id}")
async def get_run_state(run_id: str):
    try:
        state = engine.get_run_state(run_id)
        if state is None:
            raise HTTPException(status_code=404, detail="Run not found")
        return state
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/workflows")
async def get_preloaded_workflows():
    return {
        "code_review": code_review_id,
        "summarization": summarization_id,
        "data_quality": data_quality_id,
        "simple": simple_workflow_id,  # Add this line
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

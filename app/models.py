from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class Node(BaseModel):
    id: str
    type: str  # "function" or "condition"
    function_name: Optional[str] = None
    condition: Optional[str] = None

class Edge(BaseModel):
    from_node: str
    to_node: str
    condition: Optional[str] = None

class Graph(BaseModel):
    id: str
    nodes: Dict[str, Node]
    edges: List[Edge]
    start_node: str

class State(BaseModel):
    data: Dict[str, Any]
    current_node: Optional[str] = None
    run_id: str

class ExecutionLog(BaseModel):
    run_id: str
    steps: List[Dict[str, Any]]

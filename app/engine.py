import asyncio
from typing import Dict, Any, List, Optional
from .models import Graph, Node, Edge, State, ExecutionLog
from .tools import get_tool
import uuid
from .models import Graph, Node, Edge, State, ExecutionLog

class WorkflowEngine:
    def __init__(self):
        self.graphs: Dict[str, Graph] = {}
        self.runs: Dict[str, State] = {}
        self.logs: Dict[str, ExecutionLog] = {}

    def create_graph(self, nodes: Dict[str, Node], edges: List[Edge], start_node: str) -> str:
        graph_id = str(uuid.uuid4())
        graph = Graph(id=graph_id, nodes=nodes, edges=edges, start_node=start_node)
        self.graphs[graph_id] = graph
        return graph_id

    async def run_graph(self, graph_id: str, initial_state: Dict[str, Any]) -> Dict[str, Any]:
        if graph_id not in self.graphs:
            raise ValueError("Graph not found")

        graph = self.graphs[graph_id]
        run_id = str(uuid.uuid4())
        state = State(data=initial_state.copy(), current_node=graph.start_node, run_id=run_id)
        self.runs[run_id] = state
        self.logs[run_id] = ExecutionLog(run_id=run_id, steps=[])

        execution_log = []

        while state.current_node:
            node = graph.nodes.get(state.current_node)
            if not node:
                break

            # Execute node
            result = await self._execute_node(node, state.data)
            state.data.update(result)
            execution_log.append({"node": state.current_node, "result": result})

            # Determine next node
            next_node = self._get_next_node(graph, node, state.data)
            state.current_node = next_node

        self.logs[run_id].steps = execution_log
        return {"run_id": run_id,"final_state": state.data,"execution_log": execution_log
        }


    async def _execute_node(self, node: Node, state_data: Dict[str, Any]) -> Dict[str, Any]:
        if node.type == "function" and node.function_name:
            tool = get_tool(node.function_name)
            if tool:
                # Simulate async if needed
                result = tool(**{k: v for k, v in state_data.items() if k in tool.__code__.co_varnames})
                return result
        elif node.type == "condition":
            # For condition nodes, just pass through
            return {}
        return {}

    def _get_next_node(self, graph: Graph, node: Node, state_data: Dict[str, Any]) -> Optional[str]:
        for edge in graph.edges:
            if edge.from_node == node.id:
                if edge.condition:
                    try:
                        if eval(edge.condition, {"state": state_data}):
                            return edge.to_node
                    except:
                        pass
                else:
                    return edge.to_node
        return None

    def get_run_state(self, run_id: str) -> Optional[Dict[str, Any]]:
        run = self.runs.get(run_id)
        if run:
            return run.data
        return None

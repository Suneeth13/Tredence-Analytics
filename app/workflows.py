from .models import Node, Edge
from typing import Dict, Any, List

# Option A: Code Review Mini-Agent
def create_code_review_workflow() -> Dict[str, Any]:
    nodes = {
        "extract": Node(id="extract", type="function", function_name="extract_functions"),
        "check_complexity": Node(id="check_complexity", type="function", function_name="check_complexity"),
        "detect_issues": Node(id="detect_issues", type="function", function_name="detect_issues"),
        "suggest_improvements": Node(id="suggest_improvements", type="function", function_name="suggest_improvements"),
        "loop_condition": Node(id="loop_condition", type="condition", condition="state.get('quality_score', 0) < 5")
    }
    edges = [
        Edge(from_node="extract", to_node="check_complexity"),
        Edge(from_node="check_complexity", to_node="detect_issues"),
        Edge(from_node="detect_issues", to_node="suggest_improvements"),
        Edge(from_node="suggest_improvements", to_node="loop_condition"),
        Edge(from_node="loop_condition", to_node="extract", condition="state.get('quality_score', 0) < 5"),
        Edge(from_node="loop_condition", to_node="end", condition="state.get('quality_score', 0) >= 5")
    ]
    return {"nodes": nodes, "edges": edges, "start_node": "extract"}

# Option B: Summarization + Refinement
def create_summarization_workflow() -> Dict[str, Any]:
    nodes = {
        "split_text": Node(id="split_text", type="function", function_name="split_text"),
        "generate_summaries": Node(id="generate_summaries", type="function", function_name="generate_summaries"),
        "merge_summaries": Node(id="merge_summaries", type="function", function_name="merge_summaries"),
        "refine_summary": Node(id="refine_summary", type="function", function_name="refine_summary"),
        "check_length": Node(id="check_length", type="condition", condition="len(state.get('refined_summary', '')) >= 200")
    }
    edges = [
        Edge(from_node="split_text", to_node="generate_summaries"),
        Edge(from_node="generate_summaries", to_node="merge_summaries"),
        Edge(from_node="merge_summaries", to_node="refine_summary"),
        Edge(from_node="refine_summary", to_node="check_length"),
        Edge(from_node="check_length", to_node="refine_summary", condition="len(state.get('refined_summary', '')) >= 200"),
        Edge(from_node="check_length", to_node="end", condition="len(state.get('refined_summary', '')) < 200")
    ]
    return {"nodes": nodes, "edges": edges, "start_node": "split_text"}

# Option C: Data Quality Pipeline
def create_data_quality_workflow() -> Dict[str, Any]:
    nodes = {
        "profile_data": Node(id="profile_data", type="function", function_name="profile_data"),
        "identify_anomalies": Node(id="identify_anomalies", type="function", function_name="identify_anomalies"),
        "generate_rules": Node(id="generate_rules", type="function", function_name="generate_rules"),
        "apply_rules": Node(id="apply_rules", type="function", function_name="apply_rules"),
        "check_anomalies": Node(id="check_anomalies", type="condition", condition="state.get('anomalies', 0) > 5")
    }
    edges = [
        Edge(from_node="profile_data", to_node="identify_anomalies"),
        Edge(from_node="identify_anomalies", to_node="generate_rules"),
        Edge(from_node="generate_rules", to_node="apply_rules"),
        Edge(from_node="apply_rules", to_node="check_anomalies"),
        Edge(from_node="check_anomalies", to_node="identify_anomalies", condition="state.get('anomalies', 0) > 5"),
        Edge(from_node="check_anomalies", to_node="end", condition="state.get('anomalies', 0) <= 5")
    ]
    return {"nodes": nodes, "edges": edges, "start_node": "profile_data"}

def create_simple_workflow() -> Dict[str, Any]:
    nodes = {
        "start": Node(id="start", type="function", function_name="start_node"),
        "middle": Node(id="middle", type="function", function_name="middle_node"),
        "end": Node(id="end", type="function", function_name="end_node"),
    }
    edges = [
        Edge(from_node="start", to_node="middle"),
        Edge(from_node="middle", to_node="end"),
    ]
    return {"nodes": nodes, "edges": edges, "start_node": "start"}

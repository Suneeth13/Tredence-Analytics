from typing import Dict, Any, List, Callable

# Tool registry: a dictionary of tool functions
tool_registry: Dict[str, Callable] = {}

def register_tool(name: str, func: Callable):
    """Register a tool function."""
    tool_registry[name] = func

def get_tool(name: str):
    """Get a tool function by name."""
    return tool_registry.get(name)

# Pre-register some example tools
def extract_functions(code: str) -> Dict[str, Any]:
    """Extract functions from code (simplified)."""
    # Dummy implementation: count 'def' occurrences
    functions = code.count('def')
    return {"functions": functions}

def check_complexity(code: str) -> Dict[str, Any]:
    """Check code complexity (simplified)."""
    lines = len(code.split('\n'))
    complexity = min(lines // 10, 10)  # Dummy complexity score
    return {"complexity": complexity}

def detect_issues(code: str) -> Dict[str, Any]:
    """Detect basic issues in code (simplified)."""
    issues = 0
    if 'TODO' in code:
        issues += 1
    if len(code) > 1000:
        issues += 1
    return {"issues": issues}

def suggest_improvements(code: str) -> Dict[str, Any]:
    """Suggest improvements (simplified)."""
    suggestions = []
    if 'print(' in code:
        suggestions.append("Consider using logging instead of print.")
    # Calculate quality score based on issues
    quality_score = 10 - len(suggestions)  # Dummy score
    return {"suggestions": suggestions, "quality_score": quality_score}

def split_text(text: str) -> Dict[str, Any]:
    """Split text into chunks."""
    chunks = [text[i:i+100] for i in range(0, len(text), 100)]
    return {"chunks": chunks}

def generate_summaries(chunks: List[str]) -> Dict[str, Any]:
    """Generate summaries for chunks (simplified)."""
    summaries = [f"Summary of chunk {i+1}" for i in range(len(chunks))]
    return {"summaries": summaries}

def merge_summaries(summaries: List[str]) -> Dict[str, Any]:
    """Merge summaries."""
    merged = " ".join(summaries)
    return {"merged_summary": merged}

def refine_summary(merged_summary: str) -> Dict[str, Any]:
    """Refine summary."""
    refined = merged_summary[:200]  # Truncate to 200 chars
    return {"refined_summary": refined}

def profile_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Profile data."""
    num_records = len(data)
    columns = list(data[0].keys()) if data else []
    return {"num_records": num_records, "columns": columns}

def identify_anomalies(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Identify anomalies (simplified)."""
    anomalies = sum(1 for record in data if any(isinstance(v, str) and len(v) > 50 for v in record.values()))
    return {"anomalies": anomalies}

def generate_rules(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate rules (simplified)."""
    rules = ["Rule 1: Check string lengths"]
    return {"rules": rules}

def apply_rules(data: List[Dict[str, Any]], rules: List[str]) -> Dict[str, Any]:
    """Apply rules."""
    cleaned_data = data  # Dummy: no actual cleaning
    return {"cleaned_data": cleaned_data}

def start_node():
    return {"message": "Starting workflow"}

def middle_node():
    return {"message": "In the middle"}

def end_node():
    return {"message": "Ending workflow"}


# Register all tools
register_tool("extract_functions", extract_functions)
register_tool("check_complexity", check_complexity)
register_tool("detect_issues", detect_issues)
register_tool("suggest_improvements", suggest_improvements)
register_tool("split_text", split_text)
register_tool("generate_summaries", generate_summaries)
register_tool("merge_summaries", merge_summaries)
register_tool("refine_summary", refine_summary)
register_tool("profile_data", profile_data)
register_tool("identify_anomalies", identify_anomalies)
register_tool("generate_rules", generate_rules)
register_tool("apply_rules", apply_rules)

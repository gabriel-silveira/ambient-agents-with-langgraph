from langgraph.graph import END, START
from src.state import workflow
from src.nodes import call_llm, run_tool, should_continue

workflow.add_node("call_llm", call_llm)
workflow.add_node("run_tool", run_tool)

workflow.add_edge(START, "call_llm")
workflow.add_conditional_edges("call_llm", should_continue, {"run_tool": "run_tool", END: END})
workflow.add_edge("run_tool", END)

app = workflow.compile()
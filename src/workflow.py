from langgraph.graph import END, START
from src.state import workflow
from src.nodes import write_email_node

workflow.add_node("write_email_node", write_email_node)
workflow.add_edge(START, "write_email_node")
workflow.add_edge("write_email_node", END)

app = workflow.compile()
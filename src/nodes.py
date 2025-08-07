from src.types import StateSchema
from src.llm import llm
from src.tools import write_email_tool

model_with_tools = llm.bind_tools([write_email_tool], tool_choice="any", parallel_tool_calls=False)

def write_email_node(state: StateSchema) -> StateSchema:
  output = model_with_tools.invoke(state["request"])
  args = output.tool_calls[0]['args']
  email = write_email_tool.invoke(args)
  return {"email": email}
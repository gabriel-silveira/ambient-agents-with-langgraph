from typing import Literal
from langgraph.graph import MessagesState, END
from src.llm import llm
from src.tools import write_email_tool

model_with_tools = llm.bind_tools([write_email_tool], tool_choice="any", parallel_tool_calls=False)


def call_llm(state: MessagesState) -> MessagesState:
  """Run LLM"""

  print("Initial state:\n")
  print(state)

  output = model_with_tools.invoke(state["messages"])
  return {"messages": output}


def run_tool(state: MessagesState) -> MessagesState:
  """Performs a tool call"""

  result = []

  for tool_call in state["messages"][-1].tool_calls:
    observation = write_email_tool.invoke(tool_call["args"])
    result.append({"role": "tool", "content": observation, "tool_call_id": tool_call["id"]})

  return {"messages": result}


def should_continue(state: MessagesState) -> Literal["run_tool", END]:
  """Route to tool handler, or end if Done tool called"""

  # Get the last message
  last_message = state["messages"][-1]

  # if the last message is a tool call, check if it's a Done tool call
  if last_message.tool_calls:
    return "run_tool"

  # otherwise, we stop (reply to the user)
  return END
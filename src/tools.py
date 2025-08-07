from langchain.tools import tool

@tool
def write_email_tool(to: str, subject: str, content: str) -> str:
  """Writes and send email."""
  return f"Email sent to {to} with subject {subject} and content {content}"
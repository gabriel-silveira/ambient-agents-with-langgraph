
from langchain.agents import create_react_agent, AgentExecutor
from src.llm import llm
from src.tools import write_email_tool
from src.memory import memory
from langchain.memory import ConversationBufferMemory
from langchain import hub

# Criar um template de prompt adequado para o agente ReAct
prompt = hub.pull("hwchase17/react")

react_agent = create_react_agent(
  llm,
  tools=[write_email_tool],
  prompt=prompt,
)

# Configurar a memória para o agente
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Criar o executor do agente com memória
agent = AgentExecutor(
  agent=react_agent,
  tools=[write_email_tool],
  memory=memory,
  verbose=True
)
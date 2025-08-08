from langchain.agents import create_react_agent, AgentExecutor
from src.llm import llm
from src.tools import write_email_tool
from langchain.memory import ConversationBufferMemory
from langchain import hub

# Usar o prompt padrão do hub LangChain
prompt = hub.pull("hwchase17/react")

# Criar o agente ReAct
react_agent = create_react_agent(
    llm=llm,
    tools=[write_email_tool],
    prompt=prompt
)

# Configurar a memória para o agente
# Nota: Embora haja um aviso de depreciação, esta abordagem ainda é funcional
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Criar o executor do agente com memória
agent = AgentExecutor(
    agent=react_agent,
    tools=[write_email_tool],
    memory=memory,
    verbose=True
)
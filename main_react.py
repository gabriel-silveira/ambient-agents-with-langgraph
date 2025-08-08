from src.agents.resct_agent import agent


if __name__ == "__main__":
    config = {"configurable": {"thread_id": "ABC"}}

    result = agent.invoke({ 
        "input": "O que são boas práticas para a escrita de e-mails?",
        "chat_history": []  # Adiciona histórico vazio para a primeira mensagem
    }, config)

    print("\nResposta do agente:")
    print(result["output"])
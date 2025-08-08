from src.agents.react_agent import agent


if __name__ == "__main__":
    # Configurar thread_id para persistência de memória entre chamadas
    config = {"configurable": {"thread_id": "ABC123"}}
    
    # Primeira mensagem
    first_message = "O que são boas práticas para a escrita de e-mails?"
    print(f"\nVocê: {first_message}")
    
    # Chamar o agente com a primeira mensagem
    result = agent.invoke({"input": first_message}, config)
    
    # Mostrar resposta
    print(f"\nAssistente: {result['output']}")
    
    # Segunda mensagem para demonstrar a memória
    second_message = "Você poderia resumir o que falamos até agora?"
    print(f"\nVocê: {second_message}")
    
    # Chamar o agente com a segunda mensagem
    result = agent.invoke({"input": second_message}, config)
    
    # Mostrar resposta
    print(f"\nAssistente: {result['output']}")
# Ambient Agents com LangGraph

## Descrição

Este projeto demonstra a implementação de agentes ambientais usando LangGraph, uma biblioteca para construção de fluxos de trabalho com modelos de linguagem (LLMs). O sistema permite automatizar tarefas como redigir e-mails através de um fluxo de trabalho definido com nós e arestas, onde o LLM pode tomar decisões e executar ferramentas específicas.

## Estrutura do Projeto

```
.
├── .env                  # Arquivo de variáveis de ambiente
├── .gitignore            # Configuração de arquivos ignorados pelo git
├── .python-version       # Versão do Python utilizada
├── main.py               # Ponto de entrada da aplicação
├── pyproject.toml        # Configuração do projeto e dependências
├── README.md             # Este arquivo
└── src/                  # Código fonte
    ├── config.py         # Configuração e carregamento de variáveis de ambiente
    ├── llm.py            # Inicialização do modelo de linguagem
    ├── nodes.py          # Definição dos nós do fluxo de trabalho
    ├── state.py          # Definição do estado do fluxo de trabalho
    ├── tools.py          # Ferramentas disponíveis para o LLM
    └── workflow.py       # Configuração do fluxo de trabalho
```

## Funcionalidades

- **Fluxo de Trabalho Baseado em Grafos**: Utiliza o LangGraph para definir um fluxo de trabalho com nós e arestas condicionais.
- **Integração com OpenAI**: Usa o modelo GPT-4.1 da OpenAI para processamento de linguagem natural.
- **Ferramentas Personalizadas**: Implementa ferramentas como `write_email_tool` que podem ser chamadas pelo LLM.
- **Processamento de Mensagens**: Gerencia um estado de mensagens que permite conversas contextuais.

## Requisitos

- Python >= 3.11
- Dependências:
  - langchain >= 0.3.27
  - langchain-openai >= 0.3.28
  - langgraph >= 0.6.3
  - python-dotenv >= 1.1.1

## Configuração

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -e .
   ```
4. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   OPENAI_API_KEY=sua_chave_api_aqui
   LANGSMITH_API_KEY=sua_chave_langsmith_aqui  # Opcional
   ```

## Uso

Execute o script principal para ver o agente em ação:

```bash
python main.py
```

O exemplo padrão solicita ao agente que redija uma resposta sobre uma reunião de amanhã. Você pode modificar a mensagem do usuário em `main.py` para testar diferentes cenários.

## Como Funciona

1. O fluxo de trabalho é definido em `workflow.py` usando o LangGraph.
2. Quando uma mensagem do usuário é recebida, o LLM (`call_llm`) processa a mensagem.
3. O nó condicional `should_continue` decide se deve executar uma ferramenta ou finalizar a resposta.
4. Se uma ferramenta for chamada, o nó `run_tool` a executa e retorna o resultado.
5. O resultado é formatado e apresentado ao usuário.

## Personalização

Para adicionar novas ferramentas:

1. Defina a ferramenta em `tools.py` usando o decorador `@tool`.
2. Atualize `nodes.py` para incluir a nova ferramenta na lista de ferramentas disponíveis.

from src.workflow import app


if __name__ == "__main__":
    result = app.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Draft a response to my boss about tomorrow's meeting"
            }
        ]
    })

    for message in result["messages"]:
        message.pretty_print()
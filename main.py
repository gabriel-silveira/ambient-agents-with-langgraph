from src.workflow import app


if __name__ == "__main__":
    response = app.invoke({"request": "Draft a response to my boss about tomorrow's meeting"})
    print(response)

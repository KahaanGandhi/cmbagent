import os
from cmbagent import one_shot

if __name__ == "__main__":
    api_key = input("Enter your OpenAI API key: ").strip()
    os.environ["OPENAI_API_KEY"] = api_key
    print("Sending request with streaming enabled:\n")
    one_shot("Say hello to streaming", stream=True)


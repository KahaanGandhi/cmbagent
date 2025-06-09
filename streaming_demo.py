from autogen import OpenAIWrapper, get_config_list

if __name__ == "__main__":
    api_key = input("Enter your OpenAI API key: ").strip()
    configs = get_config_list(api_keys=[api_key], stream=True)
    wrapper = OpenAIWrapper(config_list=configs)
    print("Sending request with streaming enabled:\n")
    wrapper.create(messages=[{"role": "user", "content": "Hello"}], stream=True)
    print()  # newline after streaming output

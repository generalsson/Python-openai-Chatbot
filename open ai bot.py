import openai
openai.api_key = "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"

while True:
    mobile_engine = "text-davinci-003"
    prompt = input("Enter your prompt: ")
    if 'exit' in prompt or 'quit' in prompt:
        break

    completion = openai.Completion.create(
        engine=mobile_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1, stop=None,
        temperature=0.5)

    response = completion.choices[0].text
    print(response)
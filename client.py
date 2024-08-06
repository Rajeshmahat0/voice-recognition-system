# from openai import OpenAI
# api_keys = "sk-proj-INpgICHaOhNOb4gv0LtrT3BlbkFJT5q1DFxeznbxUWrWdlX2"

# client = OpenAI(api_keys)
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google cloud."},
#     {"role": "user", "content": "what is coding"}  #use to ask
#   ]
# )

# print(completion.choices[0].message.content)



import openai

# Set your API key
openai.api_key = "sk-svcacct-Gfzzj47J5rVFsMBfoy6pT3BlbkFJFevUlSn3Afatwhs4z4NQ"

# Make a request to the OpenAI API for a chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google cloud."},
        {"role": "user", "content": "what is coding"}  # Use to ask
    ]
)

# Print the response from the API
print(response.choices[0].message['content'])



import os
from openai import AzureOpenAI
import re

client = AzureOpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="8a195875605648a9bbb56dd739ad4118",
    api_version="2023-12-01-preview",
    azure_endpoint = 'https://provider-azure-open-ai.openai.azure.com/'
)

deployment_name='hackathon_genhealth' 


def get_completion_from_messages(system_message, user_message, temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    
    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    print(response)
    text = response.choices[0].message.content
    
    
    #print(type(text))
    #x = re.search("SELECT", text)
    #print('x',x)
    #st = x.start()
    #print('st',st)
    #print(text[st:])
    #y = re.search(";",text[st:])
    #end = st+y.start()
    #text= text[st:end]
    #text = text.replace('\n', ' ')
    #print('text')
    #print(text)
    return text
    
def get_complete(system_message, user_message, temperature=0, max_tokens=3500) -> str:
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]
    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    text = response.choices[0].message.content
    print('te',text)
    
    #print(type(text))
    x = re.search("```", text)
    #print('x',x)
    st = x.end()
    y = re.search('```',text[st:])
    end = st+y.start()
    text= text[st:end]

    #print(text)
    return text
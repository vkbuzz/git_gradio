import random
import gradio as gr
'''
langchain example
'''

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import gradio as gr
import os

os.environ["OPENAI_API_KEY"] = "sk-proj-FAKEKEY"  # Replace with your key

llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo')
#llm = ChatOpenAI(temperature=0.1, model='gpt-3.5-turbo')

def predict(message, history):
    history_langchain_format = []
    for msg in history:
        if msg['role'] == "user":
            history_langchain_format.append(HumanMessage(content=msg['content']))
        elif msg['role'] == "assistant":
            history_langchain_format.append(AIMessage(content=msg['content']))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content

gr.ChatInterface(predict, type="messages").launch()

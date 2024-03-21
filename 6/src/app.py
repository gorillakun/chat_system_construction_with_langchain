import os

import streamlit as st

st.title("langchainのstream-appデモ画面")
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

prompt = st.chat_input("what is up?") # プレースホルダありのinput
# print(prompt)

if prompt: # promptが空でない場合
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"): # userのアイコンで
      st.markdown(prompt) # チャットメッセージを表示

    with st.chat_message("asssitant"):
      chat = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPENAI_API_TEMPERATURE"],
      )
      messages = [HumanMessage(prompt)]
      response = chat(messages)
      st.markdown(response.content)

    
    st.session_state.messages.append({"role": "assistant", "content": response})
import openai
import re
import streamlit as st
import os

#Deloitte
openai.api_type = "azure"
openai.api_base = "https://clause-ki.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = ""
deployment = "gpt-3-fagdag" 

col1, col2, col3 = st.columns([40, 2, 1])
with col1:
    st.markdown(
        '<div class="logo"><img src="https://www2.deloitte.com/content/dam/Deloitte/no/Images/DEL_SEC_RGB.png" width="150" height="60 style="vertical-align:top"" alt="Logo"></div>',
        unsafe_allow_html=True,
    )

def show_popup():
    with st.container():
        st.info("""
            Here are a few sample questions:
            1. Where can I find information about our climate impact?
            2. I'm looking for data on our sales activity. Can you direct me to the right report?
            3. Can you guide me to the report that contains information about our greenhouse gas levels?
            4. I'm searching for data on our personvern handling. Which report should I refer to?        
        """)
 
# Initialiser 'show_popup' i session_state
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False
 
# Kolonnekonfigurasjon for å plassere 'ℹ️'-knappen
with col3:
    if st.button("ℹ️"):
        # Veksle tilstanden for å vise eller skjule popup-vinduet
        st.session_state.show_popup = not st.session_state.show_popup
 
# Vis popup-vinduet basert på tilstanden
if st.session_state.show_popup:
    show_popup()

with open('prompt.txt', 'r') as f:
    system_prompt = f.read()

print(system_prompt)# If the messages attribute is not already in session_state, initialize it
if "messages" not in st.session_state:
    # System prompt includes table information, rules, and prompts the LLM to produce
    # a welcome message to the user.
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt, 'avatar':None})

# Display the existing chat messages
for message in st.session_state.messages:
    # Your code to display messages here
    if message["role"] == "system":
        continue   
    with st.chat_message(message["role"], avatar=message['avatar']):
        st.write(message["content"])
        if "results" in message:
            st.dataframe(message["results"])

# If last message is not from assistant, we need to generate a new response
if st.session_state.messages[-1]["role"] != "assistant": 
    with st.chat_message("assistant", avatar="maskot.png"):
        response = ""
        resp_container = st.empty()
        for delta in openai.ChatCompletion.create(
            engine=deployment,
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        ):
            if delta.choices and delta.choices[0].delta.get("content"):
                response += delta.choices[0].delta.get("content", "")
                resp_container.markdown(response)

        message = {"role": "assistant", "content": response, 'avatar':'maskot.png'}

        st.session_state.messages.append(message)

last_user_question = ""
last_bot_response = ""
if len(st.session_state.messages) > 1:
    last_user_question = st.session_state.messages[-2]["content"] if len(st.session_state.messages[-2]["content"]) <= 20000 else ""
    last_bot_response = st.session_state.messages[-1]["content"] if len(st.session_state.messages[-1]["content"]) <= 20000 else ""
 
col1, col2, col3 = st.columns([13, 1, 1])
col1, col2, col3 = st.columns([13, 1, 1])
col1, col2, col3 = st.columns([13, 1, 1])

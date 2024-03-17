#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate


# In[9]:


st.set_page_config(page_title="🦜🦜 Blog Outline Generator App")
st.title('🦜🦜 Blog Outline Generator App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(topic):
    llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
    
    template = 'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'
    prompt = PromptTemplate(input_variables=['topic'], template=template)
    prompt_query = prompt.format(topic=topic)
    
    response = llm(prompt_query)
    return st.info(response)

with st.form('myform'):
    topic_text = st.text_input('Enter keyword:', '')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(topic_text)


# In[10]:


import os

notebook_path = os.getcwd()
print(notebook_path)


# In[ ]:





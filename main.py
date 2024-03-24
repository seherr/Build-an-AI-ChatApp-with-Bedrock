from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
import boto3
import os
import streamlit as st

os.environ['AWS_Profile'] = 'seher'  #profil oluştur

#create bedrock client 
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
    
)

modelID = 'anthropic.claude-v2'   #başka modelleri denemek iiçin burayı değiştirmen yeterli

#create llm with bedrock 
llm=Bedrock(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={'max_tokens_to_simple':2000,'temperature':0.9}
)

#create chatbot function -- langchain prompt structue 
def my_chatbot(language,freeform_text):
    prompt=PromptTemplate(
        input_variables=['language','freeform_tect'],
        template='You are a chatbot. You are in{language}.\n\n{freeform_text})'
    )

    #create chain 
    bedrock_chain= LLMChain(llm=llm, prompt=prompt)

    response=bedrock_chain({'language':language, 'freeform_text':freeform_text})
    return response

#testing
print(my_chatbot('English','how re you?'))

#frontend park 
st.title('Hello I am Bedrock Chatbot' )

language = st.sidebar.selectbox('Language',['English','Turkish'])
if language:
    freeform_text = st.sidebar.text_area(label='What is your question?', max_chars=100)
    
if freeform_test:
    response = my_chatbot(language,freeform_text)
    st.write(response)

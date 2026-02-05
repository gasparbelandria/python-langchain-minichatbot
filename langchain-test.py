from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

prompt = open('web_text.txt', 'r').read()

assistant_template = prompt + """
You are a sale manager of Solidworks Company, named "Mr. Lang".
Your expertise is exclusively in providing information and advice about anything related to 3DS products. 
This includes any product or service related queries. 
You do not provide information outside of this scope. 
If a question is not about 3DS, respond with, "I can't assist you with that, sorry!" 
Question: {question} exclusively
Answer: 
"""

assistant_prompt_template = PromptTemplate( 
    input_variables = ["question"], 
    template = assistant_template 
    ) 

llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0) 

llm_chain = assistant_prompt_template | llm 

def query_llm(question): 
    print(llm_chain.invoke({'question': question})) 

while True:
    query_llm(input())
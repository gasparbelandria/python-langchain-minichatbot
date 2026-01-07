# 5 interactions cost = $0.01

from flask import Flask, render_template, request, jsonify
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

prompt = open('website_text.txt', 'r').read()

assistant_template = prompt + """
You are a sale manager of 3DS Company, named "Mr. Lang". 
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
    response = llm_chain.invoke({'question': question}) 
    return response 

app = Flask(__name__) 

@app.route("/") 
def index(): 
    return render_template("index.html") 

@app.route("/chatbot", methods=["POST"]) 
def chatbot(): 
    data = request.get_json() 
    question = data["question"] 
    response = query_llm(question) 
    return jsonify({"response": response}) 

if __name__ == "__main__": 
    app.run(debug=True)
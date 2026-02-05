# python-langchain-minichatbot  
  
As part of my Python learning journey, this repository contains basic examples of how to use: BeautifulSoup, Flask, OpenAI, Langchain, and of course, Python at a very basic level (hello world).  

> Clone or download this repo.
  
First thing to do is setting up all of the environment and development variables that we will need.  
  
Because we are going to use OpenIA API Key, before to procedure make sure you have one.  
  
[OpenAi API Key link](https://platform.openai.com/docs/quickstart)

Now let's install the SDK via npm.

```
npm install openai
```   

With the OpenAI API Key and OpenAI SDK installed we are able to continue.

Libraries used on this example.

| Library | Link | Summary |
|--|--|--|
| BeautifulSoup | https://beautiful-soup-4.readthedocs.io/en/latest/ |Python library for pulling data out of HTML and XML files|
|Flask|https://flask.palletsprojects.com/en/stable/ |Lightweight Python micro-framework for building web applications and APIs|
|Requests|https://pypi.org/project/requests/| Third-party HTTP library for Python, designed to make sending HTTP requests user-friendly and straightforward |
|PyMuPDF|https://pymupdf.readthedocs.io/en/latest/| PDF manipulation, analysis, and data extraction |


Now, install all the libraries we will using:  
  
> pip insltall pymupdf
> pip install requests
> pip install langchain  
> pip install Flask  
  
The goal of this exercise is to create a chatbot to provide information about a specific topic. In this case, I used a website, but you can simply fill a text file with the relevant context.  

## pdf.py
Extract text from a PDF, output file will be pdf_text.txt.

In this example, we'll be collecting and preparing PDF data for our chat bot. 

So first of all, let's get started by importing the module that we'll need in order to create a chat bot. 

We'll be using the Fitz module that comes from the PyMuPDF library, and this library is specifically made in order to work with PDFs. 

Then we can go ahead and define our function. Here it is called it `extract_text_from_pdf`, and this is going to be the text that is used by our chat bot in order to help us get the best responses. 

So in our function, we first of all go ahead and open up the file, which is specified by the `pdf_file_path`. In our case, we'll be using the `3dexperience-solidworks-offers-product-matrix.pdf` which is a public file. 

So after we go ahead and take the path of the PDF file as an argument, we go ahead and initialize an empty string `pdf_text`, and this will store the extractive text from the PDF. 

After this, we go ahead and load in the current page of the PDF by using the `load_page` command. Then we go ahead and get all of the text on this page. 

Finally, we go ahead and close the document and check if there were any errors while doing any of the extraction.

As well as setting out a new variable called `extracted_text`. And in this variable we call the function and give it the PDF path of our PDF. 

Finally, all that's left to do now is open up a new text file and add in everything from the PDF into the text. So that's all for this file. 

Let's go ahead and give this a run. If all went ok,  you can see there is a `pdf_text.txt` file. And this text will have everything that was in the PDF stored in as a text file.

    import fitz  
      
    def extract_text_from_pdf(pdf_file_path):  
        try:  
            doc = fitz.open(pdf_file_path)  
            pdf_text = ""  
      for page_num in range(doc.page_count):  
                page = doc.load_page(page_num)  
                pdf_text += page.get_text("text")  
            doc.close()  
            return pdf_text  
        except Exception as e:  
            return f"Error extracting text: {e}"  
      
    pdf_path = "3dexperience-solidworks-offers-product-matrix.pdf"  
    extracted_text = extract_text_from_pdf(pdf_path)  
      
    file = open("pdf_text", "w", encoding='utf-8')  
    file.write(extracted_text)



## web.pdf
In this file, we'll be looking at how we can extract all of the text from a website and use this as the prompt for our chatbot. 

Now I would like to mention that you would only need to really use one of these ways, either from a PDF or from a Website. And both ways aren't needed. 

So you can pick whichever one you prefer. In this file, let's have a look at how we could extract the text from a website. 

So let's start off by importing the required modules. In this case, it's the request module as well as bs4 or BeautifulSoup. 

Then we go ahead and find the target URL. In our case, it'll be `https://www.3ds.com/3dexperience/`. 

Then we can go ahead and send a request to our target URL, and we do this in order to retrieve the website's HTML content. After that, we ensure that we have a successful response from the website so that we know that we are good to go. 

Then we can start to parse the downloaded HTML content using BeautifulSoup. After that, we go ahead and initialize an empty variable `text`, and then we go ahead and extract all of the paragraph elements of text there is on the website. And then we store this all in the text variable. After that, we can go ahead and save this extracted text, and to do so, we have used the `web_text.txt` file, and then we just write to it. If this is successful, then we go ahead and print out our success message. 

Otherwise, if the response code will start 200, then we can print this out to see what's going wrong. So that was all the coding that we needed to do for this case. Let's go ahead and run this to see what we get for our output. As you can see here, we get the message that the text has been extracted and saved successfully in the file `web_text.txt`. 

So if I open up my folder over here and go to `web_text.txt`. we see this massive file which has all the text from our website saved into one line. 

Now that we have our text files ready, we can pick either one of these, either with the one from a PDF or the one from the website, and we can start building a chatbot.   

    # BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/  
    import requests  
    from bs4 import BeautifulSoup  
    from flask import Flask, jsonify  
    target_url = "https://www.3ds.com/3dexperience/"  
    response = requests.get(target_url)  
    if response.status_code == 200:  
        soup = BeautifulSoup(response.content, 'html.parser')  
        text = ""  
      for paragraph in soup.find_all('p'):  
            text += paragraph.get_text()  
        with open('website_text.txt', 'w') as text_file:  
            text_file.write(text)  
        print("Text extracted and saved successfully!")  
    else:  
        print(f"Error: Failed to retrieve website content. Status code: {response.status_code}")

## openai_test.py (OpenAI hello world)
In this file, we'll walk you through a basic OpenAI API architecture and show you what sort of things we can do with the API. 

So first of all, let's start off by importing the modules that we need. Of course, we need the OpenAI module from OpenAI and then initialize our client variable using the OpenAI class. 

This creates an instance of the OpenAI client, which will be used in order to interact with the OpenAI API. Then we move on to the main part of our code, and this is where we can interact with the OpenAI API.

So let me go through what's happening over here. First, I'm using the client.chat.completions.create method, and this is a method that's used in order to retrieve a completion response from the OpenAI API. Now, within this, the two parameters that I have to specify is the model and the messages parameters. So the model parameter refers to the model that I'll be using. In this case, I;ve picked `gpt-4.1-mini` because is light and I think it consume less credits. 

However, you can pick any model that you want. After that, we have to go ahead and display the messages command. Now messages is a list of different dictionaries that represents the conversation between the user and the system. 

Each dictionary has a role key, that can either be a system or the user, as well as a content key, which contains the actual message. Now, the first dictionary in the list sets the system role and provides instructions to the AI model that it should extract a list of keywords from the text that I've provided. And then the second dictionary in the list sets the user role and it contains a block of text from which the keywords should be extracted. So essentially this is the input and this is what the system will use in order to generate an output for us. 

After that, I also go ahead and mention the temperature, and I've set that to 0.5. Now, the temperature is a parameter that controls the randomness of the generated response. A higher temperature will make the output more random and more creative, while a lower temperature will make the output more focused and deterministic. 

Currently, I've set it right in the middle. And then finally we can go ahead and print out our response. The `message.content` attribute here contains the actual text of the generated response instead of everything else, this also gets generated through the API. 

So let's go ahead and run this. In this case, I have given it a text block of the first AI programs, Christopher Strachey, Programming Research Group, University of Oxford, and quite a few more. So that was it for this test file. 

All I wanted to do was to go through a quick and easy implementation of how we would use the OpenAI API. And of course, you would need to make sure that you have the OpenAI API set to as an environment variable.

    from openai import OpenAI  
    import os  
    client = OpenAI()  
    response = client.chat.completions.create(  
        model="gpt-4.1-mini",  
        messages=[  
        {  
            "role": "system",  
            "content": "You will be provided with a block of text..."  
      },  
        {  
            "role": "user",  
            "content": "The earliest successful AI program..."  
      }  
        ],  
        temperature=0.5  
    )  
    print(response.choices[0].message.content)

Remember get your OpenAI API Key here: https://platform.openai.com/docs/quickstart, and setting it up as env var if using windows. Use **OPENAI_API_KEY** as variable. You may need to make a payment to acquire credits.  

Now that we know the basic fundamental OpenAI API architecture, we can start to use LangChain, and build our fully fledged chat bot. 

## langchain_test.py (Langchain hello world)

So let's start off by, first of all, importing the modules that we'll need. 

We'll need the langchain_openai module, as well as the langchain module. 

OpenAI is the class that will be required in order to initialize the OpenAI language model, and PromptTemplate is used for creating a template for our prompt. 

After that, let's go ahead and open up the `web_text.txt` file, which is the file that has all of the extracted text from our `https://www.3ds.com/3dexperience/` website. 

Then we read all of these contents into the prompt variable. Now, we create our full prompt. This is the `assistant_template` variable, and first of all, we're given all of the text from our web_text file, and then we also give the chat bot some guidelines they have to stick to. 

In this case, I've said that it is the sales manager of Solidworks, and I've given it a name `Lang`. 

After that, I've also said that any queries that are not related to the SW, it can simply ignore. 

So now, we can go ahead and use the PromptTemplate class, and create our whole object. 

The input variables parameter specifies that the template expects one input and one input only, and this variable is named question, which will be the user's query. 

Also the template that we're using for our prompt will be the assistant template, which includes both sides of our prompt. 

After that, we go ahead and initialize the OpenAI language model. In my case, I'll be using the GPT 3.5 turbo instruct model. However, you can use any other for your application. 

I've also set the temperature parameter to zero, which means that the model will generate more deterministic and conservative responses instead of trying to be creative. 

After that, we go ahead and create the llm chain, and this is the llm chain object, which is created by combining the hotel assistant prompt template and the llm, which is our OpenAI language model. 

After that, we go ahead and create a new function. This function defines the query_llm, and this takes in the question as input, and it prints out the response that is generated by our llm chain. 

The invoke method is called on by the llm chain with a dictionary containing the user's question. After that, we add in a loop based approach in order to allow the user to ask as many questions as they want to the chat bot. 

So now, let's have a go at running this, and see how it all works. 

The chat bot should correctly replying to our answers based on all the context that we've given it, but now what happens if we ask it a question where it is not in the context? For example, what if I say, what is LangChain? And as you can see, we get a response, I can't assist you with that, sorry. 

So as you can see, we have sort of restricted our chat bot to only answer questions relating to the knowledge that we have given it, and not answer questions from outside of that knowledge. That was it for this file, that's basically our chat bot made. 


    from langchain_openai import OpenAI  
    from langchain.prompts import PromptTemplate  
      
    prompt = open('web_text.txt', 'r').read()  
      
    assistant_template = prompt + """  
    You are a sale manager of Solidworks Company, named "Mr. Lang".  
    Your expertise is exclusively in providing information and advice about anything related to 3DS products. This includes any product or service related queries. You do not provide information outside of this scope. If a question is not about 3DS, respond with, "I can't assist you with that, sorry!" Question: {question} exclusivelyAnswer: """  
      
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

Now, the only thing that is left to do is to create the user interface and the front end of the chat bot to make it into a simple web application.

## chatbot.py 
Well, now, in this file, we'll be deploying our application with the use of Flask. 

So, to do so, first of all, we'll start off by importing the required modules.

We go ahead and import the necessary components from the Flask library. 

This includes render_template in order to help render the HTML templates, request to handle any incoming requests, as well as jsonify in order to convert Python objects to JSON responses. 

Now, the next change that we've made to our code from the last lesson will be lower down. And over here, instead of now printing out our response, we will be returning our response. 

So if you just assign this to a variable of response. And then we can just go ahead and return our response. Now, I've mentioned I've also gotten rid of the loop because we don't need this loop anymore when we are building the web application. 

Now, the next bit that you'll see over here is going to be the new app variable. This creates a new Flask application instance. 

And after that, we go ahead and define our route for the root URL. And this means that when a user navigates to this URL, the index function will be called, and this renders the index.html template. 

After that, we go ahead and define a route for the /chatbot endpoint, which will accept the post request. So when a post request is sent to this endpoint, the JSON data is retrieved using the `request.get_json` command, and then the question value from the JSON data is extracted and stored in the question variable. 

After that, the `query_llm` function is called with a question, and this helps us generate a response from the LLM. 

Then the response is returned as a JSON object using `jsonify({"response": response})`. And the debug mode because the script is just executed directly. 

So let's go ahead and now run this and see what we get. So as you can see, we have deployed a development server on our local host. And now if you go to this right now, we won't actually be able to see anything because we haven't still made our index.html file. 

So in the next file, we'll go ahead and make that and complete our chatbot.

    from flask import Flask, render_template, request, jsonify  
    from langchain_openai import OpenAI  
    from langchain.prompts import PromptTemplate  
      
    prompt = open('web_text.txt', 'r').read()  
      
    assistant_template = prompt + """  
    You are a sale manager of Solidworks Company, named "Mr. Lang".  
    Your expertise is exclusively in providing information and advice about anything related to 3DS products. This includes any product or service related queries. You do not provide information outside of this scope. If a question is not about 3DS, respond with, "I can't assist you with that, sorry!" Question: {question} exclusivelyAnswer: """  
      
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



## index.html
Okay, so in this moment we'll be connecting the backend of our application that we made in last file and using the index of HTML file that we had referenced in order to create the template for our chatbot. 

However, we won't be doing anything advanced, it'll be quite a basic webpage so I would encourage you to move further and develop it if you'd like. 

    <!DOCTYPE html>  
    <html>  
    <head>  
     <title>SW Chat Assistance</title>  
     <style>  /* CSS styles for the chatbot interface */  
            #chat-container {  
                width: 400px;  
                height: 500px;  
                border: 1px solid #ccc;  
                overflow-y: scroll;  
                padding: 10px;  
            }  
      
            .message {  
                margin-bottom: 10px;  
            }  
      
            .user {  
                font-weight: bold;  
                color: blue;  
            }  
      
            .bot {  
                font-weight: bold;  
                color: green;  
            }  
        </style>  
    </head>  
    <body>  
     <h1>Solidworks Chat Assistance</h1>  
     <div id="chat-container"></div>  
     <input type="text" id="user-input" placeholder="Type your message..." />  
     <button id="send-btn">Send</button>  
     <script>  const chatContainer = document.getElementById('chat-container');  
            const userInput = document.getElementById('user-input');  
            const sendBtn = document.getElementById('send-btn');  
          
            sendBtn.addEventListener('click', sendMessage);  
              
            function sendMessage() {  
                const userMessage = userInput.value.trim();  
                if (userMessage) {  
                    displayMessage('user', userMessage);  
                    sendMessageToServer(userMessage);  
                    userInput.value = '';  
                }  
            }  
              
            function displayMessage(sender, message) {  
                const messageElement = document.createElement('div');  
                messageElement.classList.add('message');  
                messageElement.classList.add(sender);  
                messageElement.textContent = `${sender}: ${message}`;  
                chatContainer.appendChild(messageElement);  
                chatContainer.scrollTop = chatContainer.scrollHeight;  
            }  
              
            function sendMessageToServer(message) {  
                fetch('/chatbot', {  
                    method: 'POST',  
                    headers: {  
                        'Content-Type': 'application/json',  
                    },  
                    body: JSON.stringify({ question: message }),  
                })  
                .then((response) => response.json())  
                .then((data) => {  
                    displayMessage('bot', data.response);  
                })  
                .catch((error) => {  
                    console.error('Error:', error);  
                });  
            }  
        </script>  
    </body>  
    </html>


As you can see, this is a fairly simple HTML document with CSS and JavaScript that doesn't require much detail; that's not the objective of this exercise.

If everything went well, you will see a message indicating the local URL you can access to view the UI and perform the tests.

```mermaid
sequenceDiagram
User ->> Browser: Hello Chat, interacts
Browser-->>FlaskApp: HTTP POST /chatbot
FlaskApp-->>LangChain : builds prompt
LangChain-->>OpenAI : invokes LLM
OpenAI --x LangChain : response
LangChain --x FlaskApp : answer
FlaskApp --x Browser : JSON response
Browser --x User : See response, interacts
```

# Happy coding!



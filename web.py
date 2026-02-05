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
    with open('web_text.txt', 'w') as text_file:
        text_file.write(text)
    print("Text extracted and saved successfully!")
else:
    print(f"Error: Failed to retrieve website content. Status code: {response.status_code}")

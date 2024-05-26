
from flask import Blueprint, render_template, request, jsonify
from openai import OpenAI
from config import Config
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate_idea():
    user_input = request.form['user_input']
    
    client = OpenAI(api_key=Config.OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que gera ideias inovadoras de startups."},
            {"role": "user", "content": f"Proponha uma ideia inovadora de startup baseada no seguinte input: {user_input}"}
        ],
        max_tokens=150
    )
    idea = response.choices[0].message.content.strip()
    print(idea)
    print(response)
    return jsonify({"idea": idea})

    
  
    


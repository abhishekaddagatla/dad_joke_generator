from flask import Flask,jsonify,request
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/')
def dad_joke():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="tell me a dad joke",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    joke = response.choices[0].text.strip()
    return jsonify(joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,jsonify,request
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/')
def dad_joke():
    topic = request.args.get('topic','')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"tell me a dad joke {topic}.",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    joke = response.choices[0].text.strip()
    return {"joke":joke}

if __name__ == '__main__':
    app.run(debug=True)
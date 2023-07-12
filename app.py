from flask import Flask,jsonify,request, render_template
import openai
import os

from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/generate_joke', methods=['POST'])
def generate_joke():
    print(request.form)
    query = request.form.get("query")
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"tell me a new dad joke about {query}.",
        temperature=0.8,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    joke = response.choices[0].text.strip()
    return {"joke":joke}
    #api call to get the joke with query, return the joke in json

@app.route('/')
def dad_joke():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
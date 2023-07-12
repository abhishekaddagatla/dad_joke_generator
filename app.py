from flask import Flask,jsonify,request, render_template
import openai
import os

# from dotenv import load_dotenv

app = Flask(__name__)

# load_dotenv()
openai.api_key = "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"


@app.route('/')
def dad_joke():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
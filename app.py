from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = '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'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/message', methods=['POST'])
def message():
    user_message = request.form['message']
    response = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"{user_message}"
            }
        ]
    )
    response_message = response['choices'][0]['message']['content']
    return jsonify({'message': response_message})

if __name__ == "__main__":
    app.run(debug=True)

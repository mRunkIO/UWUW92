# This code assumes you have set up a backend server using a framework like Flask

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configure OpenAI API credentials
openai.api_key = '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'

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data['question']
    school_marks = data['school_marks']

    # Call the OpenAI ChatGPT API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        log_level='info',
        log_probas=0.8,
        logit_bias={'school_marks': school_marks}
    )

    answer = response.choices[0].text.strip()

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run()

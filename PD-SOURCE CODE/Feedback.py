import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/feedback', methods=['POST'])
def process_feedback():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']

    # Do something with the feedback data, such as saving to a database

    return "Thank you for your feedback, {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)
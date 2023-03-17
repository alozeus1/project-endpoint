from flask import Flask

app = Flask(__name__)

@app.route('/words', methods=['GET'])
def get_words():
    return 'Hello, world!'

if __name__== '__name__':
    app.run(host='127.0.0.1', port=8080)
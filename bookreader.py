from flask import Flask
from flask_ask import Ask, statement, question
import urllib

app = Flask(__name__)
ask = Ask(app, "/book_reader")


def get_book_text():
    try:
        # The Time Machine, by H. G. Wells [1898]
        target_url = 'http://www.gutenberg.org/cache/epub/35/pg35.txt'
        txt = " ".join(urllib.urlopen(target_url).readlines()[20:50])
    except Exception as e:
        txt = str(e)
    # print txt
    return txt


@app.route("/")
def homepage():
    return "hi there, how are you doing?"


@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like to read you your book?'
    return question(welcome_message)


@ask.intent("YesIntent")
def read_book():
    print "Fetch book"
    text = get_book_text()
    message = "Reading book: " + text
    return statement(message)


@ask.intent("NoIntent")
def no_intent():
    bye_text = "I am not sure why you asked me to run, but okay....bye"
    return statement(bye_text)


@ask.intent("CancelIntent")
def cancel_intent():
    bye_text = "See you next time. Alexa Rocks!!"
    return statement(bye_text)


@ask.intent("StopIntent")
def stop_intent():
    bye_text = "See you next time!!"
    return statement(bye_text)


if __name__ == "__main__":
     app.run(debug=True)

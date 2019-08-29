from flask import Flask, request, jsonify
import re
import unidecode
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def homepage():

    return """
        <h1>Welcome to Cannjoin Server</h1>
        <p>Try our sentiment analysis by using the endpoint /commentanalysis and provide a JSON body with a feild raw_comment. You can also enjoy these cats :)</p>

        <img src="http://loremflickr.com/600/400">
        """.format(time="Today")


@app.route("/commentanalysis", methods=['POST'])
def commentanalysis():

    data = request.json
    raw_comment = data['raw_comment']
    clean_comment = apply_basic_cleaning(raw_comment)
    
    sentiment = TextBlob(clean_comment).sentiment
    
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    data = {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "raw_comment": raw_comment,
        "clean_comment": clean_comment
    }

    return data

# Here were going to add the preprocessing functions that gave best results

def remove_html_tags(sentence):
    return re.sub(re.compile('<.*?>'), '', str(sentence))

def remove_URLS(sentence):
    return re.sub(re.compile('http\S+|www\.\S+'), '', str(sentence))

def remove_breaks(sentence):
    return re.sub(re.compile('\n|\r|\t'), '', str(sentence))

def remove_unicode(sentence):
    return unidecode.unidecode(str(sentence))

def remove_numbers(sentence):
    return re.sub(re.compile('\d+'), '', str(sentence))

def lower_case(sentence):
    return str(sentence).lower()

def remove_punctuation(sentence):
    return re.sub(re.compile('[^\w\s]'), '', str(sentence))

# Put it all together (Order is important)
def apply_basic_cleaning(sentence):
    iteration_one = remove_html_tags(sentence)
    iteration_two = remove_URLS(iteration_one)
    iteration_three = remove_breaks(iteration_two)
    iteration_four = remove_numbers(iteration_three)
    iteration_five = lower_case(iteration_four)
    
    return remove_punctuation(iteration_five)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

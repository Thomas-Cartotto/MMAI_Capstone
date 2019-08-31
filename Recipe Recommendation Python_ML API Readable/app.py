from flask import Flask, request, jsonify
from CannjoinML.NLP import cannjoin_nlp
from CannjoinML.Classifier import cannjoin_xgboost


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

    nlp_processor = cannjoin_nlp()
    return nlp_processor.getNLPFeatures(raw_comment)

@app.route("/classify", methods=['POST'])
def classify():
    
    data = request.json
    raw_json = data['request_data']
    
    xgboost_processor = cannjoin_xgboost()
    return xgboost_processor.classifyReview(raw_json)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

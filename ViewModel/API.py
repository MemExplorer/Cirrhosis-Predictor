#!python

import cgi
import json
import os.path
import sys
import base64
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)

import Model.QuizManager as qm
from Model.NaiveBayes.NaiveBayesClassifier import NaiveBayesClassifier

# Initialize globals
quizInstance = qm.Quiz(r"..\Resources\raw\questions.json")
model = NaiveBayesClassifier.load_from_model(r"..\model.pickle")

# Content type
print("Content-Type: application/json\n")

def craft_request(data, state=True):
    return {"success" : state, "data": data}

# sample usage: API.py?type=fetch&index=1
def handle_fetch(form):
    global quizInstance
    page_num = int(form.getvalue("index"))
    response = quizInstance.get_question_from_index(page_num)
    encoded_response = json.dumps(craft_request(response.__dict__))
    print(encoded_response)

# sample usage: API.py?type=result&data=[base64 json]
def handle_result(form):
    global quizInstance
    global model
    data = form.getvalue("response_data")
    decoded_response = base64.b64decode(data.replace("-", "+").replace("_", "/"))
    deserialized_response = json.loads(decoded_response)
    
    pred_code = model.predict(deserialized_response)
    pred_full_result = {"result": quizInstance._prediction_mapping[pred_code]}
    encoded_response = json.dumps(craft_request(pred_full_result))
    print(encoded_response)


def handle_default(form):
    encoded_response = json.dumps(craft_request("Invalid request!", False))
    print(encoded_response)

post_form = cgi.FieldStorage()
request_type = post_form.getvalue("type")

try:
    match request_type:
        case "fetch":
            handle_fetch(post_form)
        case "result":
            handle_result(post_form)
        case _:
            handle_default(post_form)
except:
    handle_default(post_form)


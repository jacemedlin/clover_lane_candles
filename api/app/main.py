from flask import Flask, jsonify
import requests
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route("/")
def hello():
    import pymongo

    mongoclient = pymongo.MongoClient(
        "mongodb://db:27017/",
        username="root",
        password="example",
        connect=False
    )
    print(mongoclient.list_database_names())

@app.route("/test/")
def t_dawg_is_back_again():
    # requests.get("http://db:8081/")
    return jsonify({"T-Dawg is back again": "and I've brought a new hit with me, boys."})

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
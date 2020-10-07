import argparse, json
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/webhock", methods=["POST"])
def listen_to_hock():
    print(request.json)
    f = open("dump.json", request.json)
    f.close()
    return Response(status=200)




if __name__ == "__main__":
    app.run(debug=True)
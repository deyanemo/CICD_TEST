import argparse
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/webhock", methods=["POST"])
def listen_to_hock():
    print(request.json);
    return Response(status=200)




if __name__ == "__main__":
    app.run(debug=True)
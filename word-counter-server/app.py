from time import sleep

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/analyse', methods=["GET"])
def analysing():
    args = request.args
    sleep(2)
    return {
        "videoTitle": "The enduring mystery of Jack the Ripper",
        "videoId": args['videoId'],
        "lang": args["lang"],
        "results": [
            {"word": "the", "count": 100},
            {"word": "be", "count": 99},
            {"word": "to", "count": 98},
            {"word": "of", "count": 97},
            {"word": "and", "count": 96},
            {"word": "a", "count": 95},
            {"word": "in", "count": 94},
            {"word": "that", "count": 93},
            {"word": "have", "count": 92},
            {"word": "I", "count": 91},
            {"word": "it", "count": 90},
            {"word": "for", "count": 89},
            {"word": "not", "count": 88},
            {"word": "on", "count": 87},
            {"word": "he", "count": 86},
            {"word": "as", "count": 85},
            {"word": "you", "count": 84},
            {"word": "do", "count": 83},
            {"word": "are", "count": 82},
            {"word": "we", "count": 81},
            {"word": "his", "count": 80},
            {"word": "with", "count": 79},
            {"word": "by", "count": 78},
            {"word": "at", "count": 77},
            {"word": "or", "count": 76},
            {"word": "this", "count": 75},
            {"word": "but", "count": 74},
            {"word": "from", "count": 73},
            {"word": "they", "count": 72},
            {"word": "her", "count": 71},
            {"word": "which", "count": 70},
            {"word": "or", "count": 69},
            {"word": "she", "count": 68},
            {"word": "an", "count": 67},
            {"word": "will", "count": 66}
        ]
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)

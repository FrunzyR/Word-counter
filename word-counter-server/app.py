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
        "videoId": args['videoId'],
        "lang": args["lang"],
        "results": {
            "the": 100,
            "be": 99,
            "to": 98,
            "of": 97,
            "and": 96,
            "a": 95,
            "in": 94,
            "that": 93,
            "have": 92,
            "I": 91,
            "it": 90,
            "for": 89,
            "not": 88,
            "on": 87,
            "he": 86,
            "as": 85,
            "you": 84,
            "do": 83,
            "are": 82,
            "we": 81,
            "his": 80,
            "with": 79,
            "by": 78,
            "at": 77,
            "or": 76,
            "this": 75,
            "but": 74,
            "from": 73,
            "they": 72,
            "her": 71,
            "she": 68,
            "an": 67,
            "will": 66,
            "my": 65,
            "one": 64,
            "all": 63,
            "would": 62,
            "there": 61,
            "their": 60,
            "what": 59,
            "so": 58,
            "up": 57,
            "out": 56,
            "if": 55,
            "about": 54,
            "who": 53,
            "get": 52,
            "which": 51,
            "go": 50,
            "me": 49,
            "when": 48,
            "make": 47,
            "can": 46,
            "like": 45,
            "time": 44,
            "no": 43,
            "just": 42,
            "him": 41,
            "know": 40,
            "take": 39,
            "people": 38,
            "into": 37,
            "year": 36,
            "your": 35,
            "good": 34,
            "some": 33,
            "could": 32,
            "them": 31,
            "see": 30,
            "other": 29,
            "than": 28,
            "then": 27,
            "now": 26,
            "look": 25,
            "only": 24,
            "come": 23,
            "its": 22,
            "over": 21,
            "think": 20,
            "also": 19,
            "back": 18,
            "after": 17,
            "use": 16,
            "two": 15,
            "how": 14,
            "our": 13,
            "work": 12,
            "first": 11,
            "well": 10,
            "way": 9,
            "even": 8,
            "new": 7,
            "want": 6,
            "because": 5,
            "any": 4,
            "these": 3,
            "give": 2,
            "day": 1
        }
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)

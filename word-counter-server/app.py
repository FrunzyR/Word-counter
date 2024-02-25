from time import sleep

from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/analyse', methods=["GET"])
def analysing():
    args = request.args
    srt = YouTubeTranscriptApi.get_transcript(args['videoId'], languages=['en'])
    full_srt = ""
    results = []
    count = {}
    for element in srt:
        full_srt += element["text"]\
            .replace("\n", " ")\
            .replace(",", " ")\
            .replace(".", " ")\
            .replace(":", " ")\
            .replace('"', "")\
            .replace("-", " ")\
            .replace("[", " ")\
            .replace("]", " ")

    print(full_srt.split())

    for word in full_srt.lower().split():
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word] = 1
    sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    for entry in sorted_dict.items():
        results.append({"word": entry[0], "count": entry[1]})
    print(results)

    return {
        "videoTitle": "The enduring mystery of Jack the Ripper",
        "videoId": args['videoId'],
        "lang": args["lang"],
        "results": results,
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)

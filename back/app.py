from flask import Flask
from flask_cors import CORS
import openai

app = Flask(__name__)

CORS(app)

openai.api_key = "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"


@app.route("/")
def index(methods=["GET", "POST"]):
    mymsg = "hi"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": mymsg},
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message.content


@app.route("/flist")
def index(methods=["GET", "POST"]):
    List = [
        {"name1": "info"},
        {"name2": "info"},
        {"name3": "info"},
    ]
    ## 이걸 vue에 전달해서 MyFriend.vue에 적용


if __name__ == "__main__":
    app.run(debug=True)

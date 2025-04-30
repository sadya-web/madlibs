from flask import Flask, render_template, request

app = Flask(__name__)

# Only 20 words — but we’ll use them A LOT and make it super funny
word_types = [
    "silly name", "adjective", "funny animal", "verb ending in -ing", "body part", 
    "gross food", "sound effect", "weird object", "place", "clothing item", 
    "emotion", "color", "plural noun", "celebrity", "smelly thing", 
    "something sticky", "yummy food", "number", "ridiculous word", "big object"
]

@app.route("/", methods=["GET", "POST"])
def madlibs():
    if request.method == "POST":
        words = [request.form.get(f'word{i}') for i in range(20)]

        story = f"""
        One fine day, {words[0]}, the {words[1]} {words[2]}, was {words[3]} down the sidewalk while scratching their {words[4]}.
        Suddenly, a wild plate of {words[5]} flew out of nowhere, shouting “{words[6].upper()}!” and landing on a {words[7]}.
        Everyone in {words[8]} ran out wearing {words[9]}s, screaming with pure {words[10]} as a {words[11]} fog filled the sky.
        Out of the fog came 87 {words[12]} riding skateboards, all chanting “{words[19]} or bust!” in perfect harmony.
        Just when you thought it couldn’t get weirder, {words[13]} appeared, sneezing into a pile of {words[14]} and juggling {words[15]}.
        “Who wants some {words[16]}?!” they yelled, flinging it like frisbees. 
        {words[0]} caught exactly {words[17]} of them with their {words[4]} and shouted, “{words[18]} forever!”
        And that, my friends, is why you should never trust a {words[1]} {words[2]} with a suitcase full of {words[5]}.
        """

        return render_template("result.html", story=story)

    return render_template("form.html", word_types=word_types)

if __name__ == "__main__":
    app.run(debug=True)

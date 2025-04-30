from flask import Flask, render_template, request

app = Flask(__name__)

# List of 100 parts of speech or types of words
word_types = [
    "adjective", "noun", "verb ending in -ing", "place", "animal", "color", "plural noun", "funny word",
    "past-tense verb", "type of weather", "body part", "adjective", "noun", "verb", "emotion", "number",
    "silly sound", "object", "verb ending in -ed", "adverb", "insect", "liquid", "celebrity", "holiday",
    "fruit", "vegetable", "toy", "clothing item", "dessert", "plant", "magical creature", "adjective",
    "shape", "building", "type of tree", "adjective", "tool", "mode of transportation", "game", "book title",
    "song title", "movie title", "website", "junk food", "cleaning product", "part of a house", "fabric",
    "number", "adjective", "plural body part", "material", "type of dance", "emotion", "slang word",
    "brand name", "animal sound", "type of candy", "fabric pattern", "nickname", "furniture", "mythical creature",
    "verb", "past-tense verb", "sport", "magical object", "room in a house", "type of flower", "type of shoe",
    "direction", "school subject", "adjective", "type of music", "job", "name", "celebrity", "historical figure",
    "verb", "plural noun", "measurement", "device", "liquid", "object", "exclamation", "invention",
    "scientific term", "store name", "tool", "beverage", "emotion", "verb", "animal", "season",
    "plural profession", "type of chair", "precious stone", "body part", "vegetable", "unit of time",
    "game", "part of a tree", "number", "adjective"
]

@app.route("/", methods=["GET", "POST"])
def madlibs():
    if request.method == "POST":
        words = [request.form.get(f'word{i}') for i in range(100)]

        # Build the funny, spring-themed story
        story = f"""
        On a {words[0]} spring morning in {words[3]}, a {words[4]} wearing {words[27]} {words[5]} shoes was {words[2]} across a field of {words[65]}s.
        Suddenly, it shouted, "{words[7]}!" and threw a {words[12]} at a group of {words[6]} {words[1]}s.
        The sky turned {words[5]}, and it began to rain {words[6]} made of {words[21]}.
        I grabbed my {words[17]} and ran inside the {words[33]}, tripping over a {words[30]} on my way.
        Inside, my {words[70]} was dancing to {words[39]}, while a {words[59]} {words[4]} made {words[28]} using a {words[37]}.
        We {words[13]}ed and laughed until {words[15]} {words[3]} unicorns flew by wearing {words[47]} suits, throwing {words[55]} at each other.
        "{words[79]}!" I yelled, spilling my {words[85]} all over the {words[92]}.
        It was chaos — the {words[60]} screamed, the {words[82]} broke, and even the {words[29]} looked shocked.
        Just when things couldn’t get weirder, a {words[61]} floated in on a cloud of {words[90]} and gave everyone a hug.
        We ended the day by planting {words[64]}s in the {words[66]}, singing {words[40]}, and promising to never {words[74]} on a {words[99]} spring day again.
        The end.
        """

        return render_template("result.html", story=story)

    return render_template("form.html", word_types=word_types)

if __name__ == "__main__":
    app.run(debug=True)

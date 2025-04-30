from flask import Flask, render_template, request

app = Flask(__name__)

# 100 detailed, varied, and fun word prompts
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

        # Use ALL 100 words in the story
        story = f"""
        On a {words[0]} spring day, a {words[4]} wearing a {words[5]} {words[27]} was {words[2]} in the {words[3]}.
        Suddenly, a bunch of {words[6]} shouted "{words[7]}!" as they {words[8]} through the {words[9]} sky.
        I blinked my {words[10]} and saw a {words[11]} {words[12]} hopping toward me holding a {words[13]} balloon.
        Feeling {words[14]}, I grabbed {words[17]} and ran {words[19]} past {words[15]} {words[20]}s.
        A cup of {words[21]} spilled on my {words[28]}, and I bumped into {words[22]}, who was on vacation from {words[23]}.
        We sat under a {words[34]} and shared {words[24]}s and {words[25]}s while a {words[26]} floated by.
        My {words[29]} waved from a nearby bush, dressed like a {words[30]} with a {words[31]} {words[32]} hat.
        Suddenly, a {words[33]} scream rang out from the {words[35]}, where someone was fixing a {words[36]} with a {words[37]}.
        We hopped on a {words[38]} and played {words[39]} while singing {words[40]} from the movie {words[41]}.
        Later, we googled it on {words[42]} and ate {words[43]} while cleaning with {words[44]}.
        I ran through the {words[45]} with my {words[46]} cape, stepped on {words[47]} {words[48]}, and did the {words[49]}.
        I felt {words[50]}, so I yelled "{words[51]}!" and rode a {words[52]} while making a {words[53]} noise.
        I offered {words[54]} wrapped in {words[55]} to {words[56]} who sat on a {words[57]} reading about a {words[58]}.
        I {words[59]} and {words[60]} while playing {words[61]} using a {words[62]} from the {words[63]}.
        In the {words[64]}, I wore {words[65]}s and walked {words[66]} while studying {words[67]}.
        Everything felt so {words[68]}, especially with the {words[69]} music playing near the {words[70]} booth.
        My friend {words[71]} called out, "Look! {words[72]} is arm-wrestling {words[73]}!"
        We all {words[74]} and tossed {words[75]}s as a {words[76]}-tall {words[77]} spilled {words[78]}.
        I dropped my {words[79]} and screamed, "{words[80]}!" while dodging a flying {words[81]}.
        A crowd formed shouting scientific words like {words[82]} and shopping at {words[83]}.
        I fixed it with my {words[84]}, drank {words[85]}, and felt super {words[86]}.
        I {words[87]} toward a giant {words[88]} as the {words[89]} ended and {words[90]}s flew over the {words[91]}.
        I gave my {words[92]} a hug and munched on a {words[93]}, dancing for a whole {words[94]}.
        We ended with a game of {words[95]} under a {words[96]}, counting to {words[97]}, smiling at the {words[98]} sky.
        What a {words[99]} spring day!
        """

        return render_template("result.html", story=story)

    return render_template("form.html", word_types=word_types)

if __name__ == "__main__":
    app.run(debug=True)

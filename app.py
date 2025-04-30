from flask import Flask, render_template, request

app = Flask(__name__)

# List of 100 word prompts
word_types = [
    "noun", "adjective", "verb", "place", "silly word", "animal", "food", "emotion", "color", "body part",
    "verb ending in -ing", "plural noun", "number", "celebrity", "object", "sound", "adjective", "vehicle",
    "fruit", "vegetable", "occupation", "past-tense verb", "drink", "planet", "famous person", "exclamation",
    "type of weather", "clothing item", "adverb", "shape", "country", "liquid", "tool", "sport", "game",
    "school subject", "type of music", "relative", "type of candy", "part of a house", "insect",
    "furniture", "website", "language", "dessert", "toy", "movie title", "book title", "store name",
    "type of shoe", "song title", "holiday", "city", "mythical creature", "smell", "sound effect", "emotion",
    "spice", "measurement", "body part (plural)", "nickname", "fabric", "color", "cleaning product", "magical object",
    "name", "disease", "slang word", "brand name", "magazine title", "cereal name", "board game", "tree type",
    "junk food", "month", "day of the week", "building type", "type of dance", "flower", "precious stone", "gem",
    "type of cheese", "internet slang", "loud noise", "awkward phrase", "flavor", "season", "sea creature", "bird",
    "famous landmark", "type of bug", "funny phrase", "emotion", "hairstyle", "kitchen item", "emoji name",
    "superhero name", "video game", "dog breed", "cat breed", "body function", "bad habit", "magic spell"
]

@app.route('/', methods=['GET', 'POST'])
def madlibs():
    if request.method == 'POST':
        words = [request.form.get(f'word{i}') for i in range(100)]

        # Insert the words into your chaotic story template
        story = f"""
        It was a {words[1]} day in {words[3]}. Suddenly, a {words[0]} exploded next to a {words[4]} {words[5]}.
        Everyone started {words[10]} while eating {words[6]} and yelling, "{words[25]}!"
        {words[13]} arrived riding a {words[17]} full of {words[11]}.

        "This is more dramatic than {words[47]} meets {words[48]} at {words[49]}!" someone screamed.

        A {words[27]} storm blew in, covering everyone in {words[31]} and soggy {words[13]} shirts.
        "Quick!" yelled {words[12]} monkeys. "We must {words[2]} to the {words[73]} while wearing {words[26]} hats!"

        Then {words[70]} squirrels began {words[10]} around a glowing {words[63]} chanting, "{words[4]}! {words[4]}!"

        Meanwhile, {words[95]} cast {words[99]} on a {words[80]} filled with {words[83]} and {words[90]}. Chaos.

        Suddenly, {words[59]} burst from the sky wearing {words[65]} pants and holding {words[60]} {words[32]}s.

        A nearby {words[85]} began quoting {words[47]} backwards, then threw {words[84]} into the {words[29]} and yelled, "{words[89].upper()}!"

        Then, silence.

        Everyone stared at the {words[16]} {words[13]} who simply said, "{words[98]}."

        It was the {words[75]} of all {words[74]}s.

        THE END.
        """
        return render_template('result.html', story=story)

    return render_template('form.html', word_types=word_types)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


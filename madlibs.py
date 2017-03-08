from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/madlibs')
def show_madlib():
    """Greet user."""

    madlib_name = request.args.get("human")

    madlib_color = request.args.get("color")

    madlib_adj = request.args.get("adjective")

    madlib_noun = request.args.get("noun")


    return render_template("madlibs.html", human=madlib_name, color=madlib_color, adjective=madlib_adj, noun=madlib_noun,)


@app.route('/game')
def show_madlib_form():
    """madlib form."""

    selected_game = request.args.get("game-choice")

    if selected_game == "Yes!":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

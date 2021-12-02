from stories import stories
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = flask(__name__)
app.config ['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension

@app.route("/")
def ask_question():
    """Generate form to input words"""

    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

#once creating the form we can create a route to input that into story.py

@app.route("/story")
def fill_story():
    """Generate Final Story"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)


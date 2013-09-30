from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

templates = ['story.html'] #add file names of html templates from which to pick
nouns = ['block', 'guitar', "Mr. Zamansky's beard", "Mr. Brown's hair", "golf club", "golf ball"]
tverbs = ['ran', 'walked', 'swam', 'floated', 'flew', 'escaped', 'hopped', 'skipped'] #verbs to do with moving
names = ['Mr. Zamansky', 'Mr. Brown', 'Mr. Brooks', 'Mr. DW', 'Mr. K', 'Mr. Platek', 'Thluffy']
places = ['Stuyvesant High School', 'TriBeCa', 'chez Hunter', 'the International Space Station', 'Atlantis']
adjectives = ['happy', 'sad', 'angry', 'confused', 'blue', 'chartreuse', 'perplexed', 'holy']

words = {'nouns':nouns, 'tverbs':tverbs, 'names':names, 'places':places, 'adjectives':adjectives}

def shuffle_words():
    for list in words.itervalues():
        random.shuffle(list)
       

@app.route("/")
def home():
    shuffle_words()
    return render_template(random.choice(templates), d=words)

if (__name__ == "__main__"):
    app.debug = True
    app.run("0.0.0.0")



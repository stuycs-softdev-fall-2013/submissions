from flask import Flask
from flask import render_template

import random

madlibs = Flask(__name__)

template="""
<h1>Well here you go</h1>

<p>%(name1)s decided to %(adverb1)s %(verb1)s to the %(place1)s with %(name2)s. They were going there to get a %(thing1)s. After getting said %(thing1)s, the two of them went to the %(place2)s in order to have %(name2)s %(adverb2)s help %(name1)s with %(name1)s's %(thing2)s problem.</p>
"""




@madlibs.route("/")
def site():
    verb_list=['jump','walk','slide','skate']
    name_list=['Bob','Jane']
    thing_list=['bat','sandwich','gold bar','poster','clip','shoe']
    adverb_list=['quickly','arduously','sexily']
    place_list=["park",'library','store','arcade','basement','pool','sandbox']
    
    
    d={'name1':name_list.pop(int(random.random()*len(name_list))),
       'verb1':verb_list.pop(int(random.random()*len(verb_list))),
       'thing1':thing_list.pop(int(random.random()*len(thing_list))),
       'adverb1':adverb_list.pop(int(random.random()*len(adverb_list))),
       'place1':place_list.pop(int(random.random()*len(place_list))),
       'name2':name_list.pop(int(random.random()*len(name_list))),
       'thing2':thing_list.pop(int(random.random()*len(thing_list))),
       'adverb2':adverb_list.pop(int(random.random()*len(adverb_list))),
       'place2':place_list.pop(int(random.random()*len(place_list)))
    }
    return template%(d)

if __name__=="__main__":
    madlibs.debug=True
    madlibs.run(host="0.0.0.0",port=5005)

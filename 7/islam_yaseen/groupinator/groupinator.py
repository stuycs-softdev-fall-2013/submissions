from flask import Flask
import random

groupinator=Flask(__name__)

lines = open("students").readlines()
newlines = []
for l in lines: newlines.append(l.strip())
#list containing 'section,period,last,first'
newerlines=[]
for i in newlines:newerlines.append(i.split(","))
#list of lists containing [section, period, last, first]




@groupinator.route("/")
def groups():
    listofpd6names=[]
    for i in newerlines:
        if i[1]=='6':
            listofpd6names.append(i[2]+', '+i[3])


    listofpd7names=[]
    for j in newerlines:
        if j[1]=='7':
            listofpd7names.append(j[2]+', '+j[3])
    
    results6=""
    localpd6=listofpd6names
    for i in range(1,9):
        results6+='<li>Group '+str(i)+':<ul>'
        for j in range(0,4):
            results6+='<li>'+localpd6.pop(int(random.random()*len(localpd6)))+'</li>'
        results6+='</ul></li>'
    results7=""
    localpd7=listofpd7names
    for i in range(9,17):
        results7+='<li>Group '+str(i)+':<ul>'
        for j in range(0,4):
            results7+='<li>'+localpd7.pop(int(random.random()*len(localpd7)))+'</li>'
        results7+='</ul></li>'
    return """
<h1>Created by Brian Chuk and Yaseen Islam</h1>
<h2>Period 6</h2>
<ul>%s</ul>
<h2>Period 7</h2>
<ul>%s</ul>
"""%(results6,results7)


if __name__=="__main__":
    groupinator.debug=True
    groupinator.run(host="0.0.0.0",port=5005)
    

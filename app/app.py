from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
import urllib2
import operator
from itertools import islice


@app.route("/")
def index():
    return render_template('index.html');
   
@app.route("/get", methods=['POST']) 
def get():
    text = request.form['number']
    text = int(text)
    response = urllib2.urlopen('http://terriblytinytales.com/testapi?rollnumber=123')
    html = response.read()
    rollnumbers = html.split()  
    for roll in rollnumbers:
        if roll not in rollnumbers:
            text="fail" 
        text="pass"
    
    message =text
    
    return render_template('index.html',message=message)
 
if __name__ == "__main__":
    app.run()
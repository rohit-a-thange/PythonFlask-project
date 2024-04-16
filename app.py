## Create a simple flask application

from flask import Flask, render_template, request, redirect, url_for

## Create flask app

app = Flask(__name__) # Entry point of the program

# default homepage
# app.route assigns different urls (mention in parenthesis: url)
@app.route("/") # / is home page
def home():
    return "<h1>Hello, World!</h1>"

@app.route("/welcome")
def welcome():
    return "Welcome to Flask tutorial"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    return "The score is "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is "+str(score)

@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths+science+history)/3

        # results = ""
        # if average_marks>=35:
        #     result = "success"
        # else:
        #     result = "fail"

        # return redirect(url_for(result,score=average_marks)) # this helps to route within the code
    
        #To direct the result to an html page remove above results and if statements and return redirect statement
        
        return render_template("result.html", results = average_marks)

if __name__ == "__main__":
    app.run(debug=True)
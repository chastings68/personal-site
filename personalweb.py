'''Personal webpage'''
from flask import Flask, render_template
app = Flask(__name__) #Flask class
@app.route("/", methods=['GET','POST'])
def welcome():
    '''landing page where user can go to different pages'''
    # Have to build out other html's before I create nav link's
    # render must remember title = 'Welcome Page'
    return render_template('welcome.html')
@app.route("/resume")
def resume():
    '''Route to resume'''
    return render_template("resume.html")
@app.route("/about")
def about():
    '''about page'''
    return render_template("about.html")
@app.route("/contact")
def contact():
    '''contact page'''
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

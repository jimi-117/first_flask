from flask import Flask, render_template, request


app = Flask(__name__)

@ app.route("/")
def home():
    return "Welcome to my first flask app home !"

@ app.route("/simpleform", methods=["GET", "POST"])
def simple_form():
    if request.method == "GET":
        return render_template("sample_form.html")
    if request.method == "POST":
        print("data received. processing ...")
        data = request.form
        print(data)
    
    return render_template("sample_form.html")

if __name__ == "__main__":
    app.run(debug=True)
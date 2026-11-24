from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    name = ""
    error = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name:
            error = "Please enter your name."

    return render_template("index.html", name=name, error=error)


if __name__ == "__main__":
    app.run(debug=True)
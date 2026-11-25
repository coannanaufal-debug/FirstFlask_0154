from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            return render_template("greet.html", error="Masukkan nama kamu terlebih dahulu.")
        return render_template("greet.html", name=name)

    return render_template("index.html")


@app.route("/square/<int:n>")
def square(n):
    return str(n * n)


if __name__ == "__main__":
    app.run(debug=True)
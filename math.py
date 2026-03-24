from flask import Flask, request, render_template

app = Flask(__name__)

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]
        result = calculate(a, b, op)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
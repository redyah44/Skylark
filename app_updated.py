from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy flight data
flights = [
    {"id": 1, "from": "Addis Ababa", "to": "Dubai", "price": 56000},
    {"id": 2, "from": "Addis Ababa", "to": "Nairobi", "price": 45000}
]

@app.route("/")
def home():
    return render_template("index.html", flights=flights)

@app.route("/book/<int:flight_id>")
def book(flight_id):
    flight = next((f for f in flights if f["id"] == flight_id), None)
    return render_template("payment.html", flight=flight)

@app.route("/payment", methods=["POST"])
def payment():
    name = request.form["name"]
    phone = request.form["phone"]
    flight_id = int(request.form["flight_id"])
    return render_template("success.html", name=name, phone=phone)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
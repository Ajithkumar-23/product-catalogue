from flask import Flask
import os

app = Flask(__name__)

PRODUCTS = [
    {
        "name": "Laptop",
        "description": "Intel i7, 16GB RAM",
        "price": "₹75,000"
    },
    {
        "name": "Mobile",
        "description": "Android 5G Phone",
        "price": "₹25,000"
    },
    {
        "name": "Headphones",
        "description": "Wireless Bluetooth",
        "price": "₹3,000"
    }
]

@app.route("/")
def home():

    title = os.getenv("APP_TITLE", "Product Catalogue")

    html = f"<h1>{title}</h1>"

    html += "<table border='1' cellpadding='10'>"
    html += "<tr><th>Name</th><th>Description</th><th>Price</th></tr>"

    for p in PRODUCTS:
        html += f"<tr><td>{p['name']}</td><td>{p['description']}</td><td>{p['price']}</td></tr>"

    html += "</table>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template
import random
import os

app = Flask(__name__)

functions = [
    "Library", "Power Plant", "Train Station", "Observatory", "School",
    "Market Hall", "Water Tower", "Shrine", "Data Center", "Kindergarten"
]

styles = [
    "Brutalism", "Gothic", "Baroque", "Art Deco", "Japanese Metabolism",
    "Neo-futurism", "Khmer Temple", "Incan Fortress", "Nordic Vernacular",
    "Byzantine Basilica"
]

materials = [
    "Glass", "Mycelium", "Concrete", "Black Volcanic Stone", "Carbon Fiber",
    "Sugar Glass", "Recycled Plastic", "Polished Marble", "Organic Ceramic",
    "Algae-based BioBrick"
]

@app.route("/")
def index():
    func = random.choice(functions)
    style = random.choice(styles)
    material = random.choice(materials)
    return render_template("index.html", func=func, style=style, material=material)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

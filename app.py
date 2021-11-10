"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


# serialize data for json
def serialize_cupcake(cupcake):
    """Serialize a dessert SQLAlchemy obj to dictionary."""

	return
		{"id": cupcake.id,
		"flavor": cupcake.flavor,
		"sizes": cupcake.sizes,
		"rating": cupcake.rating,
		"image": cupcake.image}


@app.route("/api/cupcakes")
def list_all_cupcakes():
    """Return list of all cupcakes"""

	cupcakes = Cupcake.query.all()
	serialized = [serialize_cupcake(c) for c in cupcakes]
	return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<cupcake_id>")
def list_single_cupcake(cupcake_id):

 	cupcake = Cupcake.query.get(cupcake_id)

	serialized = serialize_cupcake(cupcake)
	return jsonify(cupcake=serialized)


@app.route("/api/cupcakes", methodS=["POST"])
def create_cupcake():
    """Create a cupcake"""

    flavor = request.json["flavor"]
    sizes = request.json["sizes"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, sizes=sizes, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)

    return jsonify(cupcake=serialized)

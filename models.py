"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"


class Cupcake(db.Model):
    """Cupcakes"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def serialize(self):
        """return a dict representation of todo which we can turn in json"""
        s = self
        return {
            "id": s.id,
            "flavor": s.flavor,
            "size": s.size,
            "rating": s.rating,
            "image": s.image,
        }


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    return app

from game import db
from datetime import datetime


class Inventory(db.Model):
    __tablename__ = 'inventories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('InventoryItem', backref='inventory', lazy=True)

    def __repr__(self):
        return f"<Inventory {self.id}>"


class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    rarity = db.Column(db.String(20), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=1)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "rarity": self.rarity,
            "count": self.count,
        }

    @staticmethod
    def from_dict(data):
        return InventoryItem(
            name=data["name"],
            type=data["type"],
            rarity=data["rarity"],
            count=data["count"]
        )


class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    qi_cultivation = db.Column(db.Integer, nullable=False)
    cultivation_level = db.Column(db.Integer, nullable=False)
    inspiration = db.Column(db.Integer, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    inventory = db.Column(db.JSON, nullable=False)
    alchemy_level = db.Column(db.Integer, nullable=False)
    artificer_level = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

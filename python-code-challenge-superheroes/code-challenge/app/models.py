from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

    heropowers = db.relationship('HeroPower', backref='hero', lazy=True)

    def __repr__(self):
        return f'<Hero {self.name}>'

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    heropowers = db.relationship('HeroPower', backref='power', lazy=True)

    @validates('description')
    def validate_description(self, key, value):
        # your validation logic
        return value

    def __repr__(self):
        return f'<Power {self.name}, Description={self.description}>'

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    strength = db.Column(db.String, nullable=False)

    @validates('strength')
    def validate_strength(self, key, value):
        # your validation logic
        return value

    def __repr__(self):
        return f'<HeroPower hero_id={self.hero_id}, power_id={self.power_id}, strength={self.strength}>'

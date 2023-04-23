from game import db
from models.cultivation import Cultivation


class CultivationRepository:
    @staticmethod
    def get_all_cultivations():
        return Cultivation.query.all()

    @staticmethod
    def get_cultivation_by_id(id):
        return Cultivation.query.get(id)

    @staticmethod
    def create_cultivation(cultivation):
        db.session.add(cultivation)
        db.session.commit()
        return cultivation

    @staticmethod
    def update_cultivation(cultivation):
        db.session.commit()
        return cultivation

    @staticmethod
    def delete_cultivation(cultivation):
        db.session.delete(cultivation)
        db.session.commit()

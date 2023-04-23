from cultivation.cultivation_repository import CultivationRepository
from models.cultivation import Cultivation


class CultivationService:
    @staticmethod
    def get_all_cultivations():
        return CultivationRepository.get_all_cultivations()

    @staticmethod
    def get_cultivation_by_id(id):
        return CultivationRepository.get_cultivation_by_id(id)

    @staticmethod
    def create_cultivation(data):
        cultivation = Cultivation(level=data['level'], cultivation_type=data['cultivation_type'])
        return CultivationRepository.create_cultivation(cultivation)

    @staticmethod
    def update_cultivation(id, data):
        cultivation = CultivationRepository.get_cultivation_by_id(id)
        if cultivation:
            cultivation.level = data['level']
            cultivation.cultivation_type = data['cultivation_type']
            cultivation.experience = data['experience']
            return CultivationRepository.update_cultivation(cultivation)
        return None

    @staticmethod
    def delete_cultivation(id):
        cultivation = CultivationRepository.get_cultivation_by_id(id)
        if cultivation:
            return CultivationRepository.delete_cultivation(cultivation)
        return None

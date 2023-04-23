from flask import request
from flask_restful import Resource

from services.cultivation_service import CultivationService


class CultivationController(Resource):
    def get(self):
        cultivations = CultivationService.get_all_cultivations()
        return [cultivation.__dict__ for cultivation in cultivations], 200

    def post(self):
        data = request.json
        cultivation = CultivationService.create_cultivation(data)
        return cultivation.__dict__, 201

    def put(self, id):
        data = request.json
        cultivation = CultivationService.update_cultivation(id, data)
        if cultivation:
            return cultivation.__dict__, 200
        return {"message": "Cultivation not found."}, 404

    def delete(self, id):
        result = CultivationService.delete_cultivation(id)
        if result:
            return {"message": "Cultivation deleted."}, 200
        return {"message": "Cultivation not found."}, 404

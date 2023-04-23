from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.character_service import CharacterService


class CharacterController(Resource):
    def __init__(self):
        self.character_service = CharacterService()

    @jwt_required()
    def get(self, character_id=None):
        if character_id:
            character = self.character_service.get_character(character_id)
            if character:
                return jsonify(character)
            else:
                return {'message': 'Character not found'}, 404
        else:
            characters = self.character_service.get_all_characters()
            return jsonify(characters)

    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        character = self.character_service.create_character(data, current_user_id)
        return jsonify(character), 201

    @jwt_required()
    def put(self, character_id):
        data = request.get_json()
        updated_character = self.character_service.update_character(character_id, data)
        if updated_character:
            return jsonify(updated_character)
        else:
            return {'message': 'Character not found'}, 404

    @jwt_required()
    def delete(self, character_id):
        if self.character_service.delete_character(character_id):
            return '', 204
        else:
            return {'message': 'Character not found'}, 404

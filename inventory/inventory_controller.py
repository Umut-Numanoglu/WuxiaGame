from flask import jsonify, request
from http import HTTPStatus

from services import InventoryService


class InventoryController:
    @staticmethod
    def create_item(user_id):
        data = request.json
        item = InventoryService.create_item(user_id, data['name'], data['description'], data['type'], data['rarity'])
        return jsonify(item.serialize()), HTTPStatus.CREATED

    @staticmethod
    def get_item(item_id):
        item = InventoryService.get_item(item_id)
        if item:
            return jsonify(item.serialize()), HTTPStatus.OK
        return '', HTTPStatus.NOT_FOUND

    @staticmethod
    def update_item(item_id):
        data = request.json
        item = InventoryService.update_item(item_id, data)
        if item:
            return jsonify(item.serialize()), HTTPStatus.OK
        return '', HTTPStatus.NOT_FOUND

    @staticmethod
    def delete_item(item_id):
        deleted = InventoryService.delete_item(item_id)
        if deleted:
            return '', HTTPStatus.NO_CONTENT
        return '', HTTPStatus.NOT_FOUND

    @staticmethod
    def get_all_items(user_id):
        items = InventoryService.get_all_items(user_id)
        return jsonify([item.serialize() for item in items]), HTTPStatus.OK

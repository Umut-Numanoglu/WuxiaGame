from game import db
from models import InventoryItem


class InventoryRepository:
    @staticmethod
    def create_item(item: InventoryItem) -> InventoryItem:
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def get_item(id: int) -> InventoryItem:
        return InventoryItem.query.get(id)

    @staticmethod
    def update_item(item: InventoryItem) -> InventoryItem:
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def delete_item(id: int):
        item = InventoryItem.query.get(id)
        db.session.delete(item)
        db.session.commit()

    @staticmethod
    def get_all_items() -> List[InventoryItem]:
        return InventoryItem.query.all()
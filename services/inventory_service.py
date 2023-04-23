from inventory.inventory_repository import InventoryRepository
from models import InventoryItem


class InventoryService:
    @staticmethod
    def add_item(data) -> InventoryItem:
        item = InventoryItem.from_dict(data)
        return InventoryRepository.create_item(item)

    @staticmethod
    def get_item(id: int) -> InventoryItem:
        return InventoryRepository.get_item(id)

    @staticmethod
    def update_item(id: int, data) -> InventoryItem:
        item = InventoryItem.from_dict(data)
        item.id = id
        return InventoryRepository.update_item(item)

    @staticmethod
    def delete_item(id: int):
        return InventoryRepository.delete_item(id)

    @staticmethod
    def get_all_items() -> List[InventoryItem]:
        return InventoryRepository.get_all_items()
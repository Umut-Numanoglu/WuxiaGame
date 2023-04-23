from typing import List

from models import Character
from characters import CharacterRepository


class CharacterService:
    def __init__(self, character_repository: CharacterRepository):
        self.character_repository = character_repository

    def get_characters(self) -> List[Character]:
        return self.character_repository.get_characters()

    def get_character(self, character_id: int) -> Character:
        return self.character_repository.get_character(character_id)

    def create_character(self, user_id: int, name: str, race: str, character_class: str, level: int) -> Character:
        return self.character_repository.create_character(user_id, name, race, character_class, level)

    def get_all_characters(self) -> List[Character]:
        return self.character_repository.get_all_characters()

    def update_character(self, user_id: int, character_id: int, name: str, race: str, character_class: str, level: int) -> Character:
        return self.character_repository.update_character(user_id, character_id, name, race, character_class, level)

    def delete_character(self, character_id: int):
        self.character_repository.delete_character(character_id)

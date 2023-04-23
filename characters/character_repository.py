from typing import List, Optional

from models import Character


class CharacterRepository:
    def get_characters(self) -> List[Character]:
        """
        Returns a list of all characters.
        """
        return Character.query.all()

    def get_all_characters(self) -> List[Character]:
        characters = Character.query.all()
        return characters

    def get_character(self, character_id: int) -> Character:
        character = Character.query.filter_by(id=character_id).first()
        return character

    def create_character(self, name: str, job: str, level: int, user_id: int) -> Character:
        """
        Creates a new character with the specified name, job, level, and user ID, and returns the new character.
        """
        character = Character(name=name, job=job, level=level, user_id=user_id)
        character.save()
        return character

    def update_character(self, character_id: int, name: str, job: str, level: int) -> Optional[Character]:
        """
        Updates the character with the specified ID with the new name, job, and level, and returns the updated character,
        or None if the character does not exist.
        """
        character = self.get_character_by_id(character_id)
        if character:
            character.name = name
            character.job = job
            character.level = level
            character.save()
        return character

    def delete_character(self, character_id: int) -> bool:
        """
        Deletes the character with the specified ID and returns True, or returns False if the character does not exist.
        """
        character = self.get_character_by_id(character_id)
        if character:
            character.delete()
            return True
        return False

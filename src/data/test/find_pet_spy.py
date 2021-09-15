from typing import Dict, List

from src.domain.models import Pets
from src.domain.test import mock_pets


class FindPetSpy:
    """Class to define use case: Find Pet"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.by_user_id_param = {}
        self.by_pet_id_param = {}
        self.by_pet_id_and_user_id_param = {}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by user_id
        :param - user_id : id of the owner
        :return - Dict with info of the process
        """

        self.by_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by pet_id
        :param - pet_id : id of the pet
        :return - Dict with info of the process
        """

        self.by_pet_id_param["pet_id"] = pet_id
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Select pet by user_id and pet_id
        :param - user_id : id of the owner
        :param - pet_id : id of the pet
        :return - Dict with info of the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(pet_id, int)
        self.by_pet_id_and_user_id_param["user_id"] = user_id
        self.by_pet_id_and_user_id_param["pet_id"] = pet_id

        if validate_entry:
            response = [mock_pets()]

        return {"Success": validate_entry, "Data": response}

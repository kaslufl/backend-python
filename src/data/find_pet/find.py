from typing import Dict, List, Type
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets
from src.domain.use_cases import FindPet as FindPetInterface


class FindPet(FindPetInterface):
    """Class to define use case Find Pet"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by pet_id
        :param - pet_id : id of the pet
        :return - Dict with info of the process
        """

        response = None
        validade_entry = isinstance(pet_id, int)

        if validade_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validade_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select user by user_id
        :param - user_id : id of the owner
        :return - Dict with info of the process
        """

        response = None
        validade_entry = isinstance(user_id, int)

        if validade_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validade_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Select user by pet_id and user_id
        :param - pet_id: id of the pet
        :param - user_id : id of the owner
        :return - Dict with info of the process
        """

        response = None
        validade_entry = isinstance(user_id, int) and isinstance(pet_id, int)

        if validade_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"Success": validade_entry, "Data": response}

from src.presenters.controllers import FindPetController
from src.data.find_pet import FindPet
from src.infra.repo.pet_repository import PetRepository


def find_pet_composer() -> FindPetController:
    """Composing find pet route
    :param: None
    :return: object with find pet route
    """

    repository = PetRepository()
    use_case = FindPet(repository)
    find_pet_route = FindPetController(use_case)

    return find_pet_route

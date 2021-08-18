from faker import Faker

from src.infra.test import PetRepositorySpy
from .find import FindPet

faker = Faker()


def test_by_pet_id():
    """Test by_pet_id method"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"pet_id": faker.random_number(digits=5)}
    response = find_pet.by_pet_id(attributes["pet_id"])

    # Test input
    assert pet_repository.select_pet_param["pet_id"] == attributes["pet_id"]

    # Test output
    assert response["Success"] is True
    assert response["Data"]


def test_by_user_id():
    """Test by_user_id method"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {"user_id": faker.random_number(digits=5)}
    response = find_pet.by_user_id(attributes["user_id"])

    # Test input
    assert pet_repository.select_pet_param["user_id"] == attributes["user_id"]

    # Test output
    assert response["Success"] is True
    assert response["Data"]


def test_by_pet_id_and_user_id():
    """Test by_pet_id_and_user_id method"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "pet_id": faker.random_number(digits=5),
        "user_id": faker.random_number(digits=5),
    }
    response = find_pet.by_pet_id_and_user_id(
        pet_id=attributes["pet_id"], user_id=attributes["user_id"]
    )

    # Test input
    assert pet_repository.select_pet_param["pet_id"] == attributes["pet_id"]
    assert pet_repository.select_pet_param["user_id"] == attributes["user_id"]

    # Test output
    assert response["Success"] is True
    assert response["Data"]

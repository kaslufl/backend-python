from faker import Faker

from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_route():
    """Test route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] == attributes["age"]
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body

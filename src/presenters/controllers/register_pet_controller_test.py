from faker import Faker

from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_route():
    """Test route method in RegisterUserRouter with right params"""

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


def test_route_no_body():
    """Test route method in RegisterUserRouter with no body"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {}

    response = register_pet_route.route(HttpRequest(body=attributes))

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body


def test_route_wrong_body():
    """Test route method in RegisterUserRouter with randoms params"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        faker.word(): faker.word(),
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_route_blank_user_params():
    """Test route method in RegisterUserRouter with blank user params"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(digits=1),
        "user_information": {},
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_route_without_age():
    """Test route method in RegisterUserRouter without age param"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] is None
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body

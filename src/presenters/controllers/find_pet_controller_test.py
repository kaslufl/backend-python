from faker import Faker

from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_pet_controller import FindPetController

faker = Faker()


def test_route_pet_id_and_user_id():
    """Testing route method with both pet_id and user_id"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(
        query={"pet_id": faker.random_number(), "user_id": faker.random_number()}
    )

    response = find_pet_controller.route(http_request)

    # Testing Inputs
    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["pet_id"]
        == http_request.query["pet_id"]
    )
    assert (
        find_pet_use_case.by_pet_id_and_user_id_param["user_id"]
        == http_request.query["user_id"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_route_pet_id_only():
    """Testing route method with pet_id only"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(query={"pet_id": faker.random_number()})

    response = find_pet_controller.route(http_request)

    # Testing Inputs
    assert find_pet_use_case.by_pet_id_param["pet_id"] == http_request.query["pet_id"]

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_route_user_id_only():
    """Testing route method with user_id only"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(query={"user_id": faker.random_number()})

    response = find_pet_controller.route(http_request)

    # Testing Inputs
    assert (
        find_pet_use_case.by_user_id_param["user_id"] == http_request.query["user_id"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_route_with_blank_params():
    """Testing route method with blank params"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_user_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(query={f"{faker.word()}": faker.word()})

    response = find_user_controller.route(http_request)

    # Testing Inputs
    assert find_pet_use_case.by_pet_id_param == {}
    assert find_pet_use_case.by_user_id_param == {}
    assert find_pet_use_case.by_pet_id_and_user_id_param == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_route_no_query_params():
    """Testing route method with no params"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_user_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest()

    response = find_user_controller.route(http_request)

    # Testing Inputs
    assert find_pet_use_case.by_pet_id_and_user_id_param == {}
    assert find_pet_use_case.by_pet_id_param == {}
    assert find_pet_use_case.by_user_id_param == {}

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body

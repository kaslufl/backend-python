from faker import Faker

from src.data.test import RegisterUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_user_controller import RegisterUserController

faker = Faker()


def test_route():
    """Test routo method in RegisterUserRoute with right params"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    attributes = {"name": faker.word(), "password": faker.word()}

    response = register_user_route.route(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_user_use_case.registry_param["name"] == attributes["name"]
    assert register_user_use_case.registry_param["password"] == attributes["password"]

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_no_body():
    """Test routo method in RegisterUserRoute with blank params"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    attributes = {}

    response = register_user_route.route(HttpRequest(body=attributes))

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body


def test_route_wrong_body():
    """Test routo method in RegisterUserRoute with wrong params"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    attributes = {
        faker.word(): faker.word(),
    }

    response = register_user_route.route(HttpRequest(body=attributes))

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body

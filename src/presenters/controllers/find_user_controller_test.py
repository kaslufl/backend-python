from faker import Faker

from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController

faker = Faker()


def test_handle_user_id_and_user_name():
    """Testing handle method with user_id and user_name"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.word()}
    )

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_user_id_only():
    """Testing handle method with user_id only"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_id": faker.random_number()})

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_param["user_id"] == http_request.query["user_id"]

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_user_name_only():
    """Testing handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_name": faker.word()})

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert find_user_use_case.by_name_param["name"] == http_request.query["user_name"]

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handle_with_blank_params():
    """Testing handle method with blank params"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={f"{faker.word()}": faker.word()})

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    # Testing Outputs
    assert response.status_code == 422
    assert "error" in response.body


def test_handle_no_query_params():
    """Testing handle method with no params"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)
    print(response)

    # Testing Inputs
    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body

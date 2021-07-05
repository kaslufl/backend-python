from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser

faker = Faker()


def test_by_id():
    """Test by_id method"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attributes["id"])

    # Test inputs
    assert user_repository.select_user_param["user_id"] == attributes["id"]

    # Test outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_name():
    """Test by_name method"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attributes = {"name": faker.name()}
    response = find_user.by_name(name=attributes["name"])

    # Test inputs
    assert user_repository.select_user_param["name"] == attributes["name"]

    # Test outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_name():
    """Test by_id_and_name method"""

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attributes = {"id": faker.random_number(digits=2), "name": faker.name()}
    response = find_user.by_id_and_name(
        user_id=attributes["id"], name=attributes["name"]
    )

    # Test inputs
    assert user_repository.select_user_param["user_id"] == attributes["id"]
    assert user_repository.select_user_param["name"] == attributes["name"]

    # Test outputs
    assert response["Success"] is True
    assert response["Data"]

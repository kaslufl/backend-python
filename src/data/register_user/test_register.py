from faker import Faker
from .register import RegisterUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_register():
    """Testing the registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attibutes = {"name": faker.name(), "password": faker.word()}

    response = register_user.register(
        name=attibutes["name"], password=attibutes["password"]
    )

    # Test input
    assert user_repo.insert_user_params["name"] == attibutes["name"]
    assert user_repo.insert_user_params["password"] == attibutes["password"]

    # Test output
    assert response["Sucess"] is True
    assert response["Data"]


def test_register_fail():
    """Testing the failure registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attibutes = {"name": faker.random_number(digits=4), "password": faker.word()}

    response = register_user.register(
        name=attibutes["name"], password=attibutes["password"]
    )

    # Test input
    assert user_repo.insert_user_params == {}

    # Test output
    assert response["Sucess"] is False
    assert response["Data"] is None

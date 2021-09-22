from src.presenters.controllers import FindUserController
from src.data.find_user import FindUser
from src.infra.repo.user_repository import UserRepository


def find_user_composer() -> FindUserController:
    """Composing find user route
    :param: None
    :return: object with find user route
    """

    repository = UserRepository()
    use_case = FindUser(repository)
    find_user_route = FindUserController(use_case)

    return find_user_route

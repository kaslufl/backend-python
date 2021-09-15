from typing import Dict

from src.domain.models import Users
from src.domain.test import mock_users


class RegisterUserSpy:
    """Class to define usecase: Register User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.registry_param = {}

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register User"""

        self.registry_param["name"] = name
        self.registry_param["password"] = password

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_users()

        return {"Success": validate_entry, "Data": response}

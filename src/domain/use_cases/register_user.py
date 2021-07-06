from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to Register use case"""

    @classmethod
    @abstractmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """Case"""

        raise Exception("should implement method: register")

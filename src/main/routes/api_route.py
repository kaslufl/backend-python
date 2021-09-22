from flask import Blueprint, jsonify, request
from src.main.composer import (
    register_user_composer,
    register_pet_composer,
    find_user_composer,
    find_pet_composer,
)
from src.main.adapter import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """register user route"""

    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["GET"])
def find_user():
    """find user route"""

    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        message = []

        for user in response.body:
            message.append(
                {
                    "type": "users",
                    "id": user.id,
                    "attributes": {
                        "name": user.name,
                    },
                }
            )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["POST"])
def register_pet():
    """register pet route"""

    response = flask_adapter(request=request, api_route=register_pet_composer())

    if response.status_code < 300:
        message = {
            "type": "pets",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {"owner": {"type": "users", "id": response.body.user_id}},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["GET"])
def find_pet():
    """find pet route"""

    response = flask_adapter(request=request, api_route=find_pet_composer())

    if response.status_code < 300:
        message = []

        for pet in response.body:
            message.append(
                {
                    "type": "pets",
                    "id": pet.id,
                    "attributes": {
                        "name": pet.name,
                        "specie": pet.specie.value,
                        "age": pet.age,
                    },
                    "relationships": {"owner": {"type": "users", "id": pet.user_id}},
                }
            )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )

from flask import Blueprint, request, jsonify
from app.schemas.hello import HelloInput, HelloResponse

hello_blueprint = Blueprint("hello", __name__, url_prefix="/api")


@hello_blueprint.route("/hello", methods=["POST"])
def say_hello():
    data = request.get_json()
    parsed = HelloInput.model_validate(data)  # Pydantic v2 style
    response = HelloResponse(message=f"Hello, {parsed.name}!")
    return jsonify(response.model_dump())

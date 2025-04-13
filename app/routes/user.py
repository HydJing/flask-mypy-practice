from flask import Blueprint, jsonify
from app.services.user_service import get_user_by_id
from app.schemas.user import UserResponse

user_blueprint = Blueprint("user", __name__, url_prefix="/api")

@user_blueprint.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    user = get_user_by_id(user_id)
    response = UserResponse.model_validate(user)
    return jsonify(response.model_dump())

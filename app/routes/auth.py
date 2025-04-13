from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, UserAlreadyExistsError
from app.schemas.auth import UserRegistration, UserResponse
from app.database import SessionLocal

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api")

@auth_blueprint.route("/register", methods=["POST"])
def register():
    # Extract JSON body and validate with Pydantic
    user_data = UserRegistration.model_validate(request.get_json())

    db = SessionLocal()
    try:
        user = register_user(db, user_data)
        response = UserResponse(model_validate(user))  # Convert SQLAlchemy model to Pydantic
        return jsonify(response.model_dump()), 201
    except UserAlreadyExistsError as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

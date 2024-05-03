from models import User
from extensions import db, jwt
from apiflask import APIBlueprint
from flask import request, jsonify
from responses import error_response, render_response
from flask_jwt_extended import (
    jwt_required,
    current_user,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)


auth_bp = APIBlueprint('auth', __name__, url_prefix='/api/auth')


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).first()


@auth_bp.post('/login')
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return error_response(401, 'Invalid email or password')

    access_token = create_access_token(identity=user)

    return render_response(data={'user_id': user.id, 'access_token': access_token})


@auth_bp.post('/logout')
@jwt_required()
def logout():
    return render_response()


@auth_bp.post('/signup')
def signup():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    phone_number = request.json.get('phone_number')

    user = User.query.filter_by(email=email).first()

    if user:
        return error_response(400, 'User already exists')

    user = User(username=username, email=email, phone_number=phone_number)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return render_response()


@auth_bp.post('/delete_account')
@jwt_required()
def delete_account():
    user = current_user
    db.session.delete(user)
    db.session.commit()
    
    return render_response()
from flask import Blueprint
api_blueprint = Blueprint('api_blueprint',__name__)


from app.api.user import handle_user
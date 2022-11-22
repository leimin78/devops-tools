from app.api import api_blueprint
from app.utils.jwt_handle import generate_token
from flask import request,jsonify

@api_blueprint.route('/user/login',methods=['POST'])
def userLogin():
    response = {}
    response['code'] = 0
    response['message'] = 'user login'
    data = request.get_json()
    username = data['username']
    passwd = data['password']
    response['token'] = generate_token(username)
    return jsonify(response)

@api_blueprint.route('/user/info',methods=['GET','POST'])
def userInfo():
    response = {}
    response['code'] = 0
    response['message'] = 'user info'
    # data = request.get_json()
    response['name'] = 'admin'
    response['avatar'] = 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'
    response['introduction'] = 'bbb'
    response['roles'] = ['admin']
    return jsonify(response)


@api_blueprint.route('/user/logout',methods=['POST'])
def userLogout():
    response = {}
    response['code'] = 0
    response['message'] = 'user logout'
    return jsonify(response)
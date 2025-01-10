from fastapi import APIRouter

from app.api.auth.auth_register import auth_register
from app.api.auth.auth_login import auth_login, LoginResponseModel
from app.api.auth.auth_logout import auth_logout
from app.api.auth.auth_refresh_token import auth_refresh_token, RefreshTokenResponseModel
from app.api.auth.get_profile import get_profile, GetProfileResponseModel
from app.api.auth.edit_profile import edit_profile
from app.api.auth.get_barang import get_all_collections
from app.api.auth.get_barang import get_collection_by_id
from app.api.auth.order import create_order,add_order,get_prompt_encrypt
from fastapi import Depends
from app.api.Predict.predict import predict, predict_dev
from app.api.auth.api_dev import request_api_key
from app.dependencies.authentication import Authentication,verify_api_key
api_router = APIRouter()

api_router.add_api_route('/api/v1/auth/register', auth_register, methods=['POST'], tags=['Auth'], status_code=201)
api_router.add_api_route('/api/v1/auth/login', auth_login, methods=['POST'], tags=['Auth'], response_model=LoginResponseModel)
api_router.add_api_route('/api/v1/auth/logout', auth_logout, methods=['POST'], tags=['Auth'], status_code=204)
api_router.add_api_route('/api/v1/auth/refresh-token', auth_refresh_token, methods=['POST'], tags=['Auth'], response_model=RefreshTokenResponseModel)
api_router.add_api_route('/api/v1/auth/profile', get_profile, methods=['GET'], tags=['Auth'], response_model=GetProfileResponseModel)
api_router.add_api_route('/api/v1/auth/profile', edit_profile, methods=['PUT'], tags=['Auth'], status_code=204)
api_router.add_api_route('/api/v1/auth/collect', get_all_collections, methods=['GET'], tags=['Collect'], status_code=200)
api_router.add_api_route('/api/v1/auth/collect/{collect_id}', get_collection_by_id,tags=['Collect'], methods=['GET'], status_code=200)
api_router.add_api_route('/api/v1/auth/order', create_order, methods=['POST'], tags=['Order'], status_code=200)
api_router.add_api_route('/api/v1/auth/order/Predict', predict, methods=['POST'],tags=['Order'] , status_code=200)
api_router.add_api_route('/api/v1/auth/request_api_key', request_api_key, methods=['POST'],tags=['Auth'] , status_code=200)
api_router.add_api_route(
    '/api/v1/auth/api_dev',
    predict_dev,
    methods=['POST'],
    tags=['Feature'],
    dependencies=[Depends(verify_api_key)],
    status_code=200
)

api_router.add_api_route(
    '/api/v1/auth/encrypt',
    get_prompt_encrypt,
    methods=['POST'],
    tags=['Order']
)



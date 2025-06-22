from fastapi import Request, HTTPException, Depends
from jwt_utils import verify_token

def get_current_user_from_jwt_cookie(request: Request):
    jwt_token=request.cookies.get('access_token')
    if not jwt_token:
        raise HTTPException(status_code=401, detail="Jwt token no encontrado")
    payload = verify_token(jwt_token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Jwt token invalido o expirado")
    return payload
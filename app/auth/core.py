import re
from typing import Optional
from uuid import UUID

import jwt
from jwt import PyJWKClient
from pydantic import BaseModel


class Actor(BaseModel):
    """the one jwt is representing
    actor is the actor of the request"""

    id: UUID
    email: Optional[str] = None
    name: str
    preferred_username: Optional[str] = None
    first_name: str
    last_name: str
    iss: str


class AuthSettings(BaseModel):
    JWT_ISSUER: str
    JWT_JWKS_URI: str
    JWT_ALGORITHM: str
    JWT_AUDIENCE: str


def authenticate_token(
    token: str, config: AuthSettings, verify_signature: bool = True
) -> Actor:
    decoded = None
    if verify_signature:
        try:
            jwks_uri = config.JWT_JWKS_URI
            jwks_client = PyJWKClient(jwks_uri)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            decoded = jwt.decode(
                token,
                key=signing_key.key,
                audience=config.JWT_AUDIENCE,
                algorithms=[config.JWT_ALGORITHM],
            )
        except Exception as e:
            raise Exception(f"invalid authorization token: {e}")
        try:
            issuer = decoded["iss"]
        except KeyError as k:
            raise Exception(f"invalid token: {k} is not provided in token")
        if not re.match(config.JWT_ISSUER, issuer):
            raise Exception(f"invalid token: issuer [{issuer}] not allowed")
    else:
        decoded: dict = jwt.decode(token, options={"verify_signature": False})
    actor = Actor(
        id=UUID(decoded["sub"]),
        name=decoded["name"],
        email=decoded.get("email", None),
        preferred_username=decoded["preferred_username"],
        first_name=decoded.get("given_name", ""),
        last_name=decoded.get("family_name", ""),
        iss=decoded["iss"],
    )

    return actor

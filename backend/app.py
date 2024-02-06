import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from webauthn import (
    generate_registration_options,
    generate_authentication_options,
    verify_registration_response,
    verify_authentication_response,
    options_to_json,
    base64url_to_bytes
)
from webauthn.helpers.cose import COSEAlgorithmIdentifier
from webauthn.helpers.structs import (
    AttestationConveyancePreference,
    AuthenticatorAttachment,
    AuthenticatorSelectionCriteria,
    PublicKeyCredentialDescriptor,
    ResidentKeyRequirement,
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


# RP_ID = "localhost"
RP_ID = "github.dev"

USER_CHALLENGE = bytes([1,2,3,4,5,6,7,8,9,0])
USER_PK = "TUZrd0V3WUhLb1pJemowQ0FRWUlLb1pJemowREFRY0RRZ0FFZERMZmg4MjF5TGpKdVl3d01MSVhaQVJUaU9LMHFLdm52bG1aeE1KRmdJeWVkZnFMMkVreXNBeThHdFVjbUdiOXQ5VWpaMHZmWUUwUnUwVl9PVmx3eFE="

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class registerBase(BaseModel):
    username:str


@app.get("/")
async def get_root():
    return "I'm alive!"

@app.post("/auth/register")
async def start_register(user:registerBase):
    simple_registration_options = generate_registration_options(
    rp_id=RP_ID,
    rp_name="Fcrozetta Dev",
    user_name=user.username,
    user_id=bytes([1,2,3,4]),
    challenge=USER_CHALLENGE,
    supported_pub_key_algs=[COSEAlgorithmIdentifier.ECDSA_SHA_512],
    
)
    # print(simple_registration_options)
    return json.loads(options_to_json(simple_registration_options))

@app.post("/auth/register/validate")
async def register_validate(credential:dict):
    # Demonstrating the ability to handle a plain dict version of the WebAuthn response
    registration_verification = verify_registration_response(
        credential=credential,
        expected_challenge=USER_CHALLENGE,
        expected_origin="http://localhost:5000",
        expected_rp_id="localhost",
        require_user_verification=True
    )

@app.get("/auth/login/options")
async def auth_options():
    simple_authentication_options = generate_authentication_options(rp_id=RP_ID,challenge=USER_CHALLENGE)
    bytes
    return json.loads(options_to_json(simple_authentication_options))

@app.post("/auth/login")
async def auth_options(credential:str):
    print(credential)
    
    simple_authentication_options = verify_authentication_response(
        credential=credential,
        expected_challenge=USER_CHALLENGE,
        expected_rp_id=RP_ID,
        expected_origin="https://miniature-trout-q5jx57wvjw29qqx-5173.app.github.dev",
        credential_public_key=base64url_to_bytes(USER_PK),
        credential_current_sign_count=0,
        require_user_verification=True,
    )
    return json.loads(options_to_json(simple_authentication_options))
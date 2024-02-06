import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from webauthn import (
    generate_registration_options,
    verify_registration_response,
    options_to_json,
    base64url_to_bytes,
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
    rp_id="localhost",
    rp_name="Fcrozetta Dev",
    user_name=user.username,
    user_id=bytes([1,2,3,4])
)
    # print(simple_registration_options)
    return json.loads(options_to_json(simple_registration_options))
import json
from fastapi import FastAPI
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

app = FastAPI()

@app.get("/")
async def get_root():
    return "I'm alive!"

@app.post("/register")
async def start_register():
    simple_registration_options = generate_registration_options(
    rp_id="fcrozetta.dev",
    rp_name="Fcrozetta Dev",
    user_name="bob",
)
    # print(simple_registration_options)
    return options_to_json(simple_registration_options)
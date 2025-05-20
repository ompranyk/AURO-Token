from ecdsa import SigningKey, SECP256k1
import base64

def create_wallet():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key.to_string().hex(), public_key.to_string().hex()

def sign_message(private_key_hex, message):
    key = SigningKey.from_string(bytes.fromhex(private_key_hex), curve=SECP256k1)
    return base64.b64encode(key.sign(message.encode())).decode()

def verify_signature(public_key_hex, message, signature):
    from ecdsa import VerifyingKey
    try:
        key = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=SECP256k1)
        return key.verify(base64.b64decode(signature), message.encode())
    except:
        return False
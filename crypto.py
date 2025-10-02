from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import base64

KEY = b"16bytessecretkey"  # 16-byte secret key
IV = b"16bytesivvector!"    # 16-byte IV

def encrypt_aes_cbc(text: str) -> str:
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    return base64.urlsafe_b64encode(ct_bytes).decode('utf-8')


from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class Enc_utils:
  def __init__(self,pwd):
    self.key = self.password_to_key(pwd)
    self.f = Fernet(self.key)
    
  def encrypt(self,data):
    return self.f.encrypt(data.encode()).decode()

  def decrypt(self,data):
    return self.f.decrypt(data.encode()).decode()

  def encrypted_save(self,filename,data):
    try:
      open(filename,"w").write(self.encrypt(data))
    except:
      open(filename,"x").write(self.encrypt(data))

  def decrypt_file(self,filename):
    try:
      return self.decrypt(open(filename,"r").read())
    except:
      return self.decrypt(open(filename,"x").read())

      
  def password_to_key(self, password):
    salt = b'.-Kh)ura/)\xcef\xc8\x88u\xc2'
    password = password.encode()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

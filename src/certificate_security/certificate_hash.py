from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from pathlib import Path

class CertificateHash:

     
    def generate_keys(self):
        """Generate RSA private and public keys."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def encrypt_text(self, plain_text: str, public_key) -> bytes:
        """Encrypt text using the public key."""
        ciphertext = public_key.encrypt(
            plain_text.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt_text(self, ciphertext: bytes, private_key) -> str:
        """Decrypt ciphertext using the private key."""
        decrypted = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()
    
        
    def get_certificate_image_encrypt(self, image_bytes: bytes, public_key: str) -> encrypt_text:
        """Generate SHA256 hash of the certificate image file."""
        return self.encrypt_text(image_bytes, public_key)
    
    def get_certificate_details_encrypt(self,public_key, **kwargs):
        """Generate SHA256 hash of the certificate details."""
        details = "|".join(kwargs.values())
        return self.encrypt_text(details, public_key)
        

if __name__ == "__main__":
 
    Certificate = CertificateHash()
    private_key, public_key = Certificate.generate_keys()
    print("Private Key:", private_key)
    print("Public Key:", public_key)    
    data = {
        "name": "John Doe",
        "id": "123456789",
        "university": "JNTU",
        "course": "KMEC",
        "branch": "CSE",
        "passed_out": 2023,
        "issue_date": "2023-10-01",
        "dob": "2001-01-01",
        "gpa": "9.0",   
        "date": "2023-10-01"
    }
    encrypted = Certificate.get_certificate_details_encrypt(public_key, data = data)
    print("Encrypted Certificate Details:", encrypted)
    decrypted = Certificate.decrypt_text(encrypted, private_key)
    print("Decrypted Certificate Details:", decrypted)
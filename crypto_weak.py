# crypto_weak.py

import hashlib

def hash_password_insecurely(password: str):
    """
    Hashes a password using the MD5 algorithm, which is cryptographically
    broken and should never be used for this purpose.
    """
    print(f"Hashing the password: '{password}'")

    # VULNERABILITY: hashlib.md5 is a known weak hashing algorithm.
    # It is vulnerable to collision and pre-image attacks (rainbow tables).
    # A SAST scanner should flag the use of md5 for any security context.
    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    
    print(f"Insecure (MD5) hash: {hashed_password}")
    return hashed_password

def hash_password_slightly_better(password: str):
    """
    Uses SHA256. While stronger than MD5, modern password hashing should
    use algorithms designed to be slow, like bcrypt or Argon2. Some scanners
    might still flag this as sub-optimal.
    """
    # Still not ideal, but much better than MD5.
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(f"Better (SHA256) hash: {hashed_password}")
    return hashed_password


if __name__ == "__main__":
    user_password = "MySuperSecretPassword123"
    hash_password_insecurely(user_password)
    hash_password_slightly_better(user_password)

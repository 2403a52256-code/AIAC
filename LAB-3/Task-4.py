import os
import hashlib
import hmac
from typing import Dict, Tuple


def _hash_password(password: str, salt: bytes | None = None, iterations: int = 100_000) -> Tuple[bytes, bytes, int]:
    """
    Create a PBKDF2-HMAC-SHA256 hash for the given password.

    Returns (salt, hash, iterations).
    """
    if salt is None:
        salt = os.urandom(16)
    password_bytes = password.encode("utf-8")
    pwd_hash = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, iterations)
    return salt, pwd_hash, iterations


def register_user(users: Dict[str, Dict[str, str]], username: str, password: str) -> Tuple[bool, str]:
    """
    Register a new user with a salted+hashed password.

    - users: in-memory user store mapping username -> record
    - username: unique username
    - password: plaintext password to be hashed and stored

    Returns (success, message).
    """
    username = username.strip()
    if not username:
        return False, "Username cannot be empty."
    if not password:
        return False, "Password cannot be empty."
    if username in users:
        return False, "Username already exists."

    salt, pwd_hash, iterations = _hash_password(password)
    users[username] = {
        "salt": salt.hex(),
        "hash": pwd_hash.hex(),
        "iterations": str(iterations),
    }
    return True, "User registered successfully."


def login_user(users: Dict[str, Dict[str, str]], username: str, password: str) -> Tuple[bool, str]:
    """
    Attempt to log in a user by verifying the password.

    Returns (success, message).
    """
    record = users.get(username)
    if record is None:
        return False, "Invalid username or password."

    try:
        salt = bytes.fromhex(record["salt"])  # type: ignore[index]
        stored_hash = bytes.fromhex(record["hash"])  # type: ignore[index]
        iterations = int(record["iterations"])  # type: ignore[index]
    except Exception:
        return False, "Corrupted user record."

    _, computed_hash, _ = _hash_password(password, salt=salt, iterations=iterations)
    if hmac.compare_digest(stored_hash, computed_hash):
        return True, "Login successful."
    return False, "Invalid username or password."


if __name__ == "__main__":
    # Simple in-memory user store
    users_store: Dict[str, Dict[str, str]] = {}

    print("User Auth Demo (one-time)")
    print("=" * 30)
    print("1) Register  2) Login")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        u = input("New username: ").strip()
        p = input("New password: ").strip()
        ok, msg = register_user(users_store, u, p)
        print(msg)
    elif choice == "2":
        # pre-register a sample user for quick demo
        register_user(users_store, "demo", "demo123")
        print("(Hint: try username=demo, password=demo123)")
        u = input("Username: ").strip()
        p = input("Password: ").strip()
        ok, msg = login_user(users_store, u, p)
        print(msg)
    else:
        print("Invalid choice. Exiting.")

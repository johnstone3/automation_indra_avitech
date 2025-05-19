import os
from dataclasses import dataclass
from typing import Dict

import yaml
from cryptography.fernet import Fernet


@dataclass
class GmailLogin:
    email: str
    password: str


@dataclass
class GmailConfig:
    urls: Dict[str, str]
    login: Dict[str, GmailLogin]


@dataclass
class Config:
    gmail: GmailConfig


def load_environment(yaml_content) -> Config:
    data = yaml.safe_load(yaml_content)

    return Config(**data)


def _get_encryption_key() -> str | None:
    return os.environ.get('SECRETS_DECRYPTION_KEY')


def decrypt_secret(encrypted_secret: str) -> str:
    key = _get_encryption_key()
    if key is None:
        return encrypted_secret

    f = Fernet(key.encode())
    decrypted_secret = f.decrypt(encrypted_secret.encode())

    return decrypted_secret.decode()
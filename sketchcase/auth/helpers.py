from math import pow
from passlib.hash import pbkdf2_sha256


def hash_password(password):
    return pbkdf2_sha256.encrypt(password, rounds=pow(10, 5), salt_size=16)


def verify_password(password, hash):
    return pbkdf2_sha256.verify(password, hash)

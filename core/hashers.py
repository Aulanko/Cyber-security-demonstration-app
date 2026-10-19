import hashlib

from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.crypto import constant_time_compare


class UnsaltedMD5Hasher(BasePasswordHasher):
    """FLAW 2: Identical passwords give identical hashes,
    and the hashes can be cracked in seconds with rainbow tables."""
    algorithm = "weak_md5"

    def encode(self, password, salt=None, **kwargs):
        return f"{self.algorithm}${hashlib.md5(password.encode()).hexdigest()}"

    def verify(self, password, encoded):
        return constant_time_compare(encoded, self.encode(password))

    def decode(self, encoded):
        algorithm, digest = encoded.split("$", 1)
        return {"algorithm": algorithm, "hash": digest}

    def safe_summary(self, encoded):
        return self.decode(encoded)

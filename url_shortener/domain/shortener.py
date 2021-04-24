import hashlib

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from hashids import Hashids

from .. import backend
from ..errors import InputError

DOMAIN = "tier.app/"
URL_VALIDATOR = URLValidator()


def shorten_url(url: str) -> str:
    try:
        URL_VALIDATOR(url)
    except ValidationError as err:
        raise InputError(message=err.message, code=err.code)

    short_id = _generate_id(url)
    short_url, created = backend.get_or_create_url(short_id=short_id, main_url=url)

    return f"{DOMAIN}{short_url.short_id}"


def _generate_id(url: str) -> str:
    md5_hash = hashlib.md5(bytes(url, encoding="utf-8"))
    hashids = Hashids()
    return hashids.encode(int(md5_hash.hexdigest(), 16))

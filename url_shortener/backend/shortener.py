from ..models import ShortURL


def get_or_create_url(main_url: str, short_id: str) -> (ShortURL, bool):
    short_url, created = ShortURL.objects.get_or_create(short_id=short_id, main_url=main_url)
    return short_url, created

from django.test import Client, TestCase

from ...models import ShortURL, TraceOperation


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "https://docs.djangoproject.com/en/3.1/"
        self.path = "/shorten_url/"

    def test_shorten_url(self):
        response = self.client.post(self.path, {"url": self.url})
        short_url = ShortURL.objects.all()[0]
        trace_operation = TraceOperation.objects.all()[0]

        assert short_url.main_url == self.url
        assert trace_operation.view_path == self.path
        assert trace_operation.hit_count == 1

        assert response.status_code == 200
        assert response.content == bytes(f"tier.app/{short_url.short_id}", encoding="utf-8")

    def test_shorten_url_returns_invalid_url_error(self):
        response = self.client.post(self.path, {"url": "not-a-url"})

        assert response.status_code == 400
        assert response.content == bytes("Enter a valid URL.", encoding="utf-8")

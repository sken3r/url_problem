from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from url_shortener.domain import shortener, trace_view_operation
from url_shortener.errors import InputError


@csrf_exempt
@trace_view_operation
@require_http_methods(["POST"])
def shorten_url(request: HttpRequest) -> HttpResponse:
    url = request.POST.get("url")
    try:
        short_url = shortener.shorten_url(url)
    except InputError as err:
        return HttpResponseBadRequest(err.message)
    return HttpResponse(short_url)

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api(request):
    urls = {
        "testing": "/testing/urls",
        "testing2": "/testing2/urls",
        "testing3": "/testing3/urls",
    }
    return Response(urls)

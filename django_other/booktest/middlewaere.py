

class TestMiddleware:
    def process_request(self, request):
        print('~~~~~~~request')

    def process_view(self, request, view_fun, view_args, view_kwargs):
        print('~~~~~~~~~~view')

    def process_response(self, request, response):
        print('~~~~~~~~response')
        return response

def logingMiddleware(get_response):
    def middleware(request):
        print(request.user)
        response = get_response(request)
        return response
    return middleware
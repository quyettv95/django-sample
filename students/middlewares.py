from django.http.response import HttpResponse


class CustomMiddleware():
  def __init__(self, get_response):
    self.get_response = get_response
    # One-time configuration and initialization.

  def __call__(self, request):
    # Code to be executed for each request before
    # the view (and later middleware) are called.

    response = self.get_response(request)
    print("This is demo middleware in Django")
    # Code to be executed for each request/response after
    # the view is called.

    return response

  def process_exception(self, request, exception):
    pass

  def process_template_response(self, request, response):
    return response;


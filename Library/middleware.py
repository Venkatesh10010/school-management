# library/middleware.py
# from django.http import JsonResponse
#
# class BookApiKeyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         path = request.path
#         if path.startswith("/library/api/book/") and request.method == "GET":
#             api_key = None
#             if hasattr(request, "headers"):
#                 api_key = request.headers.get("X-API-KEY")
#             else:
#                 api_key = request.META.get("HTTP_X_API_KEY")
#             if api_key != "secret-key-123":
#                 return JsonResponse({"detail": "API key missing or invalid (middleware)."}, status=403)
#         response = self.get_response(request)
#         return response
# from django.http import JsonResponse
#
# class ApiKeyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         api_key = request.headers.get("X-API-KEY")
#         if api_key != "secret-key-123":
#             return JsonResponse({"detail": "API key invalid or missing"}, status=403)
#         return self.get_response(request)

# middleware.py
import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request details
        self.log_request(request)

        # Process the request
        response = self.get_response(request)

        return response

    def log_request(self, request):
        logger = logging.getLogger('django.request')
        logger.info(f'Method: {request.method}, Path: {request.path}')
        logger.info(f'User-Agent: {request.META.get("HTTP_USER_AGENT", "")}')
        logger.info(f'Cookies: {request.COOKIES}')
        # logger.info(f'Body: {request.body.decode("utf-8")}')
from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle
#
# class BookPostThrottle(UserRateThrottle):
#     scope = 'book_post'
#     def get_cache_key(self, request, view):
#         only apply this throttle for POST; otherwise don't throttle here
        # if request.method != 'POST':
        #     return None
        # return super().get_cache_key(request, view)

# class LaptopGetThrottle(UserRateThrottle):
#     scope = 'laptop_get'
#     def get_cache_key(self, request, view):
#         only apply this throttle for GET; otherwise don't throttle here
#         if request.method != 'GET':
#             return None
#         return super().get_cache_key(request, view)
#
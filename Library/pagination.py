from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

#
# class LaptopPagination(PageNumberPagination):
#     page_size = 3                     # default items per page
#     page_query_param = 'pg'         # default is 'pg'
#     # page_size_query_param = 'size'   # customize the page based on user requirement
#     # max_page_size=6                  #1 single page total max record
#     # last_page_strings='end'          #last page ku redirect agum using end in that above url &default name=last here customise to end


# class LaptopLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 3               # if client doesn't send limit, return 3 items
#     max_limit = 6                   # client cannot request more than 6 items
#     limit_query_param = 'limit'       # use ?lim=4 instead of ?limit=4
#     offset_query_param = 'start'      # use ?start=6 instead of ?offset=6

#
class LaptopCursorPagination(CursorPagination):
    page_size = 3                   # items per page
    # cursor_query_param = 'record'   # ?cursor=<...>
    ordering = '-id'                # order by id desc (must be deterministic)

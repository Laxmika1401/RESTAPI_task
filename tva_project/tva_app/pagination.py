from rest_framework import pagination
class MyPagination1(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page'
    max_page_size = 1000 
    
    
class MyPagination2(pagination.LimitOffsetPagination): 
   limit_query_param='limit' 
   max_limit=20 
   

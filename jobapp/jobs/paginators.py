from rest_framework.pagination import PageNumberPagination


class JobListingPaginator(PageNumberPagination):
    page_size = 20
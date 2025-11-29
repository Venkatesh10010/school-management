from django.urls import path,include
from .router import library_router
from.views import *


urlpatterns=[
    path("api/",include(library_router.urls)),
    path('laptop/',LaptopView.as_view()),
    path('laptop/<int:pk>/',LaptopViewById.as_view()),
    # path('book/<str:tittle>/', BookView.as_view({'get': 'list'}), name='book-filter'),
    path('book/', BookView.as_view({'get': 'list'}), name='book-filter'),
]


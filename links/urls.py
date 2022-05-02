from django.urls import path
from .views import *

urlpatterns = [
    path('create_list', CreateNewList.as_view(), name="create-list"),
	path('create_link', CreateLinks.as_view(), name="create-link"),
    path('get_links/<int:list_id>', GetLinks.as_view(), name="get-links")
]
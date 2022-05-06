from django.urls import path
from .views import *

urlpatterns = [
    path('create_list', CreateNewList.as_view(), name="create-list"),
	path('create_link', CreateLinks.as_view(), name="create-link"),
    path('get_lists', GetLists.as_view(), name="get-lists"),
    path('get_links/<int:list_id>', GetLinks.as_view(), name="get-links"),
    path('delete_link/<int:link_id>', DeleteLink.as_view(), name="delete-link"),
    path('delete_list/<int:list_id>', DeleteList.as_view(), name="delete-list")
]
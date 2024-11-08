from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_album/', add_album, name="add_album"),
    path('edit_album/<int:id>', edit_album, name="edit_album"),
    path('delete_album/<int:id>', delete_album, name="delete_album"),
]

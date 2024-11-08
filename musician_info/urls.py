from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_musician/', add_musician, name="add_musician"),
    path('edit_musician/<int:id>',edit_musician, name="edit_musician"),
]

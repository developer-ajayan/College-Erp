from django.urls import path
from . views import *

urlpatterns = [
    
    path('create-college',create_college,name='create_college'),
    path('edit-college/<int:pk>',edit_college,name='edit_college'),
    path('create-frontpage',create_frontpage,name='create_frontpage'),
    path('edit-frontpage/<int:pk>',edit_frontpage,name='edit_frontpage'),
    path('list-notice',list_notice,name='list_notice'),
    path('create-notice',create_notice,name='create_notice'),
    path('edit-notice/<int:notice_id>',edit_notice,name='edit_notice'),
    path('delete-notice',delete_notice,name='delete_notice'),



]
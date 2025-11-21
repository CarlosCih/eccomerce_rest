from django.urls import path

from apps.users.api.api import user_api_view, user_detail_api_view

urlpatterns = [
    path('usuario/', user_api_view, name='user_api_view'),
    path('usuario/<int:pk>/', user_detail_api_view, name='user_detail_api_view'),
]

""" from apps.users.api.api import UserApiView

urlpatterns = [
    path('usuario/', UserApiView.as_view(), name='usuario_api'),
] """

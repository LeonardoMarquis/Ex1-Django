from django.urls import path
from .views import index, privacy_policy, user_terms, produto

urlpatterns = [
    path('', index, name= 'index'),
    path('privacy_policy', privacy_policy, name= 'privacy_policy'),
    path('user_terms', user_terms, name= 'user_terms'),
    path('produto/<int:pk>', produto, name = 'produto')
]
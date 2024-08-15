from django.urls import path
from api_service.api.auth.views import *

urlpatterns = [
    path('login', auth_view.AuthView.as_view({'post':'post'}), name="Login"),
    path('logout', auth_view.AuthView.as_view({'get':'get'}), name="Logout"),
]

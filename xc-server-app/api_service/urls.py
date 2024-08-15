from django.urls import path, include
from api_service.api.auth import urls as AuthUrls
from api_service.api.user_profile import urls as UserProfileUrls
<<<<<<< HEAD
=======
from api_service.api.admin_profile import urls as AdminProfileUrls
>>>>>>> 45ebbc3... commit #2 : django server app base > admin rest api impl

urlpatterns = [
    path('auth/', include(AuthUrls)),
    path('user/', include(UserProfileUrls)),
<<<<<<< HEAD
=======
    path('admin/', include(AdminProfileUrls)),
>>>>>>> 45ebbc3... commit #2 : django server app base > admin rest api impl
]

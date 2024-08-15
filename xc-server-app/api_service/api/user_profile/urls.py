from django.urls import path
from api_service.api.user_profile.views import *

urlpatterns = [
    path('', user_profile_view.UserProfileView.as_view({'post':'post'})),
    path('fetch/<int:id>', user_profile_view.UserProfileView.as_view({'get':'get'})),
    path('change/name/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_name'})),
    path('change/account_status/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_account_status'})),
<<<<<<< HEAD
=======
    path('change/mobile/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_mobile_number'})),
    path('change/email/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_email_id'})),
    path('change/username/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_username'})),
    path('change/password/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_password'})),
    path('change/bio/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_bio'})),
    path('change/status/<int:id>', user_profile_view.UserProfileView.as_view({'put':'update_user_status'})),
>>>>>>> 45ebbc3... commit #2 : django server app base > admin rest api impl
    path('remove/with_id/<int:id>', user_profile_view.UserProfileView.as_view({'delete':'delete_by_id'})),
    path('remove/with_account_status/<int:account_status>', user_profile_view.UserProfileView.as_view({'delete':'delete_by_account_status'})),
]

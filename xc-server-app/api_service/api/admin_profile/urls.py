from django.urls import path
from api_service.api.admin_profile.views import *

urlpatterns = [
    path('', admin_profile_view.AdminProfileView.as_view({'post':'post'})),
    path('fetch/<int:id>', admin_profile_view.AdminProfileView.as_view({'get':'get'})),
    path('change/name/<int:id>', admin_profile_view.AdminProfileView.as_view({'put':'update_name'})),
    path('change/account_status/<int:id>', admin_profile_view.AdminProfileView.as_view({'put':'update_account_status'})),
    path('change/mobile/<int:id>', admin_profile_view.AdminProfileView.as_view({'put':'update_mobile_number'})),
    path('change/email/<int:id>', admin_profile_view.AdminProfileView.as_view({'put':'update_email_id'})),
    path('change/username/<int:id>', admin_profile_view.AdminProfileView.as_view({'put':'update_username'})),
    path('change/password/<int:id>', admin_profile_view.AdminProfileView.as_view({'put':'update_password'})),
    path('change/status/<int:id>', admin_profile_view.AdminProfileView.as_view({'put':'update_user_status'})),
    path('remove/with_id/<int:id>', admin_profile_view.AdminProfileView.as_view({'delete':'delete_by_id'})),
    path('remove/with_account_status/<int:account_status>', admin_profile_view.AdminProfileView.as_view({'delete':'delete_by_account_status'})),
]

from django.urls import path, include

from .views import *

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    # path('registration/', CustomRegisterView.as_view()),
    path('registration/', include('dj_rest_auth.registration.urls')),
    # path('delete/', delete_account),
    # path('reset-password/', reset_password)
]
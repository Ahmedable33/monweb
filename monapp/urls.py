from django.urls import path
from django.contrib.auth import views
from .views import dash, signup, connexion, signout

urlpatterns = [
    path("signup", signup, name='signup'),
    path("connexion", connexion, name='connexion'),
    path("signout", signout, name='signout'),
    path("dash/", dash, name='dash'),
    # path("signout", signout, name='signout'),

    # path('resetpassword', views.PasswordResetView.as_view, name='resetpassword'),
    # path('resetpasswordSend', views.PasswordResetDoneView.as_view, name='resetpasswordSend'),
    # path('reset/uid64/token',views.PasswordResetConfirmView.as_view, name='passwordconfirm'),
    # path('resetpasswordcomplete',views.PasswordResetCompleteView.as_view, name='passwordcomplet'),

]

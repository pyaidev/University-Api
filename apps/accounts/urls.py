from django.urls import path, reverse_lazy
from .views import login_view, logout_view, signup_view
from django.contrib.auth import views as auth_view

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', signup_view, name='signup'),

    # password reset
    path('reset-password/',
         auth_view.PasswordResetView.as_view(success_url=reverse_lazy("account:password_reset_done"))),
    path('reset-password-done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-confirm/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(success_url=reverse_lazy("account:password_reset_complete")),
         name='password_reset_confirm'),
    path('reset-complete/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # password change
    path('change-password/',
         auth_view.PasswordChangeView.as_view(template_name='registration/password_change_form.html',
                                              success_url=reverse_lazy(
                                                  "account:password_change_done")),
         name='change_password'),
    path('change-password-done/',
         auth_view.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
]

"""
from django.contrib.auth import views as auth_view
1 - Submit email form                       // PasswordResetView.as_view()
2 Email sent success message                // PasswordResetDoneView.as_view()
3 - Link to password Rest form in email     // PasswordResetConfirmView.as_view()
4 - Password successfully changed message   // PasswordResetCompleteView.as_view()
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('register/',views.RegisrerView,name="register"),
    path('login/',views.LoginView,name="login"),
    path('home/',views.HomeView,name="home"),
    path('loguot/',views.Logout_view,name="logout"),
    path('message/',views.Message_View,name="message"),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name="password_reset"),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    path('updatepassword/<str:username>/',views.UpdatePassword,name="updatepassword"),
    
    path('productdata/',views.ProductDataView,name="productdata"),
    # path('identify/',views.IdentifyUserView,name="identify"),
    # path('resetpassword/<str:username>/',views.ResetPasswordView,name="resetpassword"),

    path('singleproductitem/<str:slug>/',views.SingelProductItem,name="singleproductitem"),
    path('category/<slug>/',views.CategoryView,name="category"),
    path('home/',views.HomeView,name='home'),

]
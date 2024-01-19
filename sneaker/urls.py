from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import *
from django.contrib.auth.forms import PasswordResetForm

class MyPasswordResetForm(PasswordResetForm):
    pass






urlpatterns=[
    path("", views.home),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("category/<slug:val>", views.Categoryview.as_view(),name="category"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    path("profile/",views.Profileview.as_view(),name="profile"),
    path("address/",views.address,name="address"),
    path("updateAddress/<int:pk>", views.updateAddress.as_view(), name="updateAddress"),

                #login authentication
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name="sneaker/login.html",
         authentication_form=LoginForm),name='login'),
    path("password_reset/", auth_view.PasswordResetView.as_view(
                    template_name="sneaker/password_reset.html",
                    form_class=MyPasswordResetForm
                ), name="password_reset")

            ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
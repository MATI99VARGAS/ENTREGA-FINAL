from django.urls import path     
from django.contrib.auth.views import LogoutView     
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "core"



urlpatterns = [
    path("",views.home,name="Home"),
    path("login/",views.CustomLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(template_name="core/logout.html"),name="logout"),
    path("register/",views.register,name="register"),
    path("error/",views.Error_view.as_view(),name="Error_view"),
    path("about/",views.about,name="about")
    
]


urlpatterns += staticfiles_urlpatterns()
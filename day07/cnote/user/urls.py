from django.urls import path
from . import views

urlpatterns = [
    # localhost:8888/user/reg
    path('reg', views.reg_view),
    # localhost:8888/user/login
    path('login', views.login_view),
    # localhost:8888/user/logout
    path('logout', views.logout_view),
    

]
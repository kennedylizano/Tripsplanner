from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('createaccount',views.Createuser),
    path("travels",views.travels),
    path("userlogin",views.Login),
    path("travels/add",views.addtravel),
    path("addatrip",views.addatrip),
    path("travels/destination/<viewsID>",views.views),
    path("travels/join/<Id>", views.join),
    path("logout",views.logout)

]
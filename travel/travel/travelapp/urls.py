from django.urls import path
from travelapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index2/login/',views.user_login,name='login'),
    path('index2/logout/',views.user_logout,name='logout'),
    path('index2/register/',views.registerr,name='register'),
    path('index2/<str:page>/', views.index, name='page'),
    path('index2/india/<str:page>/', views.index, name='page'),
    path('index2/india/goldenpackage/<str:page>/', views.index, name='page'),
    path('index2/india/goldenpackage/goa/try/', views.tryy, name='try'),
    path('index2/india/goldenpackage/goa/try/form/', views.form, name='form'),
    path('index2/india/goldenpackage/goa/try/form/booked', views.booked, name='booked'),

    path('index2/india/diamondpackage/<str:page>/', views.index, name='page'),
    path('index2/',views.home,name='home'),
]
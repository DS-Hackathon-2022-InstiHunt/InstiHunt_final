from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page,name='home_page'),
    path('engineering/college_list/', views.college_list,name='college_list'),
    path('analytics_page/',views.analytics_page,name="analytics_page"),
    path('engineering/',views.engineering,name="engineering"),
]




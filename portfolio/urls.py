from django.urls import path
from portfolio import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('skill',views.skill,name='skill'),
    path('project',views.project,name='project'),
    path('resume',views.resume,name='resume'),
]
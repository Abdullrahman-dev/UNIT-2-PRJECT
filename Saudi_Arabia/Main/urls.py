from django.urls import path, include
from . import views
# app_name = 'main'
urlpatterns = [
    path('',views.home,name='home_view'),
    path('home/sustainability',views.sustainability_view,name='sustainability_view'),
    path('home/neom',views.neom_view,name='neom_view'),
    path('home/the_line',views.the_line_view,name="the_line_view"),
    path('home/red_sea',views.the_red_sea_view,name="the_red_sea"),
    path('home/economy',views.economy_view,name='economy_view'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('home/innovation_technology',views.innovation_technology_view,name="innovation_technology_view"),
    path('about/',views.about_view,name='about_view'),
    path('contact_us',views.contact_us,name='contact_us_view')
]

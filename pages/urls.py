from django.urls import path
from .views import about_me_view, contact_view, experience_view

urlpatterns = [
    path('', about_me_view,name = "about_me"),
    path('experience/', experience_view, name = "experience"),
    path('contact/', contact_view, name = "contact"),
]
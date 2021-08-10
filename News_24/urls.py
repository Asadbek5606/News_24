from django.urls import path

from . import views

# TemplateView bilan url qb ishlash

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('index/', views.IndexView.as_view(), name='index'),
     path('blog/', views.BlogView.as_view(), name="blog"),
     path('single/', views.SingleView.as_view(), name='single'),
     path('Contact_us/', views.ContactView.as_view(), name='Contact_us'),
     
     path('registration/', views.registration, name='registration'),
     
     path('login/', views.login, name='login'),
     
     path('logout/', views.logout, name='logout'),
]
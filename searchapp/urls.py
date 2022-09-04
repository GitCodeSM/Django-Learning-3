from django.urls import path

from searchapp import views #as sv

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('counter/', views.counter, name="counter"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('page/<str:pk>', views.page, name="page")
    ]

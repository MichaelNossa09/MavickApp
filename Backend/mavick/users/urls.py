
from django.urls import path
from users.views import RegisterView, LoginView, UserView, LogoutView
# from gestionPedidos.views import ClienteApi


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view())
]
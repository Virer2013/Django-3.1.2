from django.urls import path
from testurlapp import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('user/<int:month>/', views.home, name='home'),
    path('user/<int:month>/<int:year>', views.home, name='home'),
    # site.com/user/12
    # site.com/user/12/2000/
]

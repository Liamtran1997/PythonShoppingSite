from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.show_new, name='Show'),
    path('<int:num>/', views.show_num, name='show_num'),
    re_path(r'^a/(?P<btcq>[0-9]{1, 2})/$', views.show_cq, name="show_cq"),
    path('<str:val>/', views.show_str, name='show_str'),
]



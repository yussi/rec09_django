from django.urls import path
from . import views

app_name = "recfile"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('list/', views.RadikoListView.as_view(), name="list"),
    ]

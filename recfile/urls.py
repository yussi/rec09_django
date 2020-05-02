from django.urls import path
from . import views

app_name = "recfile"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('list/', views.RadikoListView.as_view(), name="list"),
    path('detail/<int:pk>', views.RadikoDetailView.as_view(), name="detail"),
    path('rec_timefree/', views.TimeFreeRecordFormView.as_view(), name="rec_timefree"),
    path('rec_timefree_confirm/', views.TimeFreeRecordForm_Confirm.as_view(), name="rec_timefree_confirm"),
    path('rec_timefree_create/', views.TimeFreeRecore_Create.as_view(), name="rec_timefree_create"),
    ]

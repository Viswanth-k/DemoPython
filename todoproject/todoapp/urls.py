from django.urls import path
from todoapp import views
app_name='todoapp'

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.tasklistView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskdetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskupdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskdeleteView.as_view(),name='cbvdelete'),


    ]
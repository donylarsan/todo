from django.conf.urls.static import static
from django.urls import path

from todoproject import settings
from . import views

urlpatterns = [

    path('', views.add, name='index'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvList/', views.TaskListview.as_view(), name='cbvList'),
    path('cbvDetails/<int:pk>/', views.TaskDetailsView.as_view(), name='cbvDetails'),
    path('cbvUpdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvUpdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]

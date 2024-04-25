from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bug_list/', views.bug_list, name='bug_list'),
    path('feature_list/', views.feature_list, name='feature_list'),
    path('bug_detail/<int:b_id>', views.bug_detail, name='bug_detail'),
    path('feature_id_detail/<int:f_id>', views.feature_id_detail, name='feature_id_detail')
]
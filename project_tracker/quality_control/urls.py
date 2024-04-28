from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('bugs_list/', views.bugs_list, name='bugs_list'),
    path('feature_list/', views.feature_list, name='feature_list'),
    path('bugs_list/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('feature_list/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail')
]
from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('bugs_list/', views.bugs_list, name='bugs_list'),
    path('feature_list/', views.feature_list, name='feature_list'),
    path('bugs_list/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('feature_list/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bug/new/', views.create_bug, name='create_bug'),
    path('feature/new/', views.create_feature, name='create_feature'),
    path('bug/new/', views.BugCreateView.as_view(), name='create_bug'),
    path('feature/new/', views.FeatureCreateView.as_view(), name='create_feature'),
    path('bug/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('feature/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    path('bug/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('feature/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature'),
    path('bug/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('feature/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),
    path('bug/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('feature/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import BugReport, FeatureRequest

def index(request):
    another_page_url1 = reverse('quality_control:bugs_list')
    another_page_url2 = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href = '{another_page_url1}'>Список всех багов</a><br><a href = '{another_page_url2}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bugs_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += "<ul>"
    return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    feature_html = '<h1>Список фич</h1><ul>'
    for feature in features:
        feature_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
    feature_html += "<ul>"
    return HttpResponse(feature_html)

from django.views import View
class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_list_url = reverse('quality_control:bugs_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = f'<h1>Страница приложения quality_control</h1><a href="{bugs_list_url}">Список багов</a>'
        html += '<br>'
        html += f'<a href="{feature_list_url}">Список фич</a>'
        return HttpResponse(html)

from django.views.generic import DetailView
class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        responce_html = f"<h1>Детали бага {bug.id}</h1>"
        responce_html += f'<h2>Информация о баге</h2><h3>Название</h3><p>{bug.title}</p><h3>Описание</h3><p>{bug.description}</p><h3>Статус</h3><p>{bug.status}</p><h3>Приоритет</h3><p>{bug.priority}</p></br>'
        responce_html += '<h2>Информация о связанном проекте</h2>'
        responce_html += f'<h3>Название проекта</h3><p>{bug.project.name}</p><h3>Описание проекта</h3><p>{bug.project.description}</p></br>'
        responce_html += '<h2>Информация о связанной задаче</h2>'
        if bug.task is not None:
            responce_html += f'<h3>Название задачи</h3><p>{bug.task.name}</p><h3>Описание задачи</h3><p>{bug.task.description}</p></br>'
        else:
            responce_html += '<p>Нет связанной задачи</p>'
        return HttpResponse(responce_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        responce_html = f"<h1>Детали фичи {feature.id}</h1>"
        responce_html += f'<h2>Информация о фиче</h2><h3>Название</h3><p>{feature.title}</p><h3>Описание</h3><p>{feature.description}</p><h3>Статус</h3><p>{feature.status}</p><h3>Приоритет</h3><p>{feature.priority}</p></br>'
        responce_html += '<h2>Информация о связанном проекте</h2>'
        responce_html += f'<h3>Название проекта</h3><p>{feature.project.name}</p><h3>Описание проекта</h3><p>{feature.project.description}</p></br>'
        responce_html += '<h2>Информация о связанной задаче</h2>'
        if feature.task is not None:
            responce_html += f'<h3>Название задачи</h3><p>{feature.task.name}</p><h3>Описание задачи</h3><p>{feature.task.description}</p></br>'
        else:
            responce_html += '<p>Нет связанной задачи</p>'
        return HttpResponse(responce_html)
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):
    another_page_url1 = reverse('quality_control:bug_list')
    another_page_url2 = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href = '{another_page_url1}'>Список всех багов</a><br><a href = '{another_page_url2}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse("Список отчетов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, b_id):
    return HttpResponse(f"Детали бага {b_id}")

def feature_id_detail(request, f_id):
    return HttpResponse(f"Детали улучшения {f_id}")
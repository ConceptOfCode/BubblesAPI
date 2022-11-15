import os
from django.shortcuts import render
from django.http import HttpResponse

CURRENT_DIR = os.getcwd()


def bubbles_data(request):
    with open(f'{CURRENT_DIR}/Data/backend/data/bubbles1000.usd.json'.replace('//', '/'), 'r') as file:
        content = file.read()
        return HttpResponse(content, content_type="application/json")


def bubbles_logo(request, img_name: str):
    with open(f'{CURRENT_DIR}/Data/backend/data/logos/{img_name}'.replace('//', '/'), 'rb') as file:
        img = file.read()
        return HttpResponse(img, content_type="image/png")


def currency_table_logo(request, img_name: str):
    with open(f'{CURRENT_DIR}/Data/backend/data/logos/{img_name}'.replace('//', '/'), 'rb') as file:
        img = file.read()
        return HttpResponse(img, content_type="image/png")


def header_footer_logo(request, img_name: str):
    with open(f'{CURRENT_DIR}/Data/backend/images/{img_name}'.replace('//', '/'), 'rb') as file:
        img = file.read()
        return HttpResponse(img, content_type="image/png")


def bubbles_chart(request, time, id, file_name):
    with open(f'{CURRENT_DIR}/Data/backend/data/charts/{time}/{id}/{file_name}'.replace('//', '/'), 'r') as file:
        chart = file.read()
        return HttpResponse(chart, content_type="application/json")

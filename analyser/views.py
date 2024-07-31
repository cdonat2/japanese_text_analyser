from django.http import HttpResponse
from django.template import loader


def index(_):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

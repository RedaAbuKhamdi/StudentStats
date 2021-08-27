from django.http import HttpResponse
from django.template import loader

# TODO change to the actual index location
def index(request):
    index_page = loader.get_template('index.html')
    return  HttpResponse(index_page.render())

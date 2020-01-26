from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import QueryItem

# Create your views here.
def index(request):
    """View function for home page of site."""

    query_items = QueryItem.objects.order_by('id')
    template = loader.get_template('map/index.html')

    context = {
        'query_items': query_items,
    }

    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index_view(request):
    return render(request, 'index.html')

# Create your views here.

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        result = {}  # Here, we will later get results from embeddings
        return JsonResponse(result)
    # return render()
    return render(request, 'base/index.html')

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .logic import MultiAgentSystemGenerator

def index(request):
    if request.method == 'POST':
        # Extract the user's query from the POST data.
        query = request.POST.get('query')
        # Process the query using the chatbot logic defined in `logic.py`.
        result = {}
        print(f"Starting system generation for user idea: {query}")
        
        system_generator = MultiAgentSystemGenerator()
        result = system_generator.process_user_idea(query)

        # Return the chatbot's response as JSON.
        return JsonResponse(result)
    # For non-POST requests, render the chat interface template.
    return render(request, 'base/index.html')

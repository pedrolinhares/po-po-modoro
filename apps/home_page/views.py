from django.shortcuts import render_to_response
from apps.tasks.models import Task

def show_index(request):
	tasks_in_inventory = Task.objects.filter(worksheet="inventory")
	return render_to_response('index.html', {'tasks_in_inventory': tasks_in_inventory})

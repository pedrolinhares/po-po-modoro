from django.shortcuts import render_to_response
from apps.pomodoro.models import Task

def dashboard(request):
	return render_to_response('dashboard.html')

def todo_today(request):
	return render_to_response('todo-today.html')

def inventory(request):
	tasks_in_inventory = Task.objects.filter(worksheet="inventory")
	return render_to_response('inventory.html', {'tasks_in_inventory': tasks_in_inventory})


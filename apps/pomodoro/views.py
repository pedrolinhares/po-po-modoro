from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from apps.pomodoro.models import Task
from apps.user_app.models import UserProfile

def dashboard(request):
	return render_to_response('dashboard.html')

@login_required
def todo_today(request):
	return render_to_response('todo-today.html')

@login_required
def inventory(request):
	tasks_in_inventory = Task.objects.filter(worksheet="inventory")
	return render_to_response('inventory.html', {'tasks_in_inventory': tasks_in_inventory})

@login_required
def update_task(request, id):
	if request.is_ajax() and request.method == 'GET':
		task = get_object_or_404(Task, pk=id)
		field = request.GET['field']
		value = request.GET['value']
		if hasattr(task, field):
			if field == 'pomodoros' and value.isdigit():
				setattr(task, field, value)
				task.save()
			else:
				setattr(task, field, value)
				task.save()
	return HttpResponse(content='', mimetype='text/html')

@login_required
def create_task(request):
	if request.is_ajax() and request.method == 'GET':
		field = request.GET['field']
		value = request.GET['value']
		worksheet = request.GET['worksheet']
		user = request.user
		user = UserProfile.objects.get(user=user)

		if field == 'pomodoros':
			if value.isdigit():
				task = Task(title="new task", pomodoros=value, 
							worksheet=worksheet, user=user)
				task.save()
		else:
				task = Task(title=value, pomodoros=1, 
							worksheet=worksheet, user=user)
				task.save()
		data = serializers.serialize("json", [task,],)
		return HttpResponse(data, mimetype='application/json')
	else:
		return HttpResponse(content='', mimetype='text/html')
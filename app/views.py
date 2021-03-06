from django.shortcuts import render
from .models import User

from typing import Dict

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.request import QueryDict
from django.db.models.query import QuerySet


@csrf_exempt
def index(request):
	if request.method == 'POST':
		data: QueryDict = request.POST
		data_dict: Dict[str, str] = data.dict()
		user:User = User(data_fields=data_dict)
		user.save()
	return render(request, 'app/index.html')


def data_board(request):
	all_entries: QuerySet = User.objects.all()
	return render(request, 'app/databoard.html', {'userdata': all_entries})


def homepage(request):
	return render(request, 'homepage.html')

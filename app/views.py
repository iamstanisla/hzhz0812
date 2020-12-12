from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.request import QueryDict

from typing import Dict

from .models import User


@csrf_exempt
def index(request):
	if request.method == 'POST':
		data: QueryDict = request.POST
		data_dict: Dict[str, str] = data.dict()
		user:User = User(data_fields=data_dict)
		user.save()
	return render(request, 'app/index.html')

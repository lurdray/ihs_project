from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


from django.core.mail import send_mail



def IndexView(request):
	if request.method == "POST":
		pass

	else:

		context = {
				
	            }
		return render(request, "main/index.html", context )



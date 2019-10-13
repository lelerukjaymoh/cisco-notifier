from django.shortcuts import render
from notifier.forms import loginForm
from notifier.models import login_credentials
from django.shortcuts import render, redirect
from .login import Scraper
from .trycisco import See

def index(request):
	data = login_credentials.objects.all().values
	print(data)

	if request.method == "POST":
		form = loginForm(request.POST)
		if form.is_valid():
			studentForm = form.save(commit=False)
			studentForm.save()
			return redirect('index')
	else:
		form = loginForm()

	cisco = Scraper()
	url = cisco.login()
	cisco.courses_status(url)

	# see = See()
	# ans = see.me()

	return render(request, 'index.html', {'form': form, 'data': data})

from django.shortcuts import render
from .forms import UserProfileForm


# Create your views here.
def index(request):
	form = UserProfileForm()
	return render(request, 'userform/index.html', {'form': form})

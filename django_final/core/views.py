from django.shortcuts import redirect
from django.views.generic.list import ListView
from .models  import Owner, Repos




# Create your views here.

class OwnerList(ListView):
    model = Owner

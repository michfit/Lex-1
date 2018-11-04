from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def messaging(request):
    return render(request, 'main/messaging.html')
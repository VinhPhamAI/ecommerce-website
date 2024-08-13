from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# def authencation(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#         else:
#             form = UserCreationForm()
#     return render(request, 'sign_up.html', {'form' : form})

# Create your views here.
def index(request):
    return render(request, 'cart.html')
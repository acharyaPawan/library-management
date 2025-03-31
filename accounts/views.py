from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

# def login_view(request):
#     print("here")
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'accounts/login.html', {'form': form})

# def SignUpView(request):
#     if request.method == "POST":
#         print("here")
#         print("The formdata is: ", request)
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

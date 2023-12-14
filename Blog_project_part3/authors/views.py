from typing import Any
from django.shortcuts import render,redirect
from .import forms 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import PostModel
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def add_register(request):
    if request.method=='POST':
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            print(request.POST)
            messages.success(request, 'Account Register successful')
            form.save()
            return redirect('author:register')
    
    else:
        form=forms.RegisterForm()
    return render(request,'register.html',{'form':form ,'type':'register'})


# def user_login(request):
#     if request.method=='POST':
#         form=AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             user_name=form.cleaned_data['username']
#             user_pass=form.cleaned_data['password']
#             user=authenticate(username=user_name,password=user_pass)
#             if user is not None:
#                 messages.success(request, 'Account Login successful')
#                 login(request,user)
#                 return redirect('author:profile')
#             else:
#                 messages.warning(request, 'Account Login  Failed')
#                 return redirect('author:register')
            
#     else:
#         form=AuthenticationForm()
#     return render(request,'register.html',{'form':form,'type':'Login'})


class MyLoginView(LoginView):
    template_name='register.html'
    
    def get_success_url(self):
        return reverse_lazy('add_post')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context

@login_required
def profile(request):
   data=PostModel.objects.filter(author=request.user)
   return render(request,'profile.html',{'data':data})


@login_required
def update_profile(request):
    if request.method =='POST':
        form=forms.Change_usesr_data(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Update successful')
            return redirect('author:update_profile')
        
    else:
        form=forms.Change_usesr_data(instance=request.user)
    return render(request,'update_profile.html',{'form':form})


# def change_password(request):
#     if request.method=='POST':
#         form=PasswordChangeForm(request.user,data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request,form.user)
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('author:profile')
#         else:
#             messages.error(request, 'Please correct the error below.')

#     else:
#         form=PasswordChangeForm(user=request.user)
#     return render(request,'pass_change.html',{'form':form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('author:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html',{'form':form})
        
  




def User_logout(request):
    logout(request)
    return redirect('author:login')
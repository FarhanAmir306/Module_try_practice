from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
# Create your views here.
# @login_required
# def add_post(request):
#     if request.method=='POST':
#         form=forms.PostForm(request.POST)
#         if form.is_valid():
#             print(request.POST)
#             form.instance.author =request.user
#             form.save()
         
#             return redirect('add_post')
    
#     else:
#         form=forms.PostForm()
#     return render(request,'posts.html',{'form':form})


class AddCreateView(CreateView):
    model=models.PostModel
    fields=['title','content','category','image']
    template_name = 'posts.html'
    success_url=reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "The Post was created successfully.")
        return super().form_valid(form)
    
    

# @login_required
# def edit_post(request,id):
#     post_model=models.PostModel.objects.get(pk=id)
#     post_form =forms.PostForm(instance=post_model)
#     if request.method=='POST':
#         form=forms.post_form(request.POST,instance=post_model)
#         if form.is_valid():
#             print(request.POST)
#             form.instance.author =request.user
#             form.save()
#             return redirect('homepage')
    
#     else:
#         form=forms.PostForm()
#     return render(request,'posts.html',{'form':form})

class UpadatePost(UpdateView):
    model=models.PostModel
    form=forms.PostForm
    template_name = 'delet.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, "The Post was Update successfully.")
        return super().form_valid(form)
    

# class DetailPostView(DetailView):
#     model=models.PostModel
#     template_name='post_details.html'
#     pk_url_kwarg='id'
    
    
class DetailPostView(DetailView):
    model = models.PostModel
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    


@login_required   
def delete_post(request,id):
    del_post=models.PostModel.objects.get(pk=id)
    del_post.delete()
    return redirect('homepage')


class Delete_Post(DeleteView):
    model=models.PostModel
    form=forms.PostForm
    pk_url_kwarg='id'
    template_name='delet.html'
    success_url=reverse_lazy('homepage')

    
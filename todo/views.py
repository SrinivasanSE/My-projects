from django.shortcuts import render, reverse
from django.views import generic
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Create your views here.

class ListTodo(LoginRequiredMixin, generic.ListView):
    model = Todo

    # template_name='todo_list.html' <model>_list.html(default) dont need to specify
    # context_object_name = object_list default
    def get_queryset(self):
        return Todo.objects.filter(user=self.kwargs['user_id'])


class TodoCreateView(LoginRequiredMixin,generic.CreateView):
    model = Todo
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('todo:home', kwargs={'user_id': self.request.user.id})


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Todo

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('todo:home', kwargs={'user_id': self.request.user.id})


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Todo
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('todo:home', kwargs={'user_id': self.request.user.id})


def cross_off(request, obj_id):
    todo = Todo.objects.get(id=int(obj_id))
    todo.is_completed = True
    todo.save()
    return HttpResponseRedirect(reverse('todo:home', kwargs={'user_id': request.user.id}))


def uncross(request, obj_id):
    todo = Todo.objects.get(id=int(obj_id))
    todo.is_completed = False
    todo.save()
    return HttpResponseRedirect(reverse('todo:home', kwargs={'user_id': request.user.id}))

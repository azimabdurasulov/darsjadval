from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Turtinchi

class TurtinchiListView(ListView):
    model = Turtinchi
    template_name = 'turtinchi/turtinchi_list.html'


class TurtinchiUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Turtinchi
    fields = ('title', 'body', 'photo')
    template_name = 'turtinchi/turtinchi_edit.html'
    success_url = reverse_lazy('turtinchi_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TurtinchiDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Turtinchi
    template_name = 'turtinchi/turtinchi_delete.html'
    success_url = reverse_lazy('turtinchi_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TurtinchiCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model= Turtinchi
    template_name = 'turtinchi/turtinchi_new.html'
    fields = ('title', 'body', 'photo',)
    success_url = reverse_lazy('turtinchi_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user seper userligini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

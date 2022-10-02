from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Uchinchi

class UchinchiListView(ListView):
    model = Uchinchi
    template_name = 'uchinchi/uchinchi_list.html'


class UchinchiUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Uchinchi
    fields = ('title', 'body', 'photo')
    template_name = 'uchinchi/uchinchi_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class UchinchiDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Uchinchi
    template_name = 'uchinchi/uchinchi_delete.html'
    success_url = reverse_lazy('uchinchi_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class UchinchiCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model= Uchinchi
    template_name = 'uchinchi/uchinchi_new.html'
    fields = ('title', 'body', 'photo',)
    success_url = reverse_lazy('uchinchi_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user seper userligini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

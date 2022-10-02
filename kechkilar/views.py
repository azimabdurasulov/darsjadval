from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Kechki

class KechkiListView(ListView):
    model = Kechki
    template_name = 'kechki_list.html'


class KechkiUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Kechki
    fields = ('title', 'body', 'photo')
    template_name = 'kechki_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class KechkiDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Kechki
    template_name = 'kechki_delete.html'
    success_url = reverse_lazy('kechki_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class KechkiCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model= Kechki
    template_name = 'kechki_new.html'
    fields = ('title', 'body', 'photo',)
    success_url = reverse_lazy('kechki_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user seper userligini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

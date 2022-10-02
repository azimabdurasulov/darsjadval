from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Ikkinchi

class IkkinchiListView(ListView):
    model = Ikkinchi
    template_name = 'ikkinchi/ikkinchi_list.html'


class IkkinchiUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ikkinchi
    fields = ('title', 'body', 'photo')
    template_name = 'ikkinchi/ikkinchi_edit.html'
    success_url = reverse_lazy('ikkinchi_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class IkkinchiDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ikkinchi
    template_name = 'ikkinchi/ikkinchi_delete.html'
    success_url = reverse_lazy('ikkinchi_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class IkkinchiCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model= Ikkinchi
    template_name = 'ikkinchi/ikkinchi_new.html'
    fields = ('title', 'body', 'photo',)
    success_url = reverse_lazy('ikkinchi_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user seper userligini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

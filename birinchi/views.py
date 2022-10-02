from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Birinchi

class BirinchiListView(ListView):
    model = Birinchi
    template_name = 'birinchi/birinchi_list.html'


class BirinchiUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Birinchi
    fields = ('title', 'body', 'photo')
    template_name = 'birinchi/birinchi_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BirinchiDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Birinchi
    template_name = 'birinchi/birinchi_delete.html'
    success_url = reverse_lazy('birinchi_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BirinchiCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model= Birinchi
    template_name = 'birinchi/birinchi_new.html'
    fields = ('title', 'body', 'photo',)
    success_url = reverse_lazy('birinchi_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user seper userligini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

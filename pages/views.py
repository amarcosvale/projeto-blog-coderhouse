from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

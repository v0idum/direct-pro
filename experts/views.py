from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from experts.forms import ExpertCreateForm
from experts.models import ExpertProfile, Category


class ExpertCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ExpertProfile
    template_name = 'experts/expert_create.html'
    form_class = ExpertCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.price_per_minute *= 100
        self.request.user.is_expert = True
        self.request.user.save(update_fields=['is_expert'])
        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.is_expert


class ExpertDetailView(DetailView):
    model = ExpertProfile
    context_object_name = 'expert'
    template_name = 'experts/expert_detail.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'experts/category_detail.html'

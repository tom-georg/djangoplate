from django.shortcuts import render
from django.views import View
# Create your views here.
from django.urls import reverse_lazy
from djangoplate.views.superviews import SuperCreateView, SuperListView, SuperDetailView, SuperUpdateView
from notesdemo.models import DemoNote
class index(View):
    def get(self, request):
        return render(request, "notesdemo/index.html", {})
    
class NoteCreateView(SuperCreateView):
    model = DemoNote
    fields = ['title', 'body']
    success_url = reverse_lazy('notesdemo:list')

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        context['title'] = "Create a Note"
        return context
    
class NoteListView(SuperListView):
    model = DemoNote
    
    
    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context['title'] = "List of Notes"
        return context
    
class NoteDetailView(SuperDetailView):
    model = DemoNote
    fields = ['title', 'body']
    
    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        context['title'] = "Detail of Note"
        return context
    
class NoteUpdateView(SuperUpdateView):
    model = DemoNote
    fields = ['title', 'body']
    success_url = reverse_lazy('notesdemo:list')
    
    def get_context_data(self, **kwargs):
        context = super(NoteUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Update a Note"
        return context
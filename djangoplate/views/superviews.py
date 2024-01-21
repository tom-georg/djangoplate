from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class SuperCreateView(CreateView):
    """
    Boilerplate CreateView
    """
    template_name = 'boilerplate/form.html'
    
    #success_url = reverse_lazy('boilerplate:list')

class SuperListView(ListView):
    """
    Boilerplate ListView
    """
    template_name = 'boilerplate/list.html'

class SuperDetailView(DetailView):
    """
    Boilerplate DetailView
    """
    template_name = 'boilerplate/detail.html'

class SuperUpdateView(UpdateView):
    """
    Boilerplate UpdateView
    """
    template_name = 'boilerplate/form.html'
from django.shortcuts import render,HttpResponse
from .models import Document
from .forms import DocumentForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy


class create(CreateView):
    model=Document
    form_class=DocumentForm
    template_name="documents/create.html"
    success_url=reverse_lazy('documents_index')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    


class index(ListView):
    model=Document
    template_name="documents/index.html"
    context_object_name="parcours"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context["parcours"] = Document.objects.all()
        else:
            context["parcours"] = Document.objects.filter(author=self.request.user)
        return context
    


class edit(UpdateView):
    model=Document
    form_class=DocumentForm
    template_name="documents/edit.html"
    success_url=reverse_lazy('documents_index')

class delete(DeleteView):
    model=Document
    template_name="documents/delete.html"
    success_url=reverse_lazy('documents')
    


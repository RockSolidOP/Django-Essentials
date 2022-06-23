from turtle import title
from urllib import request
from django.shortcuts import render
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from notes.forms import NotesForm
# Create your views here.



class NotesDelete(DeleteView):
    model = Notes
    # form_class = NotesForm
    success_url = '/notes/'
    template_name = 'notes\\notes_delete.html'
    login_url = '/admin'

class NotesUpdate(LoginRequiredMixin,UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/'
    login_url = '/admin'

class NotesCreate(LoginRequiredMixin,CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/'
    login_url = '/admin'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class NotesList(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes\\notes.html'
    # login_url = '/admin'
    login_url = 'home.login'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetail(LoginRequiredMixin,DetailView):
    model = Notes
    template_name = 'notes\\notes_details.html'    
    context_object_name = 'note'
    login_url = '/admin'

# def list(request=request):
#     all_notes = Notes.objects.all()
#     return render(request=request,template_name="notes\\notes.html",context={'all_notes' : all_notes})

# def showHead(request=request):
    
#     return render(request=request,template_name="notes\\abc.html",context={})


# def detail(reqeust, pk):

#     try: 
#         note = Notes.objects.get(pk=pk)
    
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")

   
#     print(note.title)
#     return render(request=reqeust, template_name="notes\\notes_details.html", context= { 'note' : note})
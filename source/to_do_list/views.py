from django.shortcuts import render, get_object_or_404, redirect
from to_do_list.models import Task, Project
from to_do_list.forms import TaskForm
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy



class TaskView(TemplateView):
    model = Task
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('to_do_list:project_detail', kwargs={'pk': self.kwargs['pk']})



class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        form.save()
        return redirect('to_do_list:task_view', pk=self.object.pk)



class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'

    def get_success_url(self):
        project_id = self.object.project.id
        return reverse_lazy('to_do_list:project_detail', kwargs={'pk': project_id})


class ProjectIndexView(ListView):
    model = Project
    template_name = 'project_index.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Project.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        else:
            return Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'



class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['start_date', 'end_date', 'name', 'description']
    success_url = reverse_lazy('to_do_list:project_index')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['start_date', 'end_date', 'name', 'description']
    success_url = reverse_lazy('to_do_list:project_index')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = ('project_delete.html')
    success_url = reverse_lazy('to_do_list:project_index')





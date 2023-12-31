from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from to_do_list.models import Task, Project
from to_do_list.forms import TaskForm, ProjectUserForm
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.models import User



class TaskView(TemplateView):
    model = Task
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context


class TaskCreateView(PermissionRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    permission_required = 'to_do_list.add_task'


    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('to_do_list:project_detail', kwargs={'pk': self.kwargs['pk']})



class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    permission_required = 'to_do_list.delete_comment'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        form.save()
        return redirect('to_do_list:task_view', pk=self.object.pk)



class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    permission_required = 'to_do_list.delete_task'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

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
    def form_valid(self, form):
        self.project = form.save(commit=False)
        self.project.author = self.request.user
        self.project.save()
        form.save_m2m()
        return redirect('to_do_list:add_project', pk=self.project.pk)


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['start_date', 'end_date', 'name', 'description']
    success_url = reverse_lazy('to_do_list:project_index')
    permission_required = 'to_do_list.change_project'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class ProjectDeleteView(UserPassesTestMixin,DeleteView):
    model = Project
    template_name = ('project_delete.html')
    success_url = reverse_lazy('to_do_list:project_index')
    def test_func(self):
        return self.request.user.has_perm('to_do_list.delete_project') or self.request.user == self.get_object().author


class ProjectUserAddView(View):
    template_name = 'project_user_add.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectUserForm()  # This line should instantiate the form, not call it as a function
        return render(request, self.template_name, {'project': project, 'form': form})

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectUserForm(request.POST)  # This is the correct way to instantiate the form

        if form.is_valid():
            users = form.cleaned_data['users']
            project.users.set(users)
            return redirect('to_do_list:project_detail', pk=pk)

        return render(request, self.template_name, {'project': project, 'form': form})

class ProjectUserRemoveView(View):
    template_name = 'project_user_remove.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectUserForm(initial={'users': project.users.all()})
        return render(request, self.template_name, {'project': project, 'form': form})

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectUserForm(request.POST, initial={'users': project.users.all()})

        if form.is_valid():
            users = form.cleaned_data['users']
            project.users.remove(*users)
            return redirect('to_do_list:project_detail', pk=pk)

        return render(request, self.template_name, {'project': project, 'form': form})

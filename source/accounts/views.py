from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import CreateView
from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'user_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:index')

        return next_page




# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
#
#
# def login_view(request):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('to_do_list:project_index')
#         else:
#             context['has_error'] = True
#     return render(request, 'login.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('to_do_list:project_index')
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserForm
from .models import Entry

class LockedView(LoginRequiredMixin):
    login_url = "login"

class EntryListView(LockedView, ListView):
    model = Entry

    # DO NOT REMOVE QUERYSET, limits users from accessing others entries
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by("-date_created")

class EntryDetailView(LockedView, DetailView):
    model = Entry

    # DO NOT REMOVE QUERYSET, limits users from accessing others entries
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"

    def form_valid(self, form):
         user = self.request.user
         form.instance.user = user
         return super(EntryCreateView, self).form_valid(form)

class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )

    # DO NOT REMOVE QUERYSET, limits users from accessing others entries
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class EntryDeleteView(LockedView, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

def user_profile(request, username):
    user = User.objects.get(username=username)
    context = {
       "user": user
    }

    return render(request, 'entries/user_profile.html', context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="entries/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="entries/login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, f"You are now logged out.")
    return redirect('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'entries/change_password.html', {
        'form': form
    })
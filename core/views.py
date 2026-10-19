import logging

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import connection
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Note

logger = logging.getLogger("core.security")


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "core/form.html", {"form": form, "title": "Register"})


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # FLAW 4: different messages reveal which usernames exist (user enumeration),
        # and there is no limit on login attempts (brute force)
        if not User.objects.filter(username=username).exists():
            error = "User does not exist"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("note_list")
            error = "Wrong password"

        # FLAW 5: failed logins are never logged
        # FIX for 4 and 5: 
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     logger.info("Login ok user=%s ip=%s", username, request.META.get("REMOTE_ADDR"))
        #     return redirect("note_list")
        # logger.warning("Login FAILED user=%r ip=%s", username, request.META.get("REMOTE_ADDR"))
        # error = "Invalid username or password"
        # For rate limiting, also `pip install django-axes` and follow its setup.
    return render(request, "core/login.html", {"error": error})


@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, "core/note_list.html", {"notes": notes})


@login_required
def note_create(request):
    form = NoteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        note = form.save(commit=False)
        note.owner = request.user
        note.save()
        return redirect("note_detail", note_id=note.id)
    return render(request, "core/form.html", {"form": form, "title": "New note"})


@login_required
def note_detail(request, note_id):
    # FLAW 1 (Broken Access Control): any logged-in user can read any note by changing the id in the URL 
    note = get_object_or_404(Note, pk=note_id)
    # FIX 1:
    # note = get_object_or_404(Note, pk=note_id, owner=request.user)
    return render(request, "core/note_detail.html", {"note": note})


@login_required
@require_POST
def note_delete(request, note_id):
    # FLAW 1: same problem, any user can delete anyone's note
    note = get_object_or_404(Note, pk=note_id)
    # FIX 1:
    # note = get_object_or_404(Note, pk=note_id, owner=request.user)
    note.delete()
    # FLAW 5: deletions are not logged
    # FIX 5: logger.info("Note %s deleted by user=%s", note_id, request.user.username)
    return redirect("note_list")


@login_required
def search(request):
    q = request.GET.get("q", "")

    # FLAW 3 (Injection): user input is pasted straight into the SQL string
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, title FROM core_note "
            f"WHERE owner_id = {request.user.id} AND title LIKE '%{q}%'"
        )
        results = cursor.fetchall()

    # FIX 3: use the ORM (or parameterized queries: cursor.execute("... LIKE %s", [f"%{q}%"]))
    # results = Note.objects.filter(owner=request.user, title__icontains=q).values_list("id", "title")

    return render(request, "core/search.html", {"results": results, "q": q})
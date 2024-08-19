from django.shortcuts import render
from .forms import AdditionForm

# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        form = AdditionForm(request.POST or None)
        context["form"] = form
        if form.is_valid():
            context["result"] = form.cleaned_data.get("a") + form.cleaned_data.get("b")
    return render(request, "index.html", context=context)
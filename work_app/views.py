from django.shortcuts import render
from django.views import View
from .models import TodoWork
from django.shortcuts import render, redirect
from django.views import View
from .models import TodoWork, WorkDetails
from .forms import TodoWorkForm


class TodoWorkView(View):
    model = TodoWork
    template_name = "work.html"

    def get(self, request):
        data = self.model.objects.all().order_by("-id")

        return render(
            request,
            self.template_name,
            context={"data_list": data, "form": TodoWorkForm()},
        )

    def post(self, request):
        form = TodoWorkForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("todo")
        else:
            data = self.model.objects.all()
            return render(
                request, self.template_name, context={"data_list": data, "form": form}
            )

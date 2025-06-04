from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *


def index(request):
    records = Record.objects.all()
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = RecordForm()

    return render(request, "app4/index_4.html", {
                "form": form,
                'records': records,
                })

def delete_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    record.delete()
    return redirect('app4:index_4')


from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class RecordUpdate(UpdateView):
    model = Record
    form_class = RecordForm
    # fields = ['name','amount','unit']
    success_url = reverse_lazy('app4:index_4')



from rest_framework import generics
from .serializers import RecordSerializer
from rest_framework.permissions import AllowAny


class RecordListCreate(generics.ListCreateAPIView):
    queryset = Record.objects.all().order_by('-id')
    serializer_class = RecordSerializer
    permission_classes = [AllowAny]

class RecordRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [AllowAny]

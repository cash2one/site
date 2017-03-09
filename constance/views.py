# Create your views here.
from django.shortcuts import render
from constance.forms import ConfigForm
from constance.models import Config


def ChangeList(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            for f in form.fields:
                dbobj, created = Config.objects.get_or_create(key=f)
                dbobj.value = form.cleaned_data[f]
                dbobj.save()
    else:
        form = ConfigForm()

    return render(request,'contstance/simple_constance.html',locals())
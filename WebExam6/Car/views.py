from django.shortcuts import render, redirect

from WebExam6.Car.forms import CreateCarForm, EditCarForm, DeleteCarForm
from WebExam6.Car.models import Car
from WebExam6.Profile.views import get_profile


# Create your views here.
def car_create(request):
    profile = get_profile()

    form = CreateCarForm()
    if request.method == "POST":
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'car-create.html', context)


def car_details(request, id):
    profile = get_profile()
    car = Car.objects.get(pk=id)

    context = {
        'profile': profile,
        'car': car,
    }

    return render(request, 'car-details.html', context)


def car_edit(request, id):
    profile = get_profile()
    car = Car.objects.get(pk=id)

    form = EditCarForm(instance=car)
    if request.method == "POST":
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form,
    }

    return render(request, 'car-edit.html', context)


def car_delete(request, id):
    profile = get_profile()
    car = Car.objects.get(pk=id)

    form = DeleteCarForm(instance=car)
    if request.method == "POST":
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form,
    }

    return render(request, 'car-delete.html', context)

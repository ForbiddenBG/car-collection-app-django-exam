from django.db.models import Sum
from django.shortcuts import render, redirect

from WebExam6.Car.models import Car
from WebExam6.Profile.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from WebExam6.Profile.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


# Create your views here.
def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def profile_create(request):
    profile = get_profile()

    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile-create.html', context)


def catalogue_page(request):
    profile = get_profile()
    cars = Car.objects.all()

    context = {
        'profile': profile,
        'cars': cars,
    }

    return render(request, 'catalogue.html', context)


def profile_details(request):
    profile = get_profile()
    total_price = Car.objects.all().aggregate(Sum('price'))
    price = total_price['price__sum']

    context = {
        'profile': profile,
        'price': price,
    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
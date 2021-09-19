from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, DodatkoweInfo, Ocena
from .forms import FilmForm,DodatkoweInfoForm, UserRegistrationForm, OcenaForm
from django.contrib.auth.decorators import login_required


def wszystkie_filmy(request):
    wszystkie=Film.objects.all()
    return render(request,'filmy.html',{'filmy':wszystkie})

def register(request):
    user_form=UserRegistrationForm(request.POST or None)
    if user_form.is_valid():
        new_user=user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return render(request,'registration/register_done.html',{'new_user':new_user})
    return render(request,'registration/register.html',{'user_form':user_form})

@login_required
def nowy_film(request):
    czy_nowy=True
    form=FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe=DodatkoweInfoForm(request.POST or None)

    if all((form.is_valid(),form_dodatkowe.is_valid())):
        film=form.save(commit=False)
        dodatkowe=form_dodatkowe.save()
        film.dodatkowe=dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request,'film_form.html',{'form':form, 'form_dodatkowe':form_dodatkowe ,'nowy':czy_nowy})

@login_required
def edytuj_film(request, id):
    czy_nowy=False
    film=get_object_or_404(Film, pk=id)
    try:
        dodatkowe=DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe=None

    form = FilmForm(request.POST or None, request.FILES or None,instance=film)
    form_dodatkowe=DodatkoweInfoForm(request.POST or None, instance=dodatkowe)

    if all((form.is_valid(),form_dodatkowe.is_valid())):
        film=form.save(commit=False)
        dodatkowe=form_dodatkowe.save()
        film.dodatkowe=dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form, 'form_dodatkowe':form_dodatkowe, 'nowy':czy_nowy})

@login_required
def usun_film(request, id):
    film=get_object_or_404(Film, pk=id)

    if request.method=="POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})

@login_required()
def info_film(request,id):
    film=get_object_or_404(Film,pk=id)
    oceny=Ocena.objects.filter(film=film)

    form_ocena=OcenaForm(request.POST or None)
    if request.method=='POST':
        if 'gwiazdki' in request.POST:
            ocena=form_ocena.save(commit=False)
            ocena.film=film
            ocena.save()

    return render(request,'info.html',{'film':film,'oceny':oceny,'form_ocena':form_ocena})
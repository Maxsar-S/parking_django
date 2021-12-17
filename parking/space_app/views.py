import datetime
from django.shortcuts import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import Reservation, Space, User
from .forms import LoginForm, ReservationEditForm, SpaceEditForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

time_for_reserve = (
    '00:00:00 - 04:00:00',
    '04:00:00 - 08:00:00',
    '08:00:00 - 12:00:00',
    '12:00:00 - 16:00:00',
    '16:00:00 - 20:00:00',
    '20:00:00 - 23:59:59',
)


def index(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)

        auth.login(request, user)
        return HttpResponseRedirect(reverse('reserving'))
    else:
        form = LoginForm()
    users = User.objects.all()
    context = {'title': 'Authorization', 'form': form}
    return render(request, 'space_app/index.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def reserving(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    else:
        today = datetime.datetime.now().date()
        today_reserved_times = []
        today_free_times = []
        dict_res = {}
        spaces = Space.objects.all()
        reservations = Reservation.objects.all()

        for i in range(len(spaces)):
            for j in range(len(reservations)):
                if spaces[i] == reservations[j].space and reservations[j].start.date() == today:
                    today_reserved_times.append(f'{reservations[j].start.time()} - {reservations[j].end.time()}')

            for j in range(len(time_for_reserve)):
                if time_for_reserve[j] not in today_reserved_times:
                    today_free_times.append(time_for_reserve[j])

            dict_res[spaces[i]] = today_free_times
            today_free_times = []
            today_reserved_times = []

        context = {'title': 'Reserving', 'obj_dict': dict_res, 'today': today, 'user': request.user}
        return render(request, 'space_app/reservation_list.html', context)


def approving(request, space_name, reservation_time):
    date_formatter = '%Y-%m-%d %H:%M:%S'
    start = str(datetime.datetime.now().date()) + ' ' + reservation_time[:8]
    end = str(datetime.datetime.now().date()) + ' ' + reservation_time[11:]

    reservation = Reservation()
    reservation.space = Space.objects.filter(name=space_name)[0]
    reservation.user = request.user
    reservation.start = datetime.datetime.strptime(start, date_formatter)
    reservation.end = datetime.datetime.strptime(end, date_formatter)
    reservation.save()
    context = {'title': 'Approving', 'reservation': reservation}
    return render(request, 'space_app/approving.html', context)


def editing(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    elif request.user.position == 'E':
        return HttpResponseRedirect(reverse('reserving'))
    else:
        context = {'title': 'Editing'}
        return render(request, 'space_app/editing.html', context)


class ReservationsListView(ListView):
    model = Reservation
    template_name = 'space_app/reservations-read.html'


class ReservationsCreateView(CreateView):
    model = Reservation
    template_name = 'space_app/reservations-create.html'
    form_class = ReservationEditForm
    success_url = reverse_lazy('reservations-read')


class ReservationsUpdateView(UpdateView):
    model = Reservation
    template_name = 'space_app/reservations-update-delete.html'
    success_url = reverse_lazy('reservations-read')
    form_class = ReservationEditForm


class ReservationsDeleteView(DeleteView):
    model = Reservation
    template_name = 'space_app/reservations-update-delete.html'
    success_url = reverse_lazy('reservations-read')


class SpacesListView(ListView):
    model = Space
    template_name = 'space_app/spaces-read.html'


class SpacesCreateView(CreateView):
    model = Space
    template_name = 'space_app/spaces-create.html'
    form_class = SpaceEditForm
    success_url = reverse_lazy('spaces-read')


class SpacesUpdateView(UpdateView):
    model = Space
    template_name = 'space_app/spaces-update-delete.html'
    success_url = reverse_lazy('spaces-read')
    form_class = SpaceEditForm


class SpacesDeleteView(DeleteView):
    model = Space
    template_name = 'space_app/spaces-update-delete.html'
    success_url = reverse_lazy('spaces-read')

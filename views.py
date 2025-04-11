from django.shortcuts import render, get_object_or_404, redirect
from table_management.models import Table, Reservations


def table_list(request):
    tables = Table.objects.all()
    return render(request,
                  'table_list.html',
                  {'tables': tables})


def reservation_create(request):

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        table_id = request.POST.get('table_id')
        reservation_time = request.POST.get('reservation_time')
        duration_minutes = request.POST.get('duration_minutes')

        # Создание нового бронирования
        Reservations.objects.create(
            customer_name=customer_name,
            table_id_id=table_id,  # id для ForeignKey
            reservation_time=reservation_time,
            duration_minutes=duration_minutes
        )
        return redirect('reservation_list')  # Перенаправление на список бронирований после сохранения

    tables = Table.objects.all()  # Получаем список столов для выбора
    return render(request, 'reservation_form.html', {'tables': tables})


def reservation_list(request):
    """Список всех бронирований"""
    reservations = Reservations.objects.all()
    return render(request,
                  'reservation_list.html',
                  {'reservations': reservations})

def reservation_detail(request, reservation_id):
    """Подробности бронирования"""
    reservation = get_object_or_404(Reservations, id=reservation_id)
    return render(request, 'reservation_detail.html', {'reservation': reservation})


def reservation_edit(request, reservation_id):
    """Редактирование бронирования"""
    reservation = get_object_or_404(Reservations, id=reservation_id)
    if request.method == 'POST':
        reservation.customer_name = request.POST.get('customer_name')
        reservation.table_id_id = request.POST.get('table_id')
        reservation.reservation_time = request.POST.get('reservation_time')
        reservation.duration_minutes = request.POST.get('duration_minutes')
        reservation.save()
        return redirect('reservation_list')

    tables = Table.objects.all()
    return render(request, 'reservation_form.html', {'reservation': reservation, 'tables': tables})


def reservation_delete(request, reservation_id):
    """Удаление бронирования"""
    reservation = get_object_or_404(Reservations, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')

    return render(request, 'reservation_confirm_delete.html', {'reservation': reservation})
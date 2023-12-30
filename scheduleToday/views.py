from django.shortcuts import render, redirect
from .models import Schedule
from .src import Schedule_db
from django.http import HttpResponse

# Create your views here.

def scheduleBoard(request):
    schedules = Schedule_db.get_allSchedule()
    return render(request, 'ScheduleBoard.html', {'schedules': schedules})

def create_schedule_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # 예시: 폼에서 title을 POST로 받아오는 부분
        description = request.POST.get('description', 'None')  # 예시: 폼에서 description을 POST로 받아오는 부분

        # create_Schedule 함수를 호출하여 스케줄을 생성하고 성공 여부를 확인
        if Schedule_db.create_Schedule(title, description):
            return HttpResponse("Schedule created successfully!")
        else:
            return HttpResponse("Failed to create schedule.")
    else:
        return render(request, 'create_schedule_form.html')

def delete_Schedule(request):
    if request.method == 'POST':
        selected_schedule_ids = request.POST.getlist('selected_schedules')
        Schedule_db.delete_ScheduleWithId(selected_schedule_ids)
    return redirect('scheduleBoard')



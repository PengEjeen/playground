from django.shortcuts import render, redirect
from .models import Schedule, Cell
from .src import Schedule_db, Cell_db, recommend_place_src
from .src.recommend_place_src import Place
from django.http import HttpResponse
import ast

# Create your views here.

def scheduleBoard(request):
    schedules = Schedule_db.get_allSchedule()
    return render(request, 'ScheduleBoard.html', {'schedules': schedules})

def create_schedule_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # 폼에서 title을 POST로 받아오는 부분
        description = request.POST.get('description', 'None')  # 폼에서 description을 POST로 받아오는 부분

        # create_Schedule 함수를 호출하여 스케줄을 생성하고 성공 여부를 확인
        if Schedule_db.create_Schedule(title, description):
            return HttpResponse("Schedule created successfully!")
        else:
            return HttpResponse("Failed to create schedule.")
    else:
        return render(request, 'create_schedule_form.html')

def delete_Schedule(request):
    if request.method == 'POST':
        try:
            selected_schedule_ids = request.POST.getlist('schedule_ids')            
        
            #delete cell
            for schedule_id in selected_schedule_ids:
                schedule = Schedule_db.get_ScheduleWithID(schedule_id)
                cell_ids = schedule.cell_ids['ids']
                is_delete = Cell_db.delete_Cell(cell_ids)
                    
            Schedule_db.delete_ScheduleWithID(selected_schedule_ids)

            return redirect('scheduleBoard')

        except Exception as e:
            print(e)
            return redirect('scheduleBoard')

#cell page part
def select_button(request, cell_id):
    return render(request, 'select_button.html', {'cell_id': cell_id})

def recommend_place(request, cell_id):
    if request.method == 'POST':
        #get place id
        place_type = request.POST.get('type')
        place_radius = request.POST.get('radius')
        place_adress = request.POST.get('adress')
        
        #get place
        place = Place(place_type, place_radius, place_adress)
        place_ids = place.get_id()['places']
        
        #get details
        place_details = []
        place_ids_db = []
        for place_id in place_ids:
            temp_place = recommend_place_src.get_placeDetail(place_id['name'])
            place_details.append(temp_place)
            place_ids_db.append(place_id['name'])

        #get cell db with cell_id
        cell = Cell_db.get_CellWithId([cell_id]).first()
        print(cell)
        
        #save mode=recommend_place, place_id=place_ids
        cell.cell_mode = "place_detail"
        cell.place_id['place_id'] = place_ids_db
        cell.save()

        #render select_page
        return render(request, 'place_detail.html', {'places': place_details})

    else:
        return render(request, 'recommend_schedule_form.html', {'cell_id': cell_id})

def place_detail(request,cell_id):
    place_ids = request.GET.getlist('place_ids')[0]
    place_ids_list = ast.literal_eval(place_ids)
    #get details
    place_details = []
    for place_id in place_ids_list:
        temp_place = recommend_place_src.get_placeDetail(place_id)
        place_details.append(temp_place)

    return render(request, 'place_detail.html', {'places': place_details})

###
#cell part
def cell_detail(request, schedule_id):
    try:
        schedule = Schedule_db.get_ScheduleWithID(schedule_id) 
        cell_ids = schedule.cell_ids['ids']
        cells = Cell_db.get_CellWithId(cell_ids)
        return render(request, 'cell_template.html', {'schedule': schedule, 'cells': cells})

    except Schedule.DoesNotExist:
        return HttpResponse("Schedule not found.")

    except Cell.DoesNotExist:
        # Handle the case when cells are not found for the given schedule_id
        cells = None  # You can set it to an empty list or handle it as needed
        return render(request, 'cell_template.html', {'schedule': schedule, 'cells': cells})

def create_cell(request, schedule_id):
    try:
        #save cell db
        cell_id = Cell_db.create_NewCell()

        #update schedule db
        schedule = Schedule_db.get_ScheduleWithID(schedule_id)
        schedule.cell_ids['ids'].append(cell_id)
        schedule.save()
        
        return redirect('cell_detail', schedule_id=schedule_id)
        

    except Exception as e:
        print(e)
        return HttpResponse(e)

def delete_cell(request, schedule_id, cell_id): 
    #delete cell
    if Cell_db.delete_Cell([cell_id]):
        #delete schedule list
        if Schedule_db.delete_cellId(schedule_id, cell_id):
            return redirect('cell_detail', schedule_id=schedule_id)

    else:
        return HttpResponse('why...')
        



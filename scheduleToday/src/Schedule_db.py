from django.db import IntegrityError
from Crypto.Hash import SHA512
from scheduleToday.models import Schedule
from Crypto import Random
import binascii
import base64

SCHEDULE_ID_SIZE = 5

#get all
def get_allSchedule():
    schedules = Schedule.objects.all()
    return schedules

#create Schedule
def create_Schedule(title, description="None"):
    schedule_id_bytes = Random.new().read(SCHEDULE_ID_SIZE)
    schedule_id = base64.b64encode(schedule_id_bytes).decode('utf-8')
    schedule_id = schedule_id[:SCHEDULE_ID_SIZE].replace('/', '@') #/방지용...
    
   
    
    try:
        #Save in database
        schedule = Schedule(
            schedule_id=schedule_id,
            title=title,
            description=description,
            cell_ids={"ids": []}
        )
        schedule.full_clean()  # Validate model fields
        schedule.save()
        print("create success")
        return True
    except IntegrityError as e:
        print(f"Error creating Schedule: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


#delete Schedule
def delete_ScheduleWithID(schedule_ids):
    Schedule.objects.filter(schedule_id__in=schedule_ids).delete()
    return True

#get Schedule with id
def get_ScheduleWithIDs(schedule_id):
    schedule = Schedule.objects.filter(schedule_id__in=schedule_id)
    return schedule 
    

def get_ScheduleWithID(schedule_id):
    try:
        schedule = Schedule.objects.get(schedule_id=schedule_id)
        return schedule
    except Schedule.DoesNotExist:
        # 해당하는 schedule_id를 가진 Schedule이 없을 경우 처리
        return None


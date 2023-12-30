from django.db import IntegrityError
from Crypto.Hash import SHA512
from scheduleToday.models import Schedule

#make sheduel id
def get_schedule_id(title):
    title = title.encode('utf-8')
    hashTitle = SHA512.new(title)
    schedule_id = hashTitle.hexdigest()[:5]
    return schedule_id

#get all
def get_allSchedule():
    schedules = Schedule.objects.all()
    return schedules

#create Schedule
def create_Schedule(title, description="None"):
    schedule_id = get_schedule_id(title)
    
    try:
        #Save in database
        schedule = Schedule(
            schedule_id=schedule_id,
            title=title,
            description=description
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
def delete_ScheduleWithId(schedule_ids):
    Schedule.objects.filter(schedule_id__in=schedule_ids).delete()
    return True

    


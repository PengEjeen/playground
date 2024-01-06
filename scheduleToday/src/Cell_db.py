from django.db import IntegrityError
from Crypto import Random
import base64
from scheduleToday.models import Cell

CELL_ID_SIZE = 7

def get_CellWithId(cell_ids):
    cells = Cell.objects.filter(cell_id__in=cell_ids)
    return cells

#create Schedule
def create_NewCell():
    cell_id_bytes = Random.new().read(CELL_ID_SIZE)
    cell_id = base64.b64encode(cell_id_bytes).decode('utf-8')
    cell_id = cell_id[:CELL_ID_SIZE].replace('/', '@')

    try:
        #Save in database
        cell = Cell(
            cell_id=cell_id,
            cell_mode='button',
            place_id={'place_id': []}
        )
        cell.full_clean()  # Validate model fields
        cell.save()
        print("create success")
        return cell_id
    except IntegrityError as e:
        print(f"Error creating cell") 
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def delete_Cell(cell_ids):
    Cell.objects.filter(cell_id__in=cell_ids).delete()
    return True

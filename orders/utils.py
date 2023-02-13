import datetime
from services.models import ServicesImage

def generate_oder_number(pk):
    current_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    order_number = current_datetime + str(pk)
    return order_number

def serviceimg(service_name):
    pk = 0
    services = {
        '2' : 'Vehicle Repairing',
        '3' : 'Technician',
        '4' : 'Painter',
        '5' : 'Equipment',
        '6' : 'Plumbing',
        '7' : 'Electrician',
        '8' : 'Cleaning',
        '9' : 'Carpenter',
        '10' : 'Grass Cutting',
        '11' : 'Pesticide Spray',
        '12' : 'Planting',
        '13' : 'Car Driver',
        '14' : 'Farming Vehicle Driver',
        '15' : 'Heavy Vehicle Drivers',
    }
    for key,value in services.items():
        if service_name == value:
            pk = key
            break
        else:
            pk = 16
    return pk

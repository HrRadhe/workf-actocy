from django.test import TestCase

# Create your tests here.
# str = 'apple,orange,grape'
# fruits = str.split(',')

# for index,fruit in enumerate(fruits):
#     print(index)

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
name = 'Painter'

print(serviceimg(name))

from django.shortcuts import render
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from django.http import HttpResponse
import csv, io

def uploadView(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('csv'):
            messages.info(request, 'Please Upload the CSV File Only')
            return render(request, 'home.html')
        else:
            messages.info(request, 'File succesfully uploaded')
        
        data_set = new_person.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter= ',', quotechar="|"):
            created = Person.objects.update_or_create(
                name = column[0],
                blood_type = column[1],
                age = column[2],
                date_of_birth = column[3]
            )
    return render(request, 'home.html')
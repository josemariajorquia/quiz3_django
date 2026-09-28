from django.shortcuts import render

# Create your views here.
def Home(request):
    students = [
        {"name": "Jose Jorquia", "age": 20, "course": "BSCS"},
        {"name": "Jonel Pronton", "age": 22, "course": "BSIT"},
        {"name": "Mark Llanora", "age": 23, "course": "BSIS"},
        {"name": "Jhonas San Agustin", "age": 22, "course": "BSHM"},
        {"name": "Mark De Guzman", "age": 21, "course": "BSBA"},
        {"name": "Zedrick Lacuesta", "age": 21, "course": "BSTM"}
    ]
    return render(request, 'main/home.html', {'students': students})

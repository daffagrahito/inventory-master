from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': "daffagrahito's inventory master",
        'name': 'Muhammad Daffa Grahito Triharsanto',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Daffa Grahito Triharsanto',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
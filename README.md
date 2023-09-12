# Inventory Master

### Tugas 2 - Pemrograman Berbasis Platform

`Muhammad Daffa Grahito Triharsanto - 2206820075 - PBP A`
<br><hr>

## Link to App: [daffagrahito's Inventory Master](https://daffagrahitosinventorymaster.adaptable.app/main/)

> Inventory Master adalah sebuah inventori personal dan merupakan *master tool* untuk mengelola inventori-inventori lainnya.

## Cara Mengimplementasikan Aplikasi
- ### Membuat project Django baru
Pertama, saya membuat sebuah direktori baru yang telah terinisialisasi lalu mengaktifkan Virtual Environment. 

Untuk dapat mengaktifkan Virtual Environment, perlu dibuat sebuah direktori `env` yang berisi virtual environmentnya dengan menjalankan command berikut di cmd di dalam direktori sama
```
python -m venv env
```

Setelah itu aktifkan Virtual Environment dengan menjalankan
```
env\Scripts\activate.bat
```

Setelah itu saya membuat `requirements.txt` untuk mempersiapkan dan menginstall *dependencies* seperti Django dan beberapa lainnya.

Isi dari `requirements.txt` adalah sebagai berikut:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Untuk dapat menginstall *dependencies* nya di Virtual Environment saya menjalankan command 
```
pip install -r requirements.txt
```


Kemudian untuk membuat project Django yang baru, saya menjalankan command 
```
django-admin startproject inventory_master .
```

Lalu, saya mengganti bagian **`ALLOWED_HOSTS`** di `settings.py` menjadi `['*']` dan menambahkan `.gitignore` agar tidak menge-*push* file yang tidak diperlukan di GitHub


Setelah ini saya menge-*push* perubahan ini ke GitHub terlebih dahulu

- ### Membuat aplikasi dengan nama `main` pada project

Untuk membuat direktori aplikasi baru bernama `main` perlu menjalankan command 
```
python manage.py startapp main
``` 

dan tidak lupa untuk menambahkan `'main'` pada variable **`INSTALLED_APPS`** di `settings.py`

Setelah itu perlu dibuat direktori `templates` yang berisi sebuah HTML file yaitu `main.html` di dalam direktori main. `main.html` ini adalah halaman yang akan ditampilkan saat mengakses aplikasi

- ### Mengimplementasikan *models* aplikasi `main`

Dalam file `models.py` di dalam direktori `main`, saya mendefinisikan sebuah model sesuai yang diminta
```py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True, null=True)
    category = models.TextField(null=True)
```
Terdapat atribut `name` bertipe `CharField`, `amount` bertipe `IntegerField`, `description` bertipe `TextField`, `date_added` bertipe DateField, dan `category` bertipe `TextField`

Setelah itu perlu dilakukan migration setiap kali melakukan perubahan dalam `models.py` dengan menjalankan command berikut di Virtual Environment:
```
python manage.py makemigrations
```

lalu mengaplikasikan perubahan model yang tercantum dalam file `migrations` ke *database* dengan menjalankan 
```
python manage.py migrate
```

- ### Menghubungkan antara *View* (`views.py`) dengan *Template* (`templates`)
Agar dapat mengubungkan antara *View* dengan *Template* supaya dapat me-*render* tampilan HTML dengan data yang sesuai, pada file `views.py` dalam direktori `main` saya mengonfigurasikan sebuah fungsi `show_main` yang berisi variable yang nantinya akan di-*render* di template seperti dibawah ini :
```py
from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': "daffagrahito's Inventory Master",
        'name': 'Muhammad Daffa Grahito Triharsanto',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```

Lalu saya pastikan variable di template `main.html` dalam kode Django seperti dibawah :
```html
<center><h1>{{ app_name }}</h1></center>
...
<p><b>Name:<b> {{ name }}</p>
<p><b>Class:<b> {{ class }}</p>
```

- ### *Routing* pada project dengan aplikasi `main`
Untuk mengatur routing agar aplikasi `main` dapat diakses melalui web, perlu mengonfigurasi `urls.py` yang dibuat dalam direktori `main` dan mengisinya dengan :
```py
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Lalu agar URL project dapat dapat mengimpor *route* URL aplikasi `main` saya tambahkan kode berikut dalam `urls.py` yang ada dalam direktori utama :
```py
...
from django.urls import path, include
...
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

Lalu apabila saya menjalankan `python manage.py runserver` dalam Virtual Environment, saya dapat melihat halaman main yang saya buat dalam link [http://localhost:8000/main/](http://localhost:8000/main/)

- ### Melakukan Deployment Aplikasi ke *Adaptable*
Terakhir, saya menge-*push* segala perubahan seluruh project saya ke repository GitHub dan melakukan deployment ke *Adaptable* dengan memilih `Python App Template` sebagai *template deployment* dan `PostgreSQL` sebagai *database type* yang akan digunakan, lalu saya sesuaikan dengan versi Python saya gunakan yaitu `3.10` dan menambahkan start command `python manage.py migrate && gunicorn inventory_master.wsgi` serta mencentang `HTTP Listener on PORT`.

## Bagan *request client* ke *web application* berbasis Django beserta responnya
![Bagan Request Client ke Web App](https://media.discordapp.net/attachments/1149089691119915128/1151166399507595414/image0.jpg?width=890&height=464)

Gambar bagan tersebut menjelaskan bahwa setiap HTTP request aplikasi `main` yang masuk akan diproses oleh `urls.py` dan HTTP request diteruskan ke `views.py` yang sesuai. `views.py` akan mendapatkan informasi yang dibutuhkan dari *database* melalui `models.py`. Lalu, HTTP request ini akan di-*return* oleh *view* ke *client* dalam bentuk HTML yang tampilannya seperti template `main.html` sebagai respons.

## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
>Virtual environment digunakan untuk mengisolasi *dependencies* project-project Python, termasuk Django, sehingga perubahan di satu project tidak mempengaruhi proyek lain dan memudahkan manajemen *dependencies*. Meskipun demikian, Kita masih bisa membuat aplikasi web Django tanpa virtual environment. Namun, hal ini dapat menimbulkan beberapa masalah seperti konflik *dependencies* antara project yang berbeda, kesulitan dalam manajemen paket, dan kurangnya portabilitas sehingga project yang dibangun menjadi bermasalah

## Perbedaan MVC, MVT, MVVM
MVC, MVT, dan MVVM adalah tiga pola desain arsitektur yang berbeda yang digunakan dalam pengembangan perangkat lunak.

- MVC (**Model-View-Controller**) adalah pola desain yang memisahkan aplikasi menjadi tiga komponen utama: *Model* yang mengelola data dan *business logic*, *View* yang menampilkan datanya, dan *Controller* yaitu yang mengendalikan aliran data antara Model dan View dan handle input dari user. Ini biasanya digunakan dalam pengembangan aplikasi berbasis server yang contohnya adalah ASP.NET MVC, Spring MVC, dan lain-lain

- MVT (**Model-View-Template**) adalah variasi dari MVC yang digunakan dalam Django. Dalam MVT, Template yang merupakan HTML file bercampur *Django Template Language* menggantikan Controller dan bertindak sebagai perantara antara Model dan View. Template menggambarkan tampilan dan bagaimana data dimasukkan ke dalam tampilan tersebut.

- MVVM (**Model-View-ViewModel**) adalah pola desain yang memisahkan pengembangan *User Interface* dari pengembangan *business logic*. Model merepresentasikan data, *View* yang menampikan *User Interface*, dan *ViewModel* sebagai penengah antara *Model* dan *View* MVVM memungkinkan pemisahan tugas yang membuat pemeliharaan dan pengujian menjadi lebih mudah. MVVM sering digunakan dalam pengembangan aplikasi berbasis *User Interface* seperti *desktop application*.

Perbedaan utama antara ketiganya yaitu :
1. Entry Point:
    - MVC memulai aplikasi dari controller
    - MVT memulai aplikasi dari template
    - MVVM memulai aplikasi dari view

2. Input:
    - Input MVC ditangani oleh controlSler
    - Input MVT ditangani oleh template atau bisa juga view
    - Input MVVM ditangani oleh View

3. Unit testing:
    - Unit testing MVC bisa dikatakan limited karena ketergantungan antara controller, model, dan view.
    - Unit testing MVT bisa dikatakan limited karena memiliki ketergantungan antara template, model, dan view.
    - Unit testing MVVM mudah karena *View* dengan *ViewModel* dependen. Viewmodel bertugas menghubungkan *View* dengan *Model*

4. Relasi:
    - View dengan controller berelasi many to many
    - View dan template berelasi one to one
    - View dan ViewModel berelasi one to many

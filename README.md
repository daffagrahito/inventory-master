# Inventory Master

### Tugas 3 - Pemrograman Berbasis Platform

`Muhammad Daffa Grahito Triharsanto - 2206820075 - PBP A`
<br><hr>

## Mengatur Routing dari `main/` ke`/`
Supaya lebih mengikuti aturan umum yang digunakan dalam pengaturan rute URL di *web application* ini, akan diubah routing yang sebelumnya dari *`main/`* ke *`/`* (root).

Perlu diubah `urls.py` yang ada pada subdirektori inventory_master menjadi seperti ini:
```py
...
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```

## Membuat kerangka dari `views` menggunakan `skeleton`
Kerangka views dengan skeleton (*base template*) diperlukan untuk menjaga konsistensi desain antara halaman web dalam project, memperkecil kemungkinan *code redudancy*, memisahkan logika dari tampilan, dan memungkinkan perubahan desain global dengan mudah.

Perlu dibuat folder `templates` pada root folder dan di isi dengan suatu file HTML yang baru bernama `base.html` sebagai template dasar. Isi dari base.html adalah:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
Lalu pada `settings.py` yang ada dalam subdirektori inventory_master, ubah di bagian list `TEMPLATES` tepatnya di `DIRS` agar `base.html` terdeteksi sebagai suatu template.
```py
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Kode ini ditambahkan menjadi seperti ini
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        }
    }
]
...

```
Lalu pada `templates` yang ada di direktori `main`, `main.html` akan diubah supaya kita menggunakan `base.html` yang ada di direktori `templates` pada root folder menjadi template utamanya
```html
{% extends 'base.html' %}

{% block content %}
    <center><h1>{{ app_name }}</h1>

    <h4>An inventory to manage inventories</h4>
    <hr>

    <p><b>Name:</b> {{ name }}</p>
    <p><b>Class:</b> {{ class }}</p>

    <hr></center>
{% endblock content %}
```

## Implementasi Cara Kerja *Data Delivery*
- ### Membuat input `form`
Input `form` digunakan untuk menginput data baru di aplikasi sehingga nantinya data baru tersebut bisa di tampilkan di halaman utama

Pada direktori `main` buat file baru yaitu `forms.py` yang berisi kode:
```py
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "category"]
```
Lalu pada `views.py`, fungsi `show_main` di ubah menjadi seperti ini:
```py
...
from main.models import Item
...
def show_main(request):
    items = Item.objects.all()

    context = {
        'app_name': "daffagrahito's Inventory Master",
        'name': 'Muhammad Daffa Grahito Triharsanto',
        'class': 'PBP A',
        'items': items,
    }

    return render(request, "main.html", context)
```

- ### Membuat fungsi-fungsi baru pada `views`
Terdapat lima fungsi yang di tambahkan pada `views` agar kita bisa melihat data yang telah kita input pada `form`
1. **Format HTML**,

Agar kita bisa mendapatkan input data, kita membuat fungsi `create_item` di dalam `views.py`. Kode dari fungsi `create_item` adalah sebagai berikut:
```py
...
# Untuk import bisa disesuaikan
from django.shortcuts import render
from main.forms import ItemForm
from django.http import HttpResponseRedirect
from django.urls import reverse
...
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
Lalu perlu juga dibuat template baru dengan membuat file HTML baru bernama `create_item` di dalam direktori `templates` yang terletak di direktori aplikasi `main`. Adapun isi dari `create_item.html` adalah sebagai berikut:
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
``` 
Lalu pada `main.html`, tambahkan tabel data item dan tombol dengan menambahkan kode berikut di dalam `block content`:
```html
...
<table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
            <th>Category</th>
        </tr>
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
                <td>{{item.date_added}}</td>
                <td>{{item.category}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
...
```
2. **Format XML**

Tambahkan sebuah fungsi bernama `show_xml` agar saat kita mengakses URL yang terkait dengan `view` `show_xml`, kita akan mendapatkan respons dalam format XML yang berisi data dari model `Item`. Adapun isi dari fungsi `show_xml` adalah:
```py
# Untuk import bisa disesuaikan
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

3. **Format JSON**

Tambahkan sebuah fungsi bernama `show_json` agar saat kita mengakses URL yang terkait dengan `view` `show_json`, kita akan mendapatkan respons dalam format JSON yang berisi data dari model `Item`. Adapun isi dari fungsi `show_json` adalah sebagai berikut:
```py
# Untuk import bisa disesuaikan
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

4. **Format XML *by* ID**

Tambahkan sebuah fungsi bernama `show_xml_by_id` yang bertujuan untuk mengambil objek dari model Item berdasarkan ID yang diberikan (ID diteruskan sebagai parameter id dalam URL) dan mengembalikannya dalam format XML sebagai `*HTTP response*`. Adapun isi dari fungsi `show_xml_by_id` adalah sebagai berikut:
```py
# Untuk import bisa disesuaikan
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

5. **Format JSON *by* ID**

Tambahkan sebuah fungsi bernama `show_json_by_id` yang bertujuan untuk mengambil objek dari model Item berdasarkan ID yang diberikan (ID diteruskan sebagai parameter id dalam URL) dan mengembalikannya dalam format JSON sebagai `*HTTP response*`. Adapun isi dari fungsi `show_json_by_id` adalah sebagai berikut:
```py
# Untuk import bisa disesuaikan
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- ## Membuat *routing* URL untuk masing-masing `views`
Agar *web application* dapat menentukan bagaimana merespons permintaan dari pengguna berdasarkan URL yang mereka akses, setiap URL akan dihubungkan dengan view dari masing-masing fungsi yang sesuai. Untuk itu perlu ditambahkan semua *path url*nya ke dalam `urls.py` yang ada di direktori `main`. `urls.py` diubah menjadi seperti ini:
```py
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id # Import semua function dari views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```
Lalu, aktifkan `Virtual Environment` di command prompt dan jalankan command `python manage.py runserver`. Setelah itu kunjungi [http://localhost:8000/](http://localhost:8000/). 
Dengan mengakses masing-masing *route* URL yang kita mau, data yang sesuai akan ditampilkan di *web page*.

## Screenshot Akses URL dengan Postman

### 1. Format HTML
![HTML](https://cdn.discordapp.com/attachments/1152952874037428306/1153518855474380890/image.png)
### 2. Format XML
![XML](https://cdn.discordapp.com/attachments/1152952874037428306/1153518949498114140/image.png)
### 3. Format JSON
![JSON](https://cdn.discordapp.com/attachments/1152952874037428306/1153519069585227897/image.png)
### 4. Format XML *by* ID
![XML by ID](https://cdn.discordapp.com/attachments/1152952874037428306/1153519237839736832/image.png)
### 5. Format HTML *by* ID
![JSON by ID](https://cdn.discordapp.com/attachments/1152952874037428306/1153519140305375342/image.png)

## Apa perbedaan antara form `POST` dan form `GET` dalam Django?
Jadi, `Form` digunakan untuk menerima input data dari *user* dengan memasukkan text, memilih opsi, manipulasi *object* dan *controls*, dan lain sebagainya. Adapun terdapat dua *HTTP methods* yaitu `POST` dan `GET`, perbedaan antara keduanya adalah:
- `POST` digunakan untuk mengirim data (file, form data, dan lain lain) ke server untuk diproses, sedangkan `GET` digunakan untuk mengambil data dari server.
- Dengan `POST` jika data berhasil dibuat/dikirim akan me-*return* *HTTP status code* 201, sedangkan dengan `GET` jika data berhasil diambil akan me-*return* *HTTP status code* 200.
- Data `POST` lebih aman daripada data `GET`, karena tidak terlihat di URL. ini karena metode `POST` tidak menampilkan data dalam URL (data hanya dimasukkan ke dalam form dan dikirim sebagai bagian dari *HTTP request*), sementara metode `GET` menampilkan data dalam URL melalui parameter query string.
- Batasan panjang data pada metode `POST` tidak ada batasan dan bisa kita atur sendiri, sedangkan batasan panjang data pada metode `GET` tergantung pada server web, peramban, atau pengaturan server.
## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- **`XML`** digunakan untuk representasi data terstruktur.
- **`JSON`** digunakan untuk pertukaran data ringan dan sering digunakan dalam *web development*.
- **`HTML`** digunakan untuk membangun halaman web yang akan ditampilkan oleh browser.
## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara web aplikasi modern karena sifatnya yang ringan dan mudah dibaca, memungkinkan *developers* untuk merepresentasikan data dengan fleksibel, dan dapat menanamkan struktur data. Selain itu, JSON didukung oleh hampir semua bahasa pemrograman, terintegrasi dengan baik dalam lingkungan web, terutama JavaScript, dan memiliki overhead yang kecil dalam hal ukuran file.

## Implementasi Bonus
Di dalam `views.py` di fungsi `show_main`, hitung jumlah item yang terdaftar dengan menggunakan fungsi `len()`. Implementasinya menjadi sebagai berikut:
```py
def show_main(request):
    items = Item.objects.all()
    total_items = len(items)

    context = {
        'app_name': "daffagrahito's Inventory Master",
        'name': 'Muhammad Daffa Grahito Triharsanto',
        'class': 'PBP A',
        'items': items,
        'total_items': total_items,
    }

    return render(request, "main.html", context)
```
Lalu ditambahkan kode berikut pada template `main.html` untuk menampilkan berapa banyak inventory yang terdaftar.

```html
...
    <p><b>Name:</b> {{ name }}</p>
    <p><b>Class:</b> {{ class }}</p>

    <hr>

    <p>Terdapat {{ total_items }} inventory yang telah dimasukkan</p> <!-- Kode ini ditambahkan-->
    
    <table>
...
```

<hr><hr>

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

## Implementasi Test Lain selain di Tutorial pada `tests.py`
Pada `tests.py` milik saya terdapat sebuah test function yang mengecek apakah value *name* dan *class* te*render* dengan benar di HTML, pengecekan dilakukan dengan mengecek apakah value dari variable *name* dan *class* di test sama dengan name saat di*render* yaitu berisi nama panjang saya dan kelas PBP saya.
```py
def test_name_and_class_are_set_correctly_in_main_template(self):
        name = "Muhammad Daffa Grahito Triharsanto"
        class_name = "PBP A"

        response = Client().get('/main/', {'name': name, 'class': class_name})

        self.assertContains(response, name)
        self.assertContains(response, class_name)
``` 
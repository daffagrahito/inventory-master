# Inventory Master

### Tugas 6 - Pemrograman Berbasis Platform

`Muhammad Daffa Grahito Triharsanto - 2206820075 - PBP A`

> Inventory Master adalah sebuah inventori personal dan merupakan *master tool* untuk mengelola inventori-inventori lainnya.



<details>
<summary> Tugas 5 </summary>

### Tugas 5 - Pemrograman Berbasis Platform

## Implementasi CSS pada Web Application
- ## Menambahkan *library* yang dibutuhkan
Untuk dapat memulai men*design* aplikasi web, kita harus mengimport library yang dibutuhkan seperti Bootstrap CSS dan juga JS. Untuk itu saya tambahkan kode ini pada `<head>` section dalam `base.html` pada direktori `templates` yang ada di direktori `root`.
```html
    <head>
        {% block meta %}
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% endblock meta %}
        <!-- Include Bootstrap CSS from a CDN (Content Delivery Network) -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

        <!-- Include Font Awesome CSS from a CDN (Content Delivery Network) -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

        <!-- Include jQuery library from a CDN -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>

        <!-- Include Popper.js library from a CDN -->
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>

        <!-- Include Bootstrap JavaScript from a CDN -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>

        <!-- Include Bootstrap CSS from a CDN (This line is a duplicate of the first Bootstrap CSS link) -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

        <!-- Include Bootstrap JavaScript from a CDN (This line is a duplicate of the previous Bootstrap JS link) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap/dist/js/bootstrap.min.js"></script>
    </head>
```

- ## Kustomisasi halaman `login` dan `register`
Pada halaman login dan register, ide design saya kurang lebih mirip. Saya mencari template Bootstrap yang ada di internet, lalu saya coba untuk ubah sedikit-sedikit dan merapikannya dalam bentuk yang saya inginkan. Untuk isi kode dari keduanya dapat dilihat dalam folder `main/templates`. Terdapat juga beberapa implementasi CSS murni dalam *internal* dan juga *inline* *code*. Untuk sekarang model ini yang akan saya gunakan dan saya harap kedepannya masih dapat saya *improve*.

- ## Kustomisasi halaman daftar inventori
Pada halaman daftar inventori, saya mengimplementasikan *Card Bootstrap* untuk menampilkan daftar inventorinya disertai *buttons* yang memiliki fungsinya sendiri. Ada satu button tambahan yang belum ada di tugas-tugas sebelumnya yaitu `Show Description` yang berfungsi untuk menampilkan description dari *inventory item* yang menggunakan *Bootstrap modals*, yaitu semacam pop-up berisi informasi apabila kita pakai. Selain itu, saya juga menambahkan *navbar* di bagian atas halaman aplikasi yang terdapat nama app yang berdasarkan username dan juga *logout* button. Berikut *snippet code* saya dalam mengimplementasikan *navbar* dan *Card* pada halaman daftar inventori:
```html
    ...
    <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark">
        <div class="container-fluid">
        <a class="navbar-brand">{{ app_name }}</a>
        <form class="d-flex" role="logout">
            <a href="{% url 'main:logout' %}">
                <button class="btn btn-outline-success" type="button">Logout</button>
            </a>
        </form>
        </div>
    </nav>
    ...
        <div class="card main">
            <div class="card-body d-flex flex-wrap">
                {% for item in items %}
                <div class="card mb-3 item-card">
                    <div class="card-header">
                        {{ item.name }}
                    </div>
                    <div class="card-body">
                        <p><b>Amount:</b> {{ item.amount }}</p> 
                        <p><b>Date Added:</b> {{ item.date_added }}</p>
                        <p><b>Category:</b> {{ item.category }}</p>
                        <div class="btn-group" role="group">
                            <form method="post" action="{% url 'main:increase_amount' item.id %}">
                                {% csrf_token %}
                                <button class="btn btn-success btn-sm mx-1" type="submit">+</button>
                            </form>
                            <form method="post" action="{% url 'main:decrease_amount' item.id %}">
                                {% csrf_token %}
                                <button class="btn btn-success btn-sm mx-1" type="submit">-</button>
                            </form>
                            <form method="post" action="{% url 'main:delete_item' item.id %}">
                                {% csrf_token %}
                                <button class="btn btn-danger btn-sm mx-1" type="submit">Delete</button>
                            </form>
                            <a href="{% url 'main:edit_item' item.pk %}">
                                <button class="btn btn-primary btn-sm mx-1" type="submit">Edit</button>
                            </a>
                            <!-- Button to trigger the modal -->
                            <button class="btn btn-info btn-sm mx-1" data-bs-toggle="modal" data-bs-target="#descriptionModal{{ item.id }}">
                                Show Description
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Modal -->
                <div class="modal fade" id="descriptionModal{{ item.id }}" tabindex="-1" aria-labelledby="descriptionModalLabel{{ item.id }}" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="descriptionModalLabel{{ item.id }}">Description</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                {{ item.description }}
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>       
    ... 
```
Untuk kode lebih lengkapnya dapat dilihat dalam file `main.html` dalam folder `main/templates`.

- ## Kustomisasi halaman *Add New Item* dan *Edit Item*
Pada halaman *Add New Item* dan *Edit Item*, ide design yang saya pakai cukup mirip dan simpel. Form yang di *render* sebagai tabel dimasukkan dalam *Card* dan ditambahkan sedikit CSS untuk warna background dan buttons. Berikut adalah salah satu kode saya dan selengkapnya dapat dilihat dalam file `create_item.html` dan `edit_item.html` dalam folder `main/templates`

`create_item.html`:
```html
{% extends 'base.html' %}

{% block content %}
<div class="container mt-4">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h1 class="card-title">Add New Item</h1>
                </div>
                <div class="card-body">
                    <form method="POST">
                        {% csrf_token %}
                        <table class="table">
                            {{ form.as_table }}
                            <tr>
                                <td></td>
                                <td>
                                    <button type="submit" class="btn btn-primary">Add Item</button>
                                </td>
                            </tr>
                        </table>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    /* Latar belakang */
    html, body {
        background: linear-gradient(to bottom right, white, #8f94fb);
        background-attachment: scroll;
        min-height: 100vh;
        margin: 0;
    }

    /* Tombol Add Item */
    .btn-primary {
        background-color: rgb(60, 60, 60);
        border-color: black;
    }
</style>
{% endblock %}
```

## Manfaat dari setiap element selector pada CSS dan kapan waktu yang tepat untuk menggunakannya.
1. Element Selector, manfaatnya untuk memilih semua elemen dengan jenis tertentu, seperti p untuk paragraf, h1 untuk judul level 1, dan sebagainya. Selector ini memberikan kemampuan untuk *styling* semua elemen dengan jenis yang sama yang ada dalam satu file html dengan gaya yang seragam.

2. ID Selector (#), digunakan untuk memilih elemen dengan atribut id tertentu. Ini memungkinkan kita untuk *styling* atau memanipulasi elemen unik dalam satu halaman. Setiap ID harus unik dalam satu halaman HTML.

3. Class Selector (.), Class selector digunakan untuk memilih elemen dengan atribut class tertentu. Ini memungkinkan kita untuk *styling* atau memanipulasi sekelompok elemen yang memiliki kesamaan dalam tampilan atau perilaku. Elemen dengan class yang sama dapat digunakan berkali-kali dalam satu file HTML.

4. Universal Selector (*), digunakan untuk memilih semua elemen dalam satu file HTML. Ini dapat berguna dalam beberapa situasi ketika kita ingin memberikan *styling* yang umum ke seluruh dokumen.

Waktu yang tepat untuk menggunakan setiap element selector tergantung pada kebutuhan:

- Element Selector: Gunakan saat Anda ingin menggaya atau memanipulasi semua elemen dengan jenis yang sama dalam dokumen Anda, seperti mengatur gaya teks dalam semua paragraf (p).

- ID Selector: Gunakan ketika Anda ingin menggaya atau memanipulasi elemen unik dalam halaman Anda, seperti header utama (#header).

- Class Selector: Gunakan saat Anda ingin menggaya atau memanipulasi sekelompok elemen yang memiliki kesamaan dalam tampilan atau perilaku, seperti tombol dengan class tertentu (.btn).

- Universal Selector: Gunakan dengan hati-hati, jika diperlukan, untuk mengatur gaya umum ke seluruh dokumen. Hindari penggunaan berlebihan agar tidak memengaruhi kinerja atau tampilan yang tidak diinginkan.

## HTML5 Tags
- `<html>`: Tag awal untuk mendefinisikan dokumen HTML.

- `<head>`: Tempat untuk informasi meta dan elemen-elemen lainnya seperti `<title>`.

- `<title>`: Judul dokumen yang akan ditampilkan di bilah judul browser.

- `<meta>`: Informasi meta seperti karakter set dan deskripsi halaman.

- `<link>`: Menghubungkan dokumen dengan file eksternal seperti stylesheet.

- `<style>`: Mendefinisikan gaya CSS di dalam dokumen HTML.

- `<script>`: Mendefinisikan skrip JavaScript.

- `<body>`: Isi utama dokumen HTML.

- `<h1>` hingga `<h6>`: Judul dengan tingkat kepentingan yang berbeda.

- `<p>`: Paragraf teks.

- `<a>`: Hyperlink untuk menghubungkan ke halaman lain atau sumber eksternal.

- `<img>`: Menampilkan gambar.

- `<ul>`: Daftar tak terurut.

- `<ol>`: Daftar terurut.

- `<li>`: Elemen daftar dalam `<ul>` atau `<ol>`.

- `<div>`: Kontainer untuk mengelompokkan elemen.

- `<span>`: Kontainer inline untuk mengelompokkan teks atau elemen kecil.

- `<form>`: Formulir untuk mengumpulkan data dari pengguna.

- `<input>`: Elemen masukan dalam formulir.

- `<textarea>`: Area teks multiline dalam formulir.

## Perbedaan antara *Margin* dan *Padding* pada CSS
| <center> Margin | <center> Padding |
| -- | -- |
| Mengacu pada ruang di luar batas luar elemen. | Mengacu pada ruang di dalam batas elemen, di antara kontennya dan batasnya sendiri |
| Digunakan untuk mengatur jarak antara elemen tersebut dengan elemen-elemen lain di sekitarnya | Digunakan untuk mengatur jarak antara konten elemen dan batas elemen tersebut |
| Margin tidak berwarna atau transparan, sehingga tidak memengaruhi tampilan elemen itu sendiri | Padding memengaruhi tampilan elemen itu sendiri dengan mengatur seberapa dekat kontennya dengan batasnya |
| Dapat digunakan untuk mengatur ruang di antara elemen-elemen dalam tata letak halaman | Digunakan untuk mengatur ruang di antara konten elemen dan batasnya, sehingga memengaruhi ukuran elemen itu sendiri. |

## Perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Perbedaan dari framework CSS Tailwind dan Bootstrap dapat dilihat dari poin-poin berikut:

| <center> Tailwind | <center> Bootstrap |
| -- | -- |
| Tailwind adalah framework CSS *"utility-first,"* yang berarti ia memberikan kelas-kelas CSS kecil yang dapat digunakan untuk membangun komponen-komponen secara lebih fleksibel sesuai *design* yang kita mau | Bootstrap memiliki komponen-komponen siap pakai dengan desain dan tampilan yang telah ditentukan sebelumnya. Jadi kita cukup menambahkan komponen-komponen ini ke project kita dan menggunakannya dengan sedikit penyesuaian |
| Memiliki ukuran yang lebih kecil daripada Bootstrap karena ia hanya menghasilkan CSS yang digunakan pada *project* sesuai kebutuhan, sehingga halaman web jadi lebih ringan | Memiliki ukuran yang lebih besar karena ia memuat sejumlah besar komponen, gaya, dan JavaScript yang dapat digunakan |
| Lebih fleksibel dan memungkinkan untuk menyesuaikan tampilan dengan sangat detail | Lebih kaku dalam hal desain karena komponen-komponennya sudah ditentukan sebelumnya. Menyesuaikan tampilan dapat memerlukan usaha lebih banyak. |
| Memerlukan pembelajaran awal yang lebih panjang karena perlu mengenal dan memahami kelas-kelas utilitasnya | Lebih mudah digunakan untuk pemula karena komponen-komponennya sudah terdefinisi dengan baik. |

Jadi dari perbedaan-perbedaan tersebut dapat kita ambil kapan kita harus menggunakan Bootstrap dan kapan kita harus menggunakan Tailwind.

**Gunakan Bootstrap jika:**

- Memerlukan pembuatan tampilan yang cepat dengan komponen-komponen yang sudah jadi.
- Semisal bekerja dalam tim besar dengan developer yang lebih terbiasa dengan Bootstrap.
- Kustomisasi tampilan tidak menjadi prioritas utama.
- Kita ingin menghemat waktu dalam pengembangan.

**Gunakan Tailwind CSS jika:**

- Ingin tampilan yang sangat disesuaikan dan unik.
- Kita dan tim kita memiliki kebutuhan khusus dalam hal kustomisasi tampilan.
- Ingin menghindari payload CSS yang besar pada proyek Anda.
- Kita dan tim kita siap untuk mempelajari dan menggunakan kelas-kelas utilitas Tailwind.

## Implementasi Bonus
Untuk Implementasi bonus pada aplikasi web saya, saya mengubah bagian class card saya seperti dibawah ini pada `main.html` dalam direktori `main/templates`. Setelah itu saya tinggal kustomisasi dengan internal CSS.
```html
        ...
            <div class="card mb-3 item-card {% if forloop.last %} last-item-card{% endif %}">
        ...
<style>
    ...
    /* Mengatur tampilan samping-sampingan menggunakan Flexbox */
    .item-card {
        background: linear-gradient(to bottom right, white, #8f94fb); /* Ganti dengan warna latar belakang yang Anda inginkan */
        flex: 0 0 calc(50% - 20px); /* 50% lebar, dengan margin sebesar 10px */
        margin: 10px;
    }

    .last-item-card {
        background: linear-gradient(to bottom right, #4e54c8, #8f94fb); /* Ganti dengan warna latar belakang atau properti CSS lainnya yang Anda inginkan */
        color: white; /* Ganti dengan warna teks yang sesuai */
    }
    </style>
{% endblock content %}
```

## App Screenshot
**Halaman Login**:
![Login page](https://cdn.discordapp.com/attachments/1152952874037428306/1158954807223144448/image.png?ex=651e2046&is=651ccec6&hm=7120d40acb745d61058722fde6687a59f9bf84623d172cd71a1f7fae0f5443e2&)

**Halaman Register**
![Register page](https://cdn.discordapp.com/attachments/1152952874037428306/1158954885153292378/image.png?ex=651e2058&is=651cced8&hm=18b2723bc6251ba41bcb51b44e64e569b3c86eeae637c0050cac67e4875ef791&)

**Main App**
![Main App page](https://cdn.discordapp.com/attachments/1152952874037428306/1158955046969540618/image.png?ex=651e207f&is=651cceff&hm=794880ddfe14ee06b418ded0aef3fe187edf4428625395dd95e0fcd20ff36000&)

**Halaman Add New Item**
![Add New item page](https://cdn.discordapp.com/attachments/1152952874037428306/1158955558351671336/image.png?ex=651e20f9&is=651ccf79&hm=524bd023e10e4d2e3e6e106588f975deabffb955ab92f5603ed64e14a9e4ddd5&)

**Halaman Edit Item**
![Edit Item page](https://cdn.discordapp.com/attachments/1152952874037428306/1158955413186818158/image.png?ex=651e20d6&is=651ccf56&hm=6f801945b73300c5dc8d8e56d2fdb880b2df177f33fc77264c2e824f731d863d&)

</details>
<hr>

<details>
<summary>Tugas 4 </summary>

### Tugas 4 - Pemrograman Berbasis Platform

## Mengimplementasikan fungsi *register*, *login*, dan *logout*
- ## Membuat fungsi *register*
Sebelum *user* dapat mengakses aplikasi kita, mereka perlu login agar data inventory mereka tidak tertukar. Sebelum login perlu ada juga register agar mereka yang belum pernah memiliki akun dapat mengakses aplikasi ini. Dalam `main/views.py`, perlu dibuat sebuah fungsi `register` yang menerima `request`. Adapun kodenya seperti ini:
```py
# Sesuaikan importnya
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
...
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Lalu buat sebuah HTML file yang bernama `register.html` di dalam `main/templates` dan nantinya fungsi `register` dalam `views.py` akan me*return* hasil *render* dari `register.html`. Isi dari `register.html` adalah:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register an Account</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

- ## Membuat fungsi *login*
Agar *user* dapat melakukan login dan mengakses aplikasi kita, perlu dibuat fungsi login yang mengautentikasi *credentials* dari *user* sehingga mereka memiliki hak akses ke aplikasi. Perlu ditambahkan fungsi `login_user` pada `views.py` yang mengambil username dan password lalu mengecek apakah user tersebut terdaftar agar bisa ter-*authenticate*.
```py
from django.contrib.auth import authenticate, login
...
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Lalu buat sebuah file HTML lagi bernama `login.html` dalam `main/templates` sebagai interface input data dari user.
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

- ## Membuat fungsi *logout*
Agar user bisa *logout* dari aplikasi, perlu dibuat sebuah fungsi `logout_user` yang mengarahkan *user* kembali ke halaman login supaya data teramankan saat komputer yang sama diakses pengguna lain. Tambahkan fungsi `logout_user` ke dalam `views.py` yang fungsinya berisi:
```py
from django.contrib.auth import logout
...
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Setelah itu pada `main.html` dalam `main/templates` perlu ditambahkan line HTML berikut di bagian setelah button `Add New Item` untuk tombol *logout*nya:
```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
- ## Menambahkan *routing* URL dari ketiga fungsi tersebut
Agar user bisa menggunakan fungsi-fungsi yang kita telah buat, tentunya fungsi perlu di *routing* dengan benar dengan menambahkan path URL ke dalam `urlpatterns` di dalam `main/urls.py`.
```py
# Tambahkan import fungsi register, login_user, dan logout_user dari views
from main.views import register, login_user, logout_user
...
urlpatterns = [
...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

- ## Membatasi *user* agar mengakses aplikasi `main`
Agar *user* tidak sembarang mengakses aplikasi, halaman `main` perlu direstriksi agar *user* perlu login dahulu dan hak akses *user* diatur dengan benar. Dalam `main/views.py` tambahkan import `login_required` dan kode berikut di atas fungsi `show_main` supaya halaman main hanya dapat diakses oleh *user* yang sudah terautentikasi.
```py
from django.contrib.auth.decorators import login_required
...
@login_required(login_url='/login')
def show_main(request):
...
```
Setelah itu lihat hasilnya dengan menjalankan `python manage.py runserver` dalam ***virtual environment***.

## Menerapkan `cookies` pada halaman utama aplikasi
Contoh `cookies` yang dapat diterapkan pada halaman utama aplikasi adalah detail *last login* dari user. Untuk mengimplementasikannya, pastikan logout terlebih dahulu dari aplikasi Django. Lalu buka `views.py` dan update fungsi `login_user` serta tambahkan import yang sesuai di paling atas:
```py
# Sesuaikan penambahan import berikut
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
...
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Ini akan mendapatkan waktu kapan kita terakhir kali login ke akun kita. Lalu update juga fungsi `show_main` dengan menambahkan potongan kode berikut agar informasi cookie *last login* ter*update* saat kita mengakses web:
 ```py
context = {
    'app_name': "daffagrahito's Inventory Master",
    'name': 'daffagrahito,
    'class': 'PBP A',
    'items': items,
    'total_items': total_items,
    'last_login': request.COOKIES['last_login'],
    }
 ```
Lalu, agar cookie `last_login` terhapus saat *user* melakukan `logout`, ubah juga fungsi `logout_user` menjadi seperti ini:
```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Terakhir, tambahkan potongan kode berikut di bagian paling bawah `main.html` yaitu setelah tombol `Add New Item` dan `logout`:
```html
...
<a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>

    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>

    <h5>*session* terakhir login: {{ last_login }}</h5> <!-- Tambahkan ini -->
...
```

## Menghubungkan Model `Item` dengan `User` dan menampilkan detail informasi *user* yang sedang logged in
Agar setiap *user* mempunyai data inventorynya masing-masing dan detail informasi *user* seperti usernamenya sesuai saat ditampilkan pada halaman utama aplikasi, maka kita perlu menghubungkan setiap objek pada `Item` dengan `User` pembuatnya. Untuk itu, perlu ditambahkan kode berikut pada `main/models.py`:
```py
...
from django.contrib.auth.models import User # Pastikan import ditambah di bawah

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # tambahkan ini di atas variable lain
    ...
```
Lalu pada `views.py` ubah fungsi `create_item` dan key `app_name` serta `name` pada `show_main` menjadi seperti ini:
```py
def show_main(request):
    ...
    context = {
        'app_name': request.user.username + "'s Inventory Master",
        'name': request.user.username,
        'class': 'PBP A',
        'items': items,
        'total_items': total_items,
        'last_login': request.COOKIES['last_login'],
    }
    ...
    
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
Terakhir, pastikan untuk menjalankan `python manage.py makemigrations` dalam *virtual environment* lalu tambahkan default value saat ditampilkan prompt error dengan menginput 1 di keduanya. Setelah itu jangan lupa untuk menjalankan `python manage.py migrate`. Jalankan juga `python manage.py runserver` dan lihat perubahannya pada [http://localhost:8000/](http://localhost:8000/)

## Apa itu Django `UserCreationForm`, apa kelebihan dan kekurangannya?
Django `UserCreationForm` adalah salah satu dari banyak *forms* bawaan yang disediakan oleh Django untuk memudahkan pembuatan dan manajemen akun *user* dalam aplikasi web.

- Kelebihan dari Django `UserCreationForm` adalah:

    1. **Kemudahan penggunaan**, yaitu pengintegrasian yang mudah dalam aplikasi web berbasis Django dan dapat mengonfigurasi beberapa opsi sesuai kebutuhan. Form ini juga dibuat mudah untuk mengelola otentikasi dan otorisasi *user* di aplikasi.
    2. **Validasi Otomatis**, Form ini dilengkapi dengan validasi otomatis untuk memastikan bahwa *user* memasukkan data yang benar dan sesuai, seperti verifikasi bahwa *username* yang dimasukkan adalah unik atau bahwa kata sandi memiliki kompleksitas yang cukup.
    3. **Tersedia *Customization***, Kita bisa mendefinisikan `UserCreationForm` sesuai kebutuhan aplikasi kita. Kita bisa mengubah pesan kesalahan, menambahkan validasi tambahan, dan lain sebagainya.

- Kekurangan dari Django `UserCreationForm` adalah:

    1. **Kurangnya Dukungan untuk Data Pengguna Tambahan**, `UserCreationForm` secara default hanya berfokus pada data dasar *user*, seperti nama *user* (username), alamat email, dan kata sandi. Jika kita ingin data *user* tambahan, seperti nomor telepon, alamat, atau hal lainnya, Kita perlu menambahkan bidang-bidang ini secara manual atau membuat formulir pendaftaran kustom yang lebih lengkap.
    2. **Keterbatasan dalam Validasi Kustom**, meskipun dapat menambahkan validasi tambahan, ada keterbatasan dalam sejauh mana kita dapat menyesuaikannya dengan kebutuhan validasi yang sangat spesifik.
    3. **Tidak Memungkinkan Integrasi dengan Layanan Pihak Ketiga**, Jika aplikasi memerlukan otentikasi melalui layanan pihak ketiga seperti *Google*, `UserCreationForm` mungkin tidak langsung mendukung ini. Perlu ditambahkan logika kustom untuk mengintegrasikan otentikasi pihak ketiga dengan formulir pendaftaran.


## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi (*authenthication*) dan otorisasi (*authorization*) adalah dua konsep penting dalam keamanan Django. Autentikasi adalah proses memverifikasi identitas *user*, sedangkan otorisasi adalah proses menentukan tingkat akses yang diberikan kepada *user* tersebut. Ada beberapa perbedaan utama antara autentikasi dan otorisasi. Pertama, autentikasi terjadi sebelum otorisasi. Artinya, *user* harus diautentikasi terlebih dahulu sebelum mereka dapat diotorisasi. Lalu, autentikasi berfokus pada identitas *user* dan memastikan bahwa *user* tersebut sah untuk mengakses aplikasi, sedangkan otorisasi berfokus pada hak akses tertentu yang dapat diakses *user*. Autentikasi penting untuk melindungi data *user* dan informasi yang sensitif. Tanpa autentikasi, orang yang tidak berwenang dapat mengakses data dan fitur yang seharusnya hanya tersedia untuk *user* yang sah. Otorisasi juga penting untuk menjaga keamanan dan privasi data. Meskipun seorang *user* telah diotentikasi, itu tidak berarti mereka harus memiliki akses penuh ke semua fitur atau data dalam aplikasi.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi *user*?
Cookies dalam konteks aplikasi web adalah file informasi kecil yang disimpan di perangkat *user* oleh server web. Jadi, Django menggunakan cookies untuk mengelola data *session* milik *user* dengan mengkonfigurasi sistem sesi di `settings.py`. `Middleware` *session* memastikan *cookie session* dikelola dengan benar. Data *session*, seperti nama *user*, dapat disimpan dalam `request.session`. Penggunaan data *session* tersebut dapat diambil dari `request.session` dalam tampilan. Django secara otomatis mengelola cookie ini, mengirimkannya ke browser *user*, dan mengizinkan server untuk mengidentifikasi dan mengakses data *session* yang sesuai setiap kali *user* mengirimkan permintaan. Pengguna juga dapat menghapus data *session* dengan menghapus entri yang sesuai dari `request.session`. 

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Penggunaan cookies secara default dalam pengembangan web umumnya aman. Namun, ada beberapa risiko potensial yang harus diwaspadai, antara lain:

- **Kebocoran data**, Cookies dapat digunakan untuk menyimpan informasi pribadi, seperti nama pengguna, alamat email, atau kata sandi. Jika cookie ini jatuh ke tangan orang yang tidak bertanggung jawab, informasi tersebut dapat digunakan untuk melakukan penipuan atau kejahatan lainnya.
- **Pelacakan pengguna**, Cookies dapat digunakan untuk melacak aktivitas pengguna di berbagai situs web. Hal ini dapat digunakan untuk menargetkan pengguna dengan iklan atau konten yang relevan, tetapi juga dapat digunakan untuk memantau perilaku pengguna.
- **Interferensi dengan privasi**, Cookies dapat digunakan untuk mengganggu privasi pengguna. Misalnya, cookies dapat digunakan untuk melacak lokasi pengguna atau untuk menyimpan informasi tentang kebiasaan penelusuran pengguna.

Untuk mengurangi risiko-risiko tersebut, pengembang web dapat mengambil langkah-langkah berikut:

- **Gunakan cookies hanya untuk tujuan yang diperlukan**, Jangan menyimpan informasi pribadi di cookies jika tidak perlu.
- **Gunakan cookies dengan aman**, Gunakan metode enkripsi untuk melindungi informasi pribadi yang disimpan di cookies.
- **Berikan informasi kepada pengguna**, Beri tahu pengguna tentang jenis cookies yang digunakan di situs web dan bagaimana cookies tersebut digunakan.

## Implementasi Bonus
Terdapat tombol `+` untuk menambahkan `amount` dari item inventory dan `-` untuk mengurangi `amount` dari item dari inventory. Ada juga button `Delete` yang dapat langsung menghapus item inventory tersebut. Juga, apabila `amount` item berjumlah 1 dan kita mengeklik button `-` maka akan dianggap sebagai hapus item. Adapun fungsi dalam `views.py` dari ketiga tombol tersebut adalah:
```py
...
def increase_stock(request, id):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=id, user=request.user)
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrease_stock(request, id):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=id, user=request.user)
        if item.amount > 1:
            item.amount -= 1
            item.save()
        else:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_item(request, id):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=id, user=request.user)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
...
```
Dalam `main.html` perlu ditambahkan tombol dalam format HTML pada data cell agar action dari user terekam. 
```html
...
    <td>
        <form method="post" action="{% url 'main:increase_stock' item.id %}">
            {% csrf_token %}
            <button type="submit">+</button>
        </form>
    </td>
    <td>
        <form method="post" action="{% url 'main:decrease_stock' item.id %}">
            {% csrf_token %}
            <button type="submit">-</button>
        </form>
    </td>
    <td>
        <form method="post" action="{% url 'main:delete_item' item.id %}">
            {% csrf_token %}
            <button type="submit">Delete</button>
        </form>
    </td>
...
```
Lalu juga perlu ditambahkan URL mapping dari `urls.py` ke `views.py` 
```py
# Sesuaikan importnya
...
from main.views import increase_stock, decrease_stock, delete_item
...
urlpatterns = [
    ...
    path('increase_stock/<int:id>/', increase_stock, name='increase_stock'),
    path('decrease_stock/<int:id>/', decrease_stock, name='decrease_stock'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
]
```

## Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat
Berikut Screenshot halaman utama untuk dua akun *user* berbeda:

akun: daffagrahito
![Gambar1](https://cdn.discordapp.com/attachments/1152952874037428306/1155947241857617981/image.png)

akun: daffaG
![Gambar2](https://cdn.discordapp.com/attachments/1152952874037428306/1155947091714121860/image.png)
</details>
<hr>
<details>

<summary> Tugas 3 </summary>

### Tugas 3 - Pemrograman Berbasis Platform

## Perubahan Implementasi Aplikasi
- ## Mengatur Routing dari `main/` ke `/`
Supaya lebih mengikuti aturan umum yang digunakan dalam pengaturan rute URL di *web application* ini, akan diubah routing yang sebelumnya dari *`main/`* ke *`/`* (root).

Perlu diubah `urls.py` yang ada pada subdirektori inventory_master menjadi seperti ini:
```py
...
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```

- ## Membuat kerangka dari `views` menggunakan `skeleton`
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
Lalu pada `main.html`, tambahkan tabel data item dan tombol dengan menambahkan kode berikut di dalam `block content` untuk menambahkan detail data dan tombol untuk input `form` nya:
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
Dengan begitu, HTML akan di *render* oleh fungsi `show_main` sebelumnya lalu menampilkan sebuah web page dalam bentuk HTML

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
Agar *web application* dapat menentukan bagaimana merespons permintaan dari *user* berdasarkan URL yang mereka akses, setiap URL akan dihubungkan dengan view dari masing-masing fungsi yang sesuai. Untuk itu perlu ditambahkan semua *path url*nya ke dalam `urls.py` yang ada di direktori `main`. `urls.py` diubah menjadi seperti ini:
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
</details>
<hr>

<details>
<summary> Tugas 2 </summary>

### Tugas 2 - Pemrograman Berbasis Platform

## Link to App: [daffagrahito's Inventory Master](https://daffagrahitosinventorymaster.adaptable.app/main/)

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
Virtual environment digunakan untuk mengisolasi *dependencies* project-project Python, termasuk Django, sehingga perubahan di satu project tidak mempengaruhi proyek lain dan memudahkan manajemen *dependencies*. Meskipun demikian, Kita masih bisa membuat aplikasi web Django tanpa virtual environment. Namun, hal ini dapat menimbulkan beberapa masalah seperti konflik *dependencies* antara project yang berbeda, kesulitan dalam manajemen paket, dan kurangnya portabilitas sehingga project yang dibangun menjadi bermasalah

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
    - Input MVC ditangani oleh controller
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
</details>
---
 
![SIMALAB_logo](lampiran/logo.png)

---
[Deskripsi Aplikasi](#-deskripsi-aplikasi) | [Lingkungan Pengembangan](#-lingkungan-pengembangan) | [User Research and Analysis](#-user-research-and-analysis) | [Sistem Design](#-sistem-design) | [Implementation and Unit Testing](#-implementation-and-unit-testing)| [Deployment](#-deployment) | [Saran](#-saran) | 
:---:|:---:|:---:|:---:|:---:|:---:|:---:

---

## 💡 Deskripsi Aplikasi
__Simalab IPB__
<p align="justify"> Merupakan sebuah sistem manajemen lab internal yang membantu penanggung jawab dalam dalam mengelola laboratorium, serta mahasiswa IPB yang ingin menggunakan lab untuk kebutuhan penelitian. Dalam input datanya, Simalab IPB menggunakan API IPB, untuk mendapatkan data pengguna mencakup pegawai dan mahasiswa untuk SSO. Sedangkan data-data inventaris dan kegiatan lab akan diinput mandiri oleh admin lab. Data tersebut kemudian akan disimpan pada sebuah database baru Simalab IPB, dan dikembangkan sebagai API Simalab.</p>

__Output dari Simalab IPB__
<p align="justify"> Diharapkan dapat membantu aktivitas dan manajemen lab IPB khususnya dalam melayani peminjaman laboratorium, memantau ketersediaan alat laboratorium, melakukan rekap bahan dan alat yang tersedia, dan mengelola jadwal pemakaian laboratorium.</p>

---

## 🚧 Lingkungan Pengembangan

__Software__
```
- Google Cloud Product VM Instances
    - n1-standard-2 (2 vCPUs, 7.5 GB memory)
    - asia-southeast2-a 
    - Ubuntu 20.04.2.0 LTS
- Cloudflare
- Windows 10 64 bit
- Sublime Text v3.2.2    
- Visual Code Studio v1.57
- Figma
```
__Hardware__
```
- i5-1135G7 @ 2.40 Ghz ( 8 CPUs)
- 8GB RAM
```
__Tech Stack__
```
- Frontend  : NextJS dan Material UI for React
- Backend   : Django 3.2.4 , djangorestframework 3.12.4 , SQLite database  
- Server    : Nginx/1.18.0
```
---

## 🙋 User Research and Analysis

__Desk Research__

<p align="justify"> Kami melakukan literasi terhadap penelitian terdahulu sesuai dengan permasalahan yang ingin kami solve. Selain itu, research kami awali dengan melakukan observasi terhadap kemungkinan masalah yang dapat kami selesaikan. Dari beberapa topik yang kami kumpulkan, kami memilih untuk memfokuskan topik mengenai alur peminjaman laboratorium di IPB, khususnya pada laboratorium FMIPA basah. 
Fokus kami adalah menggali lebih dalam mengenai hal yang dibutuhkan oleh para laboran khususnya untuk membantu efektifitas kinerja mereka. Setelah literasi dilakukan kami mendapatkan beberapa asumsi terkait, yakni mengenai prosedur peminjaman laboratorium.</p>

__In Depth Interview__

<p align="justify"> Kami menetapkan sampel yakni <code> <b> 3 orang tendik laboran</b> </code>, masing-masing merupakan laboran dari <code> <b>laboratorium kimia, laboratorium biologi dan laboratorium biokimia</b> </code>. Kami mengumpulkan kontak laboran tersebut melalui literasi pada web departemen terkait di IPB lalu menanyakan kontak pada rekan mahasiswa yang berkuliah di departemen terkait. Kami melakukan <code> <b> interview by phone ataupun validasi melalui chat dengan laboran selaku narasumber</b> </code>. </p>

Berikut tujuan dari interview yang kami lakukan:
1. Mengetahui alur prosedur peminjaman dan pemakaian lab pada departemen terkait.
2. Mengetahui cara laboran melakukan manajemen laboratorium pada departemen terkait.
3. Mengetahui kendala laboran melakukan manajemen laboratorium departemen terkait.

<p align="justify"> Setelah kami melakukan interview dengan tujuan untuk menggali pain yang dirasakan oleh laboran. Kami mendapatkan insight bahwa <code> <b> 2 dari 3</b> </code> laboran yang kami wawancarai sepakat bahwa mereka mengalami kesulitan dalam menjelaskan keterangan dari alat-alat yang tersedia di lab dikarenakan jumlahnya sangat banyak, dan <code> <b> ketiganya</b> </code> berpendapat bahwa belum tersedia manajemen data alat dan bahan Lab secara digital di laboratorium mereka, maupun terpusat dari IPB University.  Mayoritas kegiatan peminjaman lab pun diawali dengan pengisian form yang disesuaikan dengan aturan departemen masing-masing.</p>

**User Story**
> Sebagai seorang laboran di IPB saya ingin sebuah wadah yang dapat membantu saya menginformasikan **keterangan dan ketersediaan stok** bahan dan peralatan di laboratorium. Serta membantu request **peminjaman lab**. Agar para mahasiswa dapat melakukan peminjaman lab secara terstruktur, serta mahasiswa dapat mengetahui informasi ketersediaan alat bahan serta peralatan di lab tanpa harus bertanya kepada saya terlebih dahulu.

**Persona** |
------------ |
![persona](lampiran/persona.png) |

**Solusi**

<p align="justify"> Menilik dari pengamatan kami mengenai fakta terkait alur peminjaman serta Manajemen data pada laboratorium di IPB University, khususnya pada laboratorium FMIPA basah (Kimia, Biologi dan Biokimia ). Kami mendapatkan beberapa chance untuk melakukan sebuah perbaikan dalam sisi manajemen penyimpanan data dan keefektifan alur peminjaman lab. Adapun rancangan sistem yang kami tawarkan, memiliki fitur berupa : </p>
   
1. Melakukan pendaftaran request peminjaman laboratorium.
2. Melakukan pencarian alat dan bahan yang tersedia di laboratorium terkait
3. Melihat jumlah stok alat dan bahan yang tersedia.

<p align="justify"> Tentunya sistem ini akan disesuaikan dengan kebutuhan pada lab departemen terkait dan manajemen data laboratorium dikelola oleh admin yang bersangkutan. </p>

---

## 🌐 Sistem Design

**Use Case Diagram** | 
------------ |
 ![usecase](lampiran/usecase.png) |


 **Activity diagram** | 
------------ |
 ![Activity](lampiran/Activity_Diagrams.png) |
[Link to Activity Diagram on figma](https://www.figma.com/file/a7teoauijvA6np4MsRLbMR/PSBO-Kelompok-5?node-id=5%3A12) |


 **Class diagram**| 
------------ |
 ![class](lampiran/class.png) |


 **Entity Relationship Diagram** | 
------------ |
[Link to Entity Relational](ipb.link/psbo-entity-kel5) |


 **Arsitektur sistem** | 
------------ |
 ![arsitektur](lampiran/arsitektur.png) |

---

## 👾 Implementation and Unit Testing


**Konsep OOP yang Digunakan**
   ***Class***|
--------------|   

Class merupakan *blueprint* dari objek yang mendefinisikan properti (sifat) dan method (perilaku) dari suatu objek. Pada implementasi sistem, kami menggunakan class untuk membuat model, view dan serializer. Terdapat total 53 class yang dibuat pada sistem.

contoh penerapan:
```
class Laboratorium(models.Model):
    id_labor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    ruangan = models.CharField(max_length=100, blank=False, null=False)
    departemen = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.ruangan
```


***Object***|
--------------|   

Objek adalah suatu entitas yang memiliki sifat atau karakter dan perilaku tertentu. Contohnya adalah kucing, mobil, manusia, dll. 

contoh penerapan:
```
user_att = MhsSerializer()
lab_att = laborSerializer()
queryset = AlatLab.objects.all()
```


   ***Abstraction***|
--------------|

Abstraction adalah teknik untuk hanya menampilkan informasi yang perlu ditampilkan pada suatu objek, informasi-informasi yang tidak perlu tidak akan ditampikan. Salah satu model yang dibangun sebagai abstract model adalah User.
```
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    username = models.CharField(max_length=32, blank=False, null=False, unique=True)
    
    is_mahasiswa = models.BooleanField(default=False)
    is_adminLab = models.BooleanField(default=False)
```

   ***Polymorphism***|
--------------|

Polymorphism merupakan konsep oop dimana class memiliki banyak "bentuk" method yang berbeda, meskipun namanya sama. Penerapan hal ini pada sistem salah satunya pada serializer, dimana terdapat beberapa method yang sama digunakan pada class yang ada.

contoh penerapan:
```
class alatSerializer(serializers.ModelSerializer):
    kategori_id = kategoriSerializer()
    lab_id = laborSerializer()
    class Meta:
        model = AlatLab
        fields = ('id_alat','NamaAlat','Quantity','SubInv','gambarAlat','kategori_id','lab_id')
    def create(self, validated_data):
        contact_data = validated_data.pop('kategori_id')  
        
 ....
 
 class submisiSerializer(serializers.ModelSerializer):
    user_id = MhsSerializer()
    ruangan_id = laborSerializer()
    class Meta:
        model = Form_Submisi
        fields = ('id_form','judulPenelitian','no_hp','dosbing','date_form','date_peminjaman','file1','file2','Verifikasi','Status','user_id','ruangan_id')
    def create(self, validated_data):
        contact_data = validated_data.pop('ruangan_id')  
```

**Tipe Desain Pengembangan**

```
   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

**Fitur dan Tampilan Aplikasi**

   ***Login Page***|
--------------|   
 ![Login](lampiran/Login.jpg) |

---

   ***Dashboard User***|
--------------|   
 ![dashboard](lampiran/dashboard_user.png) |

---

   ***Informasi Peralatan Lab***|
--------------|   
 ![info](lampiran/peralatan_lab.png) |

---

   ***Form Peminjaman***|
--------------|   
 ![form](lampiran/form_peminjaman.png) |

---

   ***Dashboard Admin***|
--------------|   
 ![admin](lampiran/dashboard_admin.png) |

---

   ***Manage , Verfikasi Request Peminjaman***|
--------------|   
 ![manage](lampiran/Manage.png) |

---

   ***Manage Inventaris Lab***|
--------------|   
 ![manage](lampiran/upload_bahan.png) |

---

---


## 🚀 Deployment

**Website SIMALAB IPB**

https://simalab.bintangfikriguska.my.id

**Endpoint SIMALAB API**

| Endpoint API | Fungsi | Method |
| :---         | :---  | :---   |
| https://api-simalab.bintangfikriguska.my.id/api-token-auth/       | Create Token                              | POST                      |
| https://api-simalab.bintangfikriguska.my.id/orang/				            | Read data User                            | GET						                 | 
| https://api-simalab.bintangfikriguska.my.id/mahasiswa/			         | Read data Mahasiswa                       | GET						                 | 
| https://api-simalab.bintangfikriguska.my.id/pegawai/				          | Read data Pegawai                         | GET						                 | 
| https://api-simalab.bintangfikriguska.my.id/lab/					             | CRUD data lab                             | GET,POST,PATCH,PUT,DELETE | 
| https://api-simalab.bintangfikriguska.my.id/kategoriAlat/			      | CRUD data kagetori alat                   | GET,POST,PATCH,PUT,DELETE	| 
| https://api-simalab.bintangfikriguska.my.id/alat/					            | Read data alat+related_FK						           | GET                       | 
| https://api-simalab.bintangfikriguska.my.id/CUDalat/				          | Create,Delete,Update alat		               | POST,PATCH,PUT,DELETE     | 
| https://api-simalab.bintangfikriguska.my.id/submisiPeminjaman/	   | Read data Form Peminjaman + related FK				| GET                       | 
| https://api-simalab.bintangfikriguska.my.id/CUDsubmisiPeminjaman/	| Create,Delete,Update data Form Peminjaman	| POST,PATCH,PUT,DELETE     | 
| https://api-simalab.bintangfikriguska.my.id/jadwalPeminjaman/		   | CRUD jadwal peminjaman terverifikasi	     | GET,POST,PATCH,PUT,DELETE | 							
| https://api-simalab.bintangfikriguska.my.id/templateForm/			      | CRUD template berkas form	                | GET,POST,PATCH,PUT,DELETE | 

---

## 💬 Saran

---

## 👨‍👩‍👦‍👦 Developer
<table>
    <thead>
        <tr>
            <th></th>
            <th>Nama</th>
            <th>Nim</th>
            <th>Role</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Aldi Oktaviana Hidayat</td>
            <td>G64180005</td>
            <td>Frontend</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Bintang Fikriguska</td>
            <td>G64180024</td>
            <td>Backend</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Rafiandi Ammar Putra</td>
            <td>G64180072</td>
            <td>UI Designer,Front end</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Annisa Faradila</td>
            <td>G64180074</td>
            <td>UX Research , UI Designer</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Alvin Ferdiansyah</td>
            <td>G64180079</td>
            <td>Backend, Project Manager</td>
        </tr>
    </tbody>
</table>

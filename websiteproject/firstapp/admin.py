from django.contrib import admin
from .models import Post

admin.site.register(Post)

'''Untuk membuat model kita terlihat di halaman admin, kita perlu mendaftarkan model dengan admin.site.register(Post)'''

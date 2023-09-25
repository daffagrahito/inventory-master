from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, \
    show_json_by_id, register, login_user, logout_user, increase_stock, decrease_stock, delete_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase_stock/<int:id>/', increase_stock, name='increase_stock'),
    path('decrease_stock/<int:id>/', decrease_stock, name='decrease_stock'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
]
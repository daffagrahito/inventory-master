from django.urls import path
from main.views import create_product_flutter, show_main, create_item, show_xml, show_json, show_xml_by_id, \
    show_json_by_id, register, login_user, logout_user, increase_amount, decrease_amount, show_json_user, \
    delete_item_ajax, edit_item, get_item_json, create_ajax

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
    path('increase-amount/<int:id>/', increase_amount, name='increase_amount'),
    path('decrease-amount/<int:id>/', decrease_amount, name='decrease_amount'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('get-item-json/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
from django.urls import path
from .views import pepero_letter_detail, pepero_letter_list, pepero_make_choco_view, pepero_make_letter_view, pepero_make_deco_view,pepero_make_sauce_view,pepero_make_start_view,pepero_make_home_view,pepero_make_end_view,pepero_make_ing_view

app_name = 'pepero'

urlpatterns = [
    path('', pepero_make_home_view, name='pepero_home'),
    path('start/', pepero_make_start_view, name='pepero_start'),
    
    path('choco/', pepero_make_choco_view, name='pepero_choco'),
    path('sauce/', pepero_make_sauce_view, name='pepero_sauce'),
    path('deco/', pepero_make_deco_view, name='pepero_deco'),
    path('letter/', pepero_make_letter_view, name='pepero_letter'),
    
    path('end/', pepero_make_end_view, name='pepero_end'),
    path('ing/', pepero_make_ing_view, name='pepero_ing'),

    path('list/', pepero_letter_list, name='pepero_list'),
    path('detail/', pepero_letter_detail, name='pepero_detail'),
]
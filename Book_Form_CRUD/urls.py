from django.urls import path
from Book_Form_CRUD.views import index, add, update, delete

# here it's your apps urls
urlpatterns = [
    path('', index, name='index' ),
    path('add/', add, name='add-book' ),
    path('update/<int:book_id>/', update),
    path('delete/<int:book_id>/', delete),
]
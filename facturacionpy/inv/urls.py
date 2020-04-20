from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaRemove, SubCategoriaView, \
SubCategoriaNew, SubCategoriaEdit



urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/remove/<int:pk>', CategoriaRemove.as_view(), name='categoria_remove'),
    
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
]
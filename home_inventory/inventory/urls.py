from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/item', views.ItemDetailView.as_view(), name='item_detail'),
    path('<int:pk>/item/update',
         views.ItemUpdateView.as_view(),
         name='item_update'),
    path('item/list/', views.ItemListView.as_view(), name='item_list'),
    path('item/new/', views.NewItemView.as_view(), name='new_item'),
    path('<int:pk>/container',
         views.ContainerDetailView.as_view(),
         name='container_detail'),
    path('container/list/',
         views.ContainerListView.as_view(),
         name='container_list'),
    path('container/tree/',
         views.ContainerTreeView.as_view(),
         name='container_tree'),
    path('container/new/',
         views.NewContainerView.as_view(),
         name='new_container'),
    path('<int:pk>/container/update',
         views.ContainerUpdateView.as_view(),
         name='container_update'),
]
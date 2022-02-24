from django.urls import path

from final.recipe.views import home_page, create, edit_recipe, delete_recipe, details_recipe

urlpatterns = [
    path('', home_page, name='home'),
    path('create/', create, name='create'),
    path('edit/<int:id>', edit_recipe, name='edit recipe'),
    path('delete/<int:id>', delete_recipe, name='delete recipe'),
    path('details/<int:id>', details_recipe, name='details recipe')
]

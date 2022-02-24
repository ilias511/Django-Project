from django.shortcuts import render, redirect

from final.recipe.models import Recipe
from django import forms


class Create_recipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class EditRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipe(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()

    def __init__(self, *args, **kwargs):
        super(DeleteRecipe, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['disabled'] = True
        self.fields['image_url'].widget.attrs['disabled'] = True
        self.fields['description'].widget.attrs['disabled'] = True
        self.fields['ingredients'].widget.attrs['disabled'] = True
        self.fields['time'].widget.attrs['disabled'] = True

    class Meta:
        model = Recipe
        fields = '__all__'


def get_recipes():
    recipe = Recipe.objects.all()
    if recipe:
        return recipe


def home_page(request):
    get_recipe = get_recipes()

    context = {
        'recipes': get_recipe
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        created_recipe = Create_recipe(request.POST)
        created_recipe.save()
        return redirect('home')
    else:
        created_recipe = Create_recipe()

    context = {'recipe_create': created_recipe}

    return render(request, 'create.html', context)


def edit_recipe(request, id):
    get_rep = Recipe.objects.get(id=id)

    if request.method == 'POST':
        created_recipe = EditRecipe(request.POST, instance=get_rep)
        created_recipe.save()
        return redirect('home')
    else:
        created_recipe = EditRecipe(instance=get_rep)

    context = {'recipe_create': created_recipe, 'get': get_rep}

    return render(request, 'edit.html', context)


def delete_recipe(request, id):
    get_rep = Recipe.objects.get(id=id)

    if request.method == 'POST':
        created_recipe = DeleteRecipe(request.POST, instance=get_rep)
        created_recipe.save()
        return redirect('home')
    else:
        created_recipe = DeleteRecipe(instance=get_rep)

    context = {'recipe_delete': created_recipe, 'get': get_rep}

    return render(request, 'delete.html', context)


def details_recipe(request, id):
    get_rep = Recipe.objects.get(id=id)

    context = {'get': get_rep}

    return render(request, 'details.html', context)

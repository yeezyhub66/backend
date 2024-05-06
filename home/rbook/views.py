from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":

        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get ('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_instruction = data.get ('recipe_instruction')
        print(recipe_image)
        print (recipe_instruction)
        print (recipe_description)
        print (recipe_name)

    else:
        return render(request,'recipe.html',{})

    
    return render(request,'recipe.html',{})
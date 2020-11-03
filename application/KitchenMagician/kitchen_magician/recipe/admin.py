from django.contrib import admin

from .models import RecipeTest

from .models import Recipe
from .models import RecipeType
from .models import RecipeTypeItem
from .models import RecipeIngredient
from .models import RecipeIngredientItem
from .models import RecipeInformation
from .models import RecipeInstruction
from .models import RecipeImage
from .models import RecipeVideo
from .models import RecipeFavorite
from .models import RecipeUpvote

admin.site.register(RecipeTest)

admin.site.register(Recipe)
admin.site.register(RecipeType)
admin.site.register(RecipeTypeItem)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeIngredientItem)
admin.site.register(RecipeInformation)
admin.site.register(RecipeInstruction)
admin.site.register(RecipeImage)
admin.site.register(RecipeFavorite)
admin.site.register(RecipeUpvote)
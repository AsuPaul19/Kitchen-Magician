from django.contrib import admin

# Jeff's
from .models import RecipeTest
admin.site.register(RecipeTest)


from .models import Recipe
from .models import RecipeCourse
from .models import RecipeCourseItem
from .models import RecipeIngredient
from .models import RecipeIngredientItem
from .models import RecipeInformation
from .models import RecipeInstruction
from .models import RecipeImage
from .models import RecipeVideo
from .models import RecipeFavorite
from .models import RecipeUpvote
from .models import RecipeComment
from .models import RecipeOccasion
from .models import RecipeOccasionItem
from .models import RecipeDiet
from .models import RecipeDietItem
from .models import RecipePreparationTime
from .models import RecipePreparationTimeItem
from .models import RecipeQuantityServe


admin.site.register(Recipe)
admin.site.register(RecipeCourse)
admin.site.register(RecipeCourseItem)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeIngredientItem)
admin.site.register(RecipeInformation)
admin.site.register(RecipeInstruction)
admin.site.register(RecipeImage)
admin.site.register(RecipeVideo)
admin.site.register(RecipeFavorite)
admin.site.register(RecipeUpvote)
admin.site.register(RecipeComment)
admin.site.register(RecipeOccasion)
admin.site.register(RecipeOccasionItem)
admin.site.register(RecipeDiet)
admin.site.register(RecipeDietItem)
admin.site.register(RecipeQuantityServe)
admin.site.register(RecipePreparationTime)
admin.site.register(RecipePreparationTimeItem)
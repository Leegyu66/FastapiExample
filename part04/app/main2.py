from fastapi import FastAPI, APIRouter, Query
from schemas import RecipeCreate, Recipe
from recipe_data import RECIPES

app = FastAPI(title = "Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.post("/recipe/")
def add_recipe(*, recipe_in: RecipeCreate):
    new_recipe_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id = new_recipe_id,
        label = recipe_in.label,
        source = recipe_in.source,
        url = recipe_in.url
    )
    RECIPES.append(recipe_entry.dict())

    return recipe_entry

@api_router.get("/recipe_check/")
def check_recipe(*, keyword):
    # result = [recipe for recipe in RECIPES]
    result = filter(lambda recipe: keyword.lower() in recipe['label'].lower(), RECIPES)
    return {"result": list(result)}

app.include_router(api_router)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
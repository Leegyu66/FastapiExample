from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates

from typing import Optional, Any
from pathlib import Path

from schemas import RecipeSearchResults, Recipe, RecipeCreate
from recipe_data import RECIPES

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/", status_code=200)
def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "recipes": RECIPES},
    )

@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> Any:
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {recipe_id} not found"
        )
    
    return result[0]


@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    *,
    keyword: Optional[str] = Query(None, min_length=3, examples="chicken"),
    max_results: Optional[int] = 10,
) -> dict:
    if not keyword:
        return {"results": RECIPES[:max_results]}
    
    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}

@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> dict:
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url
    )
    RECIPES.append(recipe_entry.dict())

    return recipe_entry

app.include_router(api_router)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
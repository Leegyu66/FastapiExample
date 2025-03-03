from typing import Sequence
from pydantic import BaseModel, HttpUrl 


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl

# raw_recipe = {'id': 1, 'label': 'Lasagna', 'source': 'Grandma Wisdom'}
# structured_recipe = Recipe(**raw_recipe)


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int
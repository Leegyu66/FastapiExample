from pydantic import BaseModel, HttpUrl
from typing import Sequence


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl

class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]

class RecipeCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int

# class Car(BaseModel):
#     brand: str
#     color: str
#     gears: int

# class ParkingLot(BaseModel):
#     cars: List[Car]
#     spaces: int

if __name__=="__main__":
    raw_recipe = {'id': 1, 'label': 'Lasagna', 'source': 'Grandma Wisdom'}
    structured_recipe = Recipe(**raw_recipe)
    print(structured_recipe.id)

    '''
    이렇게 dictionary 대신 BaseModel 로 정의했을 때의 이점
    1. request, response data 를 검증할 때
    2. 복잡한 데이터 구조 검증
    3. 확장성
    4. Python class 와 작동
    5. 빠르다
    '''
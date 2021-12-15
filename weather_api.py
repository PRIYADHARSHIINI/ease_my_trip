from typing import Optional

import fastapi

from models.   loction import Location

router = fastapi.APIRouter()


@router.get('/api/pythonProject1')
def do_i_need_an_pythonProject1(location: Location):
    return location
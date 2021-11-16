from typing import Optional
from typing import Optional

import fastapi

router = fastapi.APIRouter()

@router.get('/api/weather/{city}')
def weather(city: str, state: str, country: str = "US", units: Optional[str] = 'metric'):
    return "Some report" + city

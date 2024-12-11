from pydantic import BaseModel
from typing import Optional

class PredictionRequest(BaseModel):
    bedrooms: float
    baths: float
    size: float
    bed_bath_ratio: float
    price_per_sqft: float
    luxury_index: float
    FECHS_2: Optional[int] = 0
    Attock: Optional[int] = 0
    Faisalabad: Optional[int] = 0
    Gujranwala: Optional[int] = 0
    Islamabad: Optional[int] = 0
    Karachi: Optional[int] = 0
    Lahore: Optional[int] = 0
    Multan: Optional[int] = 0
    Murree: Optional[int] = 0
    Peshawar: Optional[int] = 0
    Quetta: Optional[int] = 0
    Rawalpindi: Optional[int] = 0
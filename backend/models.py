from pydantic import BaseModel, Field
from typing import Optional


class ProjectRequest(BaseModel):
    plot_width: float = Field(gt=0)
    plot_length: float = Field(gt=0)

    unit: str = "ft"

    city: str
    building_type: str = "residential"

    floors: Optional[int] = Field(default=None, ge=1)

    bedrooms: Optional[int] = Field(default=None, ge=0)
    bathrooms: Optional[int] = Field(default=None, ge=0)

    car_parking: Optional[int] = Field(default=None, ge=0)

    drawing_room: Optional[bool] = None
    tv_lounge: Optional[bool] = None
    kitchen: Optional[bool] = None
    dining_room: Optional[bool] = None
    store: Optional[bool] = None
    servant_room: Optional[bool] = None

    special_requirements: Optional[str] = None

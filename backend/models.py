from pydantic import BaseModel, Field
from typing import Optional


class ProjectRequest(BaseModel):
    city: str
    building_type: str = "residential"

    floors: int = Field(ge=1)

    bedrooms: Optional[int] = Field(default=None, ge=0)
    bathrooms: Optional[int] = Field(default=None, ge=0)
    car_parking: Optional[int] = Field(default=None, ge=0)
    kitchen: Optional[int] = Field(default=None, ge=0)

    servant_room: Optional[str] = None

    special_requirements: Optional[str] = None


class PlotRequest(BaseModel):
    plot_width: float = Field(gt=0)
    plot_length: float = Field(gt=0)
    unit: str = "ft"

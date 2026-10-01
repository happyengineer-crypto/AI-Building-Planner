from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="AI Building Planner",
    description="AI-powered architectural planning backend",
    version="0.1.0",
)


class PlotRequest(BaseModel):
    width: float = Field(gt=0, description="Plot width")
    length: float = Field(gt=0, description="Plot length")
    unit: str = Field(default="ft", description="Measurement unit")


@app.get("/")
def root():
    return {
        "project": "AI Building Planner",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/plot/analyze")
def analyze_plot(plot: PlotRequest):
    area = plot.width * plot.length

    return {
        "width": plot.width,
        "length": plot.length,
        "unit": plot.unit,
        "area": area,
        "message": "Plot analyzed successfully."
    }

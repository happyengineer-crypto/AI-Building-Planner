from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from question_engine import get_next_question


app = FastAPI(
    title="AI Building Planner",
    description="AI-powered architectural planning backend",
    version="0.2.0",
)


class PlotRequest(BaseModel):
    width: float
    length: float
    unit: str = "ft"


class QuestionRequest(BaseModel):
    answers: Dict = {}


@app.get("/")
def root():
    return {
        "project": "AI Building Planner",
        "status": "running",
        "version": "0.2.0",
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
        "message": "Plot analyzed successfully.",
    }


@app.post("/requirements/next-question")
def next_question(request: QuestionRequest):
    question = get_next_question(request.answers)

    return {
        "next_question": question
    }

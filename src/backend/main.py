from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os
from ai_project.crew import AiProjectCrew

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI backend is running"}

@app.post("/generate")
async def generate_post(request: Request):
    data = await request.json()  # raw JSON as a dict

    # Manually validate keys (topic, tone, word_count)
    topic = data.get("topic")
    tone = data.get("tone")
    word_count = data.get("word_count")

    if not topic or not tone or not isinstance(word_count, int):
        return {"error": "Invalid input"}

    inputs = {
        "topic": topic,
        "tone": tone,
        "word_count": word_count
    }

    result = AiProjectCrew().crew().kickoff(inputs=inputs)

    final_post = None
    if isinstance(result, dict):
        if "raw" in result:
            final_post = result["raw"]
        elif "generated_post" in result and "raw" in result["generated_post"]:
            final_post = result["generated_post"]["raw"]
    if not final_post:
        final_post = str(result)

    return {"generated_post": final_post}

@app.get("/post")
def get_post():
    return {"message": "Hello"}

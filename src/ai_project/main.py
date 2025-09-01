# #!/usr/bin/env python
# from ai_project.crew import AiProjectCrew

# def run_crew():
#     inputs = {
#         "topic": "deep Learning",
#         "tone": "casual",
#         "word_count": 300
#     }
#     result = AiProjectCrew().crew().kickoff(inputs=inputs)
#     print(result)

# if __name__ == "__main__":
#     run_crew()

# run_crew.py
from ai_project.crew import AiProjectCrew

def generate_post(topic: str, tone: str, word_count: int) -> str:
    inputs = {
        "topic": topic,
        "tone": tone,
        "word_count": word_count
    }
    result = AiProjectCrew().crew().kickoff(inputs=inputs)
    return result

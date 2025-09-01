from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, llm
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from dotenv import load_dotenv
load_dotenv()



@CrewBase
class AiProjectCrew():
  """Crew for creating social media content"""

  agents: List[BaseAgent]
  tasks: List[Task]

  @llm
  @llm
  def ai_llm(self):
    return os.getenv("MODEL", "gemini/gemini-1.5-flash")

  @agent
  def source_collector(self) -> Agent:
    return Agent(
      config=self.agents_config['source_collector'], # type: ignore[index]
      verbose=True,
      tools=[SerperDevTool()],
      llm=self.ai_llm()
    )

  @agent
  def content_preparer(self) -> Agent:
    return Agent(
      config=self.agents_config['content_preparer'], # type: ignore[index]
      verbose=True,
      llm=self.ai_llm()
    )

  @agent
  def personalizer(self) -> Agent:
    return Agent(
      config=self.agents_config['personalizer'], # type: ignore[index]
      verbose=True,
      llm=self.ai_llm()
    )

  @task
  def source_task(self) -> Task:
    return Task(config=self.tasks_config['source_task'])

  @task
  def preparation_task(self) -> Task:
    return Task(config=self.tasks_config['preparation_task'])

  @task
  def personalization_task(self) -> Task:
    return Task(
      config=self.tasks_config['personalization_task'],
      output_file="output/post.txt"
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=self.agents,
      tasks=self.tasks,
      process=Process.sequential,
      verbose=True
    )

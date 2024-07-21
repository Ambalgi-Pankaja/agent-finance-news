from crewai import Crew, Process
from task import write_task, yt_task
from agents import blog_writer, yt_researcher

# Forming the tech focused crew with some enhanced configuration
crew = Crew(
    agents=[yt_researcher, blog_writer],
    tasks=[yt_task, write_task],
    process=Process.sequential,
)

# starting the task execution process with enhanced feedback

result = crew.kickoff(inputs={'topic': 'Travel'})
print(result)

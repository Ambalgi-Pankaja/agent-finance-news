from crewai import Task
from tools import serper_tool, yt_tool
from agents import blog_writer, yt_researcher

# Research task
yt_task = Task(
  description=(
    "List the YT videos links on the topic {topic}. "
    "Focus on finding the popular videos of each of the topic. "
    "Also get the description of video selected to write about it."
  ),
  expected_output='A comprehensive list of YT video links on each of the topic {topic}.',
  tools=[yt_tool, serper_tool],
  agent=yt_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose a the list of few YT video links on the {topic} searched by the YT search"
    "Also provide a description of the video searched by the YT and write about the videos."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A blog having summary of about 3 paragraphs on the '
                  'the list of few YT videos on {topic} and about the {topic} formatted as markdown.',
  tools=[serper_tool, yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)
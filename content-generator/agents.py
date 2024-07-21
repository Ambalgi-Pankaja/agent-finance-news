from crewai import Agent
from tools import serper_tool, yt_tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()


# call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating a senior researcher agent with memory and verbose mode

yt_researcher = Agent(
    role="Senior Researcher",
    goal='Search list of YouTube videos on the topic {topic} get its description.',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're searching popular YT video links on the YouTube on the given {topic}. "
        "Also you have the ability to explore the description of the channel."
    ),
    tools=[yt_tool, serper_tool],
    llm=llm,
    allow_delegation=True
)

# creating a write agent with custom tools responsible in writing news blog

blog_writer = Agent(
  role='Writer',
  goal='Write a blog of the list of few youtube video links for the given {topic} '
       'searched by the YT search, along with its description. Also write about the {topic}.',
  verbose=True,
  memory=True,
  backstory=(
    "As a good summarizer,"
    "a list of few you tube videos along with its links searched by the YT search agent "
    "and about the {topic}"
    "Give the description of it."
    "You are the best to summarize the list with its description and provide in a neat way."
  ),
  tools=[yt_tool, serper_tool],
  llm=llm,
  allow_delegation=False
)

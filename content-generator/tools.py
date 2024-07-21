import os
from crewai_tools import SerperDevTool
from langchain_community.tools import YouTubeSearchTool
from dotenv import load_dotenv
load_dotenv()


os.environ['SERPAPI_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

serper_tool = SerperDevTool()

yt_tool = YouTubeSearchTool()
yt_tool.run("topic")

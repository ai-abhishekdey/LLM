import os
from crewai import Agent
from Tools import llm, serper_tool


## Agent-1: Flight Search Agent

flight_agent = Agent(
    role="Flight Searcher",
    goal="To find the cheapest flights from {source} to {destination} between {start_date} and {return_date}",
    backstory="An expert in finding the best flight deals and schedules using online search",
    tools=[serper_tool],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)

## Agent-2: Hotel Search Agent

hotel_agent = Agent(
    role="Luxury Hotel Finder",
    goal="To find the top 3 luxury hotels at {destination} between {start_date} and {return_date}",
    backstory="A travel expert who specializes in finding the most luxurious hotels",
    tools=[serper_tool],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)


## Agent-3: Travel guide Agent

travel_guide_agent = Agent(
    role="travel guide",
    goal="To suggest the top attractions and destinations near {destination}",
    backstory="A seasoned travel guide with in-depth knowledge of popular travel destinations",
    tools=[serper_tool],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)


## Agent-4: Weather Advisor Agent

weather_agent = Agent(
    role="Weather Forecaster",
    goal="To check the weather in {destination} between {start_date} and {return_date} and suggest what to carry",
    backstory="An expert in weather prediction and travel packing advice",
    tools=[serper_tool],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)

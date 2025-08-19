from crewai import Task
from Agents import flight_agent, hotel_agent, travel_guide_agent, weather_agent
from Tools import llm
from Tools import llm, serper_tool


# Task 1: Flight Search Task

flight_search_task = Task(
    description="Search for the cheapest flights from {source} to {destination} between {start_date} and {return_date}",
    expected_output="A list of the cheapest flights with prices and links",
    tools=[serper_tool],
    llm=llm,
    agent=flight_agent,
)

# Task 2: Hotel Search Task

hotel_search_task = Task(
    description="Search for the top 3 luxury hotels in {destination} between {start_date} and {return_date}",
    expected_output="A list of top 3 luxury hotels with ratings and booking links",
    tools=[serper_tool],
    llm=llm,
    agent=hotel_agent,
)

# Task 3: Destination Recommendation Task

destination_recommendation_task = Task(
    description="Provide top attractions and recommended destinations near {destination}",
    expected_output="A list of recommended attractions and destinations",
    tools=[serper_tool],
    llm=llm,
    agent=travel_guide_agent,
)


# Task 4: Weather Advisory Task

weather_advisory_task = Task(
    description="Check the weather in {destination} between {start_date} and {return_date} and suggest what to carry",
    expected_output="Weather forecast summary and packing recommendations",
    tools=[serper_tool],
    llm=llm,
    agent=weather_agent,
)

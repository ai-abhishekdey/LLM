from crewai import Crew
from Agents import flight_agent, hotel_agent, travel_guide_agent, weather_agent
from Tasks import flight_search_task, hotel_search_task, destination_recommendation_task, weather_advisory_task


# Initialize the Crew with agents and tasks
crew = Crew(
    agents=[flight_agent, hotel_agent, travel_guide_agent, weather_agent],
    tasks=[flight_search_task, hotel_search_task, destination_recommendation_task, weather_advisory_task],
    verbose=True
)

# Kickoff the Crew with travel inputs
result = crew.kickoff(inputs={
    'source': "Guwahati",
    'destination': "Mumbai",
    'start_date': "2025-08-21",
    'return_date': "2025-08-25"
})

# Print structured travel plan
#print(result)

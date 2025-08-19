from Agents import content_writer_agent
from Tasks import content_writing
from crewai import Crew



crew=Crew(

    agents=[content_writer_agent],
    tasks=[content_writing],
    verbose=True

)

result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})

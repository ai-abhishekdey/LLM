from crewai import Task
from Agents import content_writer_agent


# Content writing task


content_writing=Task(

    description="Analyse the given topic {topic} and write a beautiful paragraph within 100 words ",
    expected_output="A summarized paragraph on the given topic {topic} within 100 words",
    agent=content_writer_agent

)
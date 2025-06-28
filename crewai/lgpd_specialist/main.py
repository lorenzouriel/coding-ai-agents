from crew import SpecialistCrew

def run_specialist_crew(question: str):
    crew_instance = SpecialistCrew()
    result = crew_instance.crew().kickoff(inputs={"question": question})
    return result

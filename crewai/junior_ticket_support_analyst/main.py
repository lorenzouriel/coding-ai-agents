from crew import JuniorSupportCrew

def run_junior_support_crew(question: str):
    crew_instance = JuniorSupportCrew()
    result = crew_instance.crew().kickoff(inputs={"question": question})
    return result

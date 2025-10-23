class PostdocAgent(BaseAgent):
def __init__(self, model="gpt4omini", notes=None, max_steps=100,
openai_api_key=None):
super().__init__(model, notes, max_steps, openai_api_key)
self.phases = ["plan formulation", "results interpretation"]
def context(self, phase):
sr_str = str()
if self.second_round:
sr_str = (
f"The following are results from the previous
experiments\n",
f"Previous Experiment code:
{self.prev_results_code}\n"
f"Previous Results: {self.prev_exp_results}\n"
f"Previous Interpretation of results:
{self.prev_interpretation}\n"
f"Previous Report: {self.prev_report}\n"
f"{self.reviewer_response}\n\n\n"
)
if phase == "plan formulation":
return (
sr_str,
f"Current Literature Review: {self.lit_review_sum}",
)
elif phase == "results interpretation":
return (
sr_str,
f"Current Literature Review: {self.lit_review_sum}\n"
f"Current Plan: {self.plan}\n"
f"Current Dataset code: {self.dataset_code}\n"
f"Current Experiment code: {self.results_code}\n"
f"Current Results: {self.exp_results}"
)
return ""
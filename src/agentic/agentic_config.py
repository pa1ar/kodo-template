from agenticos.connectors import BaseWorkflowConfig, CrewaiWorkflowConfig
from agenticos.node.models import AgenticConfig

workflows : dict[str,BaseWorkflowConfig] = {}

# Example workflow
# Import the Crew class. If you used the flow from CrewAI docs the following import should work
# If you are getting any erros please correct the import path
from templatecrew.crew import TemplatecrewCrew as Crew

# Define workflows here
# key is the workflow name
workflows["template"] = CrewaiWorkflowConfig(
    # Description of the workflow
    description="TEMPLATE_WORKFLOW",
    # Inputs for the workflow
    inputs={"topic": "The topic to make a research about"},
    # The crew class to be used
    crew_cls=Crew,
)

# Create the config object. Change the name to the name of your node
config = AgenticConfig(name="TEMPLATE_NODE", workflows=workflows)
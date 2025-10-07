from django.shortcuts import render, get_object_or_404
import json
from .services import generate_dialogue
from .models import Scenario

# Function to display a list of all available scenarios
def scenario_list_view(request):
    scenarios = Scenario.objects.all()
    context = {"scenarios": scenarios}
    return render(request, "core/scenario_list.html", context)

# Function to display a specific scenario and generate dialogue
def scenario_detail_view(request, slug):
    # Find the chosen scenario based on the slug
    scenario_object = get_object_or_404(Scenario, slug=slug)

    
    # Call to service function with scenario's description
    dialogue_json_string = generate_dialogue(
        language="French", #change from hardcoded later
        level="Beginner", #change from hardcoded later
        scenario_description=scenario_object.title
    )

    context = {"title": scenario_object["title"]}

    if dialogue_json_string:
        try:
            dialogue_data = json.loads(dialogue_json_string)
            context['scenario'] = dialogue_data
        except json.JSONDecodeError:
            context['error'] = "The response was not valid JSON."
    else:
        context['error'] = "Failed to get a response from the API."

    return render(request, 'core/scenario.html', context)


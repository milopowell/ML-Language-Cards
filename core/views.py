from django.shortcuts import render, get_object_or_404
import json
from .services import generate_dialogue


SCENARIOS = [
    {
        "id": 1,
        "title": "Going to the Barbershop",
        "slug": "barbershop",
        "description": "Practice a dialogue between a customer and a barber.",
    },
    {
        "id": 2,
        "title": "At the Restaurant",
        "slug": "restaurant",
        "description": "Practice ordering food and interacting with restaurant staff.",
    },
    {
        "id": 3,
        "title": "Booking a Hotel Room",
        "slug": "hotel",
        "description": "Practice checking in and making requests at a hotel.",
    },
    {
        "id": 4,
        "title": "Asking for Directions",
        "slug": "directions",
        "description": "Practice asking for and giving directions in a new city.",
    },
    {
        "id": 5,
        "title": "Shopping for Clothes",
        "slug": "shopping",
        "description": "Practice interacting with sales staff while shopping for clothes.",
    },
    {
        "id": 6,
        "title": "Visiting the Doctor",
        "slug": "doctor",
        "description": "Practice describing symptoms and understanding medical advice.",
    },
    {
        "id": 7,
        "title": "At the Airport",
        "slug": "airport",
        "description": "Practice checking in, going through security, and boarding a flight.",
    },
    {
        "id": 8,
        "title": "Making Small Talk",
        "slug": "small-talk",
        "description": "Practice casual conversations on various topics.",
    },
]

# Function to display a list of all available scenarios
def scenario_list_view(request):
    context = {"scenarios": SCENARIOS}
    return render(request, "core/scenario_list.html", context)

# Function to display a specific scenario and generate dialogue
def scenario_detail_view(request, slug):
    # Find the chosen scenario based on the slug
    scenario_object = next((item for item in SCENARIOS if item["slug"] == slug), None)

    # 404 error if scenario doesn't exist
    if not scenario_object:
        return render(request, 'core/scenario_not_found.html', status=404)
    
    # Call to service function with scenario's description
    dialogue_json_string = generate_dialogue(
        language="French", #change from hardcoded later
        level="Beginner", #change from hardcoded later
        scenario_description=scenario_object["title"]
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


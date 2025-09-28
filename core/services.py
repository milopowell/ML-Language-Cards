import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# Function to generate dialogue given a specific language, level, and scenario
# Returns the raw JSON string from the API
def generate_dialogue(language, level, scenario_description):
    """
    Generates a language-learning dialogue using the Gemini API.
    """
    
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # This prompt is structured for Gemini
    prompt = f"""
    You are a helpful language tutor AI. Your task is to create a simple, educational dialogue
    for a language learner. The dialogue should be clear, concise, and focused on the
    provided scenario.

    Generate a simple dialogue for a '{level}' level learner in '{language}' for the following scenario: '{scenario_description}'.
    Respond with only a valid JSON object in the specified format.
    {{
        "scenario": "{scenario_description}",
        "dialogue": [
            {{ "speaker": "Person A", "phrase": "...", "translation": "..." }},
            {{ "speaker": "Person B", "phrase": "...", "translation": "..." }}
        ]
    }}
    """
    
    try:
        # Gemini Pro Latest Model
        model = genai.GenerativeModel('gemini-pro-latest')
        generation_config = genai.types.GenerationConfig(response_mime_type="application/json")
        response = model.generate_content(prompt, generation_config=generation_config)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None 

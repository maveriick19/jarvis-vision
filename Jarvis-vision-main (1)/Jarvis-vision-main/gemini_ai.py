import google.generativeai as genai
import re

 
# Replace with your real API key from Step 1
GENAI_API_KEY = "use_your_api_key"   # Put your API key here in github repo it is removed for security reasons

genai.configure(api_key=GENAI_API_KEY)

# Load Gemini Pro model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def clean_ai_response(text):
            # Remove markdown formatting like *text* or **text**
            cleaned = re.sub(r"\*+", "", text)
            return cleaned

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        result_text = response.text  #  this is the string we need
        cleaned = clean_ai_response(result_text)
        return cleaned
    except Exception as e:
        return f"Error: {e}"

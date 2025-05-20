import google.generativeai as genai
import os

# Configure with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # For Google AI Studio APIs

# Or if using Vertex AI, the initialization would be different
# from google.cloud import aiplatform
# aiplatform.init(project='YOUR_PROJECT', location='YOUR_LOCATION')

print("Available models:")
# The exact way to list models might differ slightly based on whether you're using
# the Google AI Generative Language API or Vertex AI API.

# For google-generativeai library (often used with Google AI Studio):
try:
    for m in genai.list_models():
        # Check if the model supports the 'generateContent' method (or its equivalent)
        # The attribute name for supported methods might vary, e.g., m.supported_generation_methods
        can_generate_content = False
        if hasattr(m, 'supported_generation_methods'):
            if 'generateContent' in m.supported_generation_methods or 'generate_content' in m.supported_generation_methods:
                 can_generate_content = True
        elif hasattr(m, 'supports_generate_content'): # Fictional attribute for illustration
             can_generate_content = m.supports_generate_content

        print(f"Model name: {m.name}")
        print(f"  Description: {m.description}")
        print(f"  Supports generateContent (or equivalent): {can_generate_content}")
        if hasattr(m, 'version'):
            print(f"  Version: {m.version}")
        if hasattr(m, 'supported_generation_methods'):
             print(f"  Supported generation methods: {m.supported_generation_methods}")
        print("-" * 20)

except Exception as e:
    print(f"An error occurred while listing models: {e}")
    print("Please ensure your API key is correctly configured and has the necessary permissions.")
    print("Also, check the library documentation for the exact method to list models and their capabilities for the API version you intend to use.")

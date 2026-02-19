import google.generativeai as genai

# Use your key
genai.configure(api_key="AIzaSyBA_xv5inXm3rhIQqOG1kxHVimvJVf9Cu4")

print("Available models that support text generation:")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(f"- {m.name}")

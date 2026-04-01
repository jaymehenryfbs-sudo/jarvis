import google.generativeai as genai
genai.configure(api_key="AIzaSyBYO6mb1DVaPjWcSItuohKcVXilp6EKbRM")

print("Modèles disponibles pour votre clé :")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")

import os
from groq import Groq

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

selected_model = "llama-3.3-70b-versatile"  # Replace with the appropriate Groq model name

def basic_generation(user_prompt):
    # Use the Groq API to generate text
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        model=selected_model,
    )
    # Extract the generated text from the response
    generated_text = response.choices[0].message.content  # Adjust based on Groq's response structure
    return generated_text
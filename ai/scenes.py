from ai.client import client

def generate_scenes(product, goal):

    prompt = f"""
Suggest exactly THREE visual scenes.

Product:
{product}

Campaign Goal:
{goal}

Requirements:

- Number them 1,2,3.
- Each description should be 2-3 sentences.
- Focus on practical visuals.
- No dialogue.
- No camera jargon.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
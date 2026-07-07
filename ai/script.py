from ai.client import client

def generate_script(product, audience, goal, duration=30):

    prompt = f"""
Write a promotional video script.

Product:
{product}

Audience:
{audience}

Campaign Goal:
{goal}

Duration:
{duration} seconds

Requirements:

- Approximately one sentence every 3 seconds.
- Maximum 3 scenes.
- Minimum 2 scenes.

Format exactly:

[SCENE 1]
Scene Description

VOICEOVER:
...

[SCENE 2]
Scene Description

VOICEOVER:
...

Do not include anything else.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
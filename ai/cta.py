from ai.client import client

def generate_cta(product, audience, goal):

    prompt = f"""
Write a short Call-To-Action.

Product:
{product}

Audience:
{audience}

Goal:
{goal}

Rules:

- Maximum 25 words.
- Strong action verb.
- Mention where users can purchase or learn more if appropriate.
- Return only the CTA.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()
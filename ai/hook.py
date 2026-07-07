from ai.client import client

def generate_hook(product, audience):

    prompt = f"""
You are a professional video marketing copywriter.

Generate ONE attention-grabbing hook.

Rules:
- Maximum 20 words.
- Begin with either:
  * a question
  * a surprising fact
  * a bold statement
- Mention the product naturally.
- Target audience: {audience}
- Product: {product}

Return only the hook.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()
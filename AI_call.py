import os


from google import genai
from openai import OpenAI




def AI_fetch(ai_prompt):
    try:
        client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=ai_prompt
        )
        return response.text.replace('*','')

      
        
    except Exception:
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1", 
        api_key=os.getenv('X_backupai'),
        )

        # First API call with reasoning
        response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct:free", 
        messages=[
                {
                    "role": "user",
                    "content": ai_prompt
                }
                ],
        extra_body={"reasoning": {"enabled": True}}
        )

        # Extract the assistant message with reasoning_details
        return response.choices[0].message.content.replace('*','')

       
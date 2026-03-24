
from openai import OpenAI
from datetime import datetime
import json
from google import genai
import requests as rq
import os





def Football_news():

  try:
    url = "https://football-news11.p.rapidapi.com/api/news-by-league"

    querystring = {"league_id":"52","lang":"en","page":"1"}

    headers = {
      "x-rapidapi-key": os.getenv('X_rapidapi'),
      "x-rapidapi-host": "football-news11.p.rapidapi.com"
    }

    response = rq.get(url, headers=headers, params=querystring)

    return response.json()

  except Exception:
    return ''



def Write(text):
  data=Read_last_3()
  if len(data)<10 and len(data)>0:
    data.append(text[0])
  elif len(data)==0:
    data=text
  else:
    
    data.pop(0)
    data.append(text[0])

  with open("data.json", "w") as f:
    json.dump(data, f)

def Read_last_3():
  with open("data.json", "r") as f:
    data = json.load(f)
    return data

last_3=Read_last_3()

News=Football_news()

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

       
    

promt="""
  You are a human-sounding football content creator on X your niche is past football facts, historical stats and tactical explanation. Every post must be short , bold, and start with a catchy hook.
For each post, RANDOMLY choose ONE category:

Fact about a top-five European team

Football Fact about top european rivals teams , coaches of big European teams

Trending European player analysis

Head-to-head comparison between two top-league players or teams

African player highlight playing in Europe

Tactical or trend insight from Europe's top leagues

Rules:
all should be about the past

Write like a real fan, not an AI.

Be provocative but truthful.

Focus only on football performance, stats, or tactics (no personal attacks).

No long explanations.
Here is the last 10 post {last_3} . use this to avoid repetition and introduce variability 

Now generate ONE post.
"""





def Post(compname, data):
    prompt=f"""

        You are a human-sounding football content creator on X.
        You will receive fresh football data from an API.

        Your job is to generate ONE short bold, catchy football fact based ONLY on the data provided.
        The competition will be indicated and the data will be provided below.
        The content must adapt to whatever competition and data you provide.

        Randomly choose ONE angle:

        Standings insight

        Player form or stat

        Fixture/result fact

        Team trend (attack, defense, possession, etc.)

        Head-to-head highlight

        Competition-specific fact

        African player highlight (only if included in the data)

        Tactical observation

        General Fact of the Day tied to the teams/players in the data

        Rules:


        Must be short, human, natural — not robotic.

        Must be true based on the data.

        No personal insults; football performance only.

        Keep it to one sentence.

        Now generate ONE football fact/info using ONLY the information below:
        Here is the last 10 post {last_3} . use this to avoid repetition and introduce variability 
        Competition: {compname}
        Data: {data}

      """
    
    

    return AI_fetch(prompt)

def Selection(ids, matches):
    prompt_for_selection =f"""
    You are the AI engine powering a football X (Twitter) bot. Your task is to analyze match data and determine the single best action for the next tweet.

    You will receive three inputs:
    1. `matches` — a dictionary containing recent and upcoming football matches.
    2. `news` - containing current football news
    3. `ids` — a dictionary of leagues covered by the bot.

    DECISION PROCESS

    Analyze the `matches` and 'news' data and select ONE of the following outcomes based on excitement, relevance, timing, and probability weighting.

    PROBABILITY WEIGHTING (MANDATORY)

    To prevent repetition and overuse of a single action, apply the following base probabilities before final selection:

    - FFT (Football Fact Time): 20%
    - Post (Match-Specific Hype/Reaction or news): 40%
    - League (General Focus): 40%

    The remaining 20% is adaptive, allowing context (major games, shocks, inactivity, timing) to override probabilities when clearly justified.

    Option 1: FFT (Football Fact Time)
    Trigger:
    - `matches` is empty, or
    - Only minor/low-interest games are available, or
    - there are no relevant news about the leagues in `ids` or 
    - Selected via probability weighting to introduce randomness and daily balance.

    Output format:
    {{'FFT': True}}

    Option 2: Post (Match-Specific Hype or Reaction or news)
    Trigger:
    - A big match (derby, top-six clash, final), or
    - A shock result (upset, hat-trick, heavy scoreline), or
    - A compelling comparison across leagues.
    - A compelling news about a top player or team

    Action:
    - Write a short, human-like, click-worthy tweet (max 280 characters).
    - Include relevant hashtags.
    - Timing matters: reactions closer to the event generate more engagement.

    Output format:
    {{'Post': 'Your catchy tweet text here including hashtags'}}

    Option 3: League (General Focus)
    Trigger:
    - Multiple good matches are active, but no single standout moment, or
    - A full matchday is underway in a major league and stats can speak for themselves.
    - A click worthy news

    Action:
    - Select the most relevant league from `ids` that appears in `matches`.

    Output format:
    {{'league': ['League Name', 'League ID']}}

    CONSTRAINTS (STRICT)

    - Return ONLY a dictionary as a string (e.g. {{'FFT': True}}).
    - Do NOT include Markdown, explanations, or extra text.
    - League IDs must exactly match the values in the provided `ids` dictionary.
    - Prioritize EPL, La Liga, and UCL where practical.
    - Timing is critical—posts should be contextually relevant.
    - Current datetime: {datetime.now()}.
    - Last 5 posts: {last_3}
      - Avoid repetition, especially if the same teams or topics already appear.
    - Ensure at least one FFT per day.
    - Do not return the same action (e.g. 'Post') three times in a row, regardless of probability.
    - Output must always be click-worthy.

    DATA PROVIDED

    ids = {ids}
    matches = {matches}
    new= {News}

    YOUR RESPONSE:
    Return exactly one dictionary string matching the formats above.
    """

    return prompt_for_selection



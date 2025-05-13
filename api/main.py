from fastapi import FastAPI, Query, HTTPException
from modules import sentiment, suggestion

app = FastAPI(debug=True)

@app.get("/mood")
def read_moods():
    # TODO: fetch real mood logs from DB
    return {"mood_logs": []}

@app.get("/vibes")
def read_vibes():
    # TODO: fetch real presets from DB
    return {"vibe_presets": ["focused", "calm"]}

@app.get("/sentiment")
def get_sentiment(text: str = Query(..., description="Text to analyze sentiment")):
    try:
        result = sentiment.analyze_sentiment(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sentiment analysis failed: {e}")
    return {"sentiment": result}

@app.get("/suggestion")
def get_suggestion(prompt: str = Query(..., description="Prompt for introspection")):
    try:
        result = suggestion.why_am_i_feeling_this(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Suggestion generation failed: {e}")
    return {"suggestion": result}
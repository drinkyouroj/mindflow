# MindFlow

**MindFlow** is a self-management software suite designed to boost productivity while nurturing emotional wellbeing. Built with a neuro-affirming and low-friction approach, MindFlow offers real-time mood tracking, smart task management, and extensible plugins — all while keeping your data local-first and private.

## Vision

1. **Neuro-affirming**: Leverage strengths like pattern recognition and detail focus
2. **Low-friction**: Natural-language vibe commands, minimal clicks, smart defaults
3. **Emotionally intelligent**: Mood check-ins, burnout prevention nudges
4. **Local-first & private**: Data lives on your machine, optional sync
5. **Open & extensible**: Plugin hooks for community modules

## Core Modules

- **Contextual Awareness**: CreatorGuard comment moderation, email/DM sentiment filter
- **Task & Executive Function**: Smart to-do list, vibe triggers, Pomodoro, auto-pause
- **Emotional Logging**: Quick mood journal, GPT-powered reflection prompts
- **Sensory Environment**: White noise/music suggestions, screen breaks
- **Self-Insight & Analytics**: Weekly dashboards, burnout risk alerts

## Tech Stack

- **Backend**: Python, FastAPI
- **Database**: SQLite (encrypted), schema in `db/schema.sql`
- **AI**: OpenAI GPT-4-turbo
- **Frontend**: React + Tailwind in Electron/Tauri
- **CLI**: Click-based vibe tool

## Installation

```bash
git clone <repo-url>
cd mindflow

# Create & activate virtual env
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python db/init_db.py

# Start API server
uvicorn api.main:app --reload
```

## Usage

### CLI
```bash
# Activate "focused" preset
mindflow-vibe focused

# Activate "calm" preset
mindflow-vibe calm
```

### API
```http
GET http://localhost:8000/mood
GET http://localhost:8000/vibes
```

### Frontend Shell
```bash
cd app
npm install
npm start
``` 

## Contributing

Contributions welcome! Please open issues or PRs.

## Roadmap

- Plugin marketplace
- Emotional-vs-productivity analytics
- Sync across devices via Git

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

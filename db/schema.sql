-- Enable foreign‑key support (SQLite pragma)
PRAGMA foreign_keys = ON;

-- 1) Mood logging
CREATE TABLE IF NOT EXISTS mood_logs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    mood        TEXT NOT NULL,                         -- e.g. "anxious", "calm", "focused"
    intensity   INTEGER CHECK(intensity BETWEEN 1 AND 10),
    notes       TEXT                                  -- free‑form journal entry
);

-- 2) Vibe presets
CREATE TABLE IF NOT EXISTS vibe_presets (
    name        TEXT PRIMARY KEY,                      -- e.g. "focused", "calm"
    config      JSON NOT NULL,                         -- JSON blob mapping module states
    created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 3) CreatorGuard comment moderation
CREATE TABLE IF NOT EXISTS comment_moderation (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    comment_id    TEXT,                                -- original platform ID
    text          TEXT NOT NULL,                       -- comment body
    sentiment     TEXT,                                -- e.g. "supportive", "toxic", etc.
    tag           TEXT CHECK(tag IN ('hide','respond','flag','ignore','other')),
    action_taken  TEXT,                                -- e.g. "hidden", "queued reply"
    logged_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 4) Task / Executive‑function entries
CREATE TABLE IF NOT EXISTS tasks (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    description  TEXT NOT NULL,
    created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    due_at       DATETIME,
    completed    INTEGER NOT NULL DEFAULT 0            -- 0 = no, 1 = yes
);

-- 5) Global config / settings
CREATE TABLE IF NOT EXISTS config (
    key   TEXT PRIMARY KEY,
    value TEXT
);

-- Indexes for faster lookups
CREATE INDEX IF NOT EXISTS idx_mood_logs_timestamp    ON mood_logs(timestamp);
CREATE INDEX IF NOT EXISTS idx_presets_created_at     ON vibe_presets(created_at);
CREATE INDEX IF NOT EXISTS idx_comments_logged_at     ON comment_moderation(logged_at);
CREATE INDEX IF NOT EXISTS idx_tasks_due_at           ON tasks(due_at);
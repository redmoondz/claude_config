# claude_config

Personal Claude Code configuration — settings, statusline, and plugins.

## What's here

| File | Purpose |
|------|---------|
| `settings.json` | Global Claude Code settings (statusline, env flags) |
| `statusline.py` | Status bar script — shows session start, context usage, weekly rate limit |
| `plugins/` | Cloned [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) marketplace |

## Status bar

The bottom status bar shows four segments in one line:

```
30.05.2026 14:30  |  ▓▓▓░░░░░░░░░░░░░ 23% (46,000/200,000)  |  ▓▓░░░░░░░░░░░░░░ 12% 5h  |  ▓▓▓▓▓▓░░░░░░░░░░ 41% 7d
```

- **Date** — session start time
- **Context bar** — tokens used in the current context window vs the model limit (200k by default)
- **5-hour bar** — Claude.ai rate limit consumption for the rolling 5-hour window (Pro/Max only)
- **Weekly bar** — Claude.ai rate limit consumption for the 7-day rolling window (Pro/Max only)

Color coding: green → yellow at 70% → red at 90%.

## Setup

### This machine

```bash
# Copy script to Claude's config dir
cp statusline.py ~/.claude/statusline.py
chmod +x ~/.claude/statusline.py

# Copy settings (merge manually if you have existing settings)
cp settings.json ~/.claude/settings.json
```

### Another machine

```bash
git clone https://github.com/redmoondz/claude_config
cd claude_config
cp statusline.py ~/.claude/statusline.py
chmod +x ~/.claude/statusline.py
# Add statusLine block to ~/.claude/settings.json — see settings.json for the snippet
```

### settings.json snippet

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/statusline.py"
  }
}
```

**Requires:** Python 3 (pre-installed on macOS/most Linux distros). No extra packages needed.

## Sync workflow

```bash
# Pull latest on any machine
git pull

# Apply updates
cp statusline.py ~/.claude/statusline.py
```

## What's gitignored

Sensitive and ephemeral files are excluded:

- `.credentials.json` — OAuth tokens (never commit)
- `history.jsonl`, `projects/`, `tasks/`, `plans/` — session data
- `backups/`, `file-history/`, `paste-cache/`, `cache/` — runtime cache

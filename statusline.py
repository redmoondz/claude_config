#!/usr/bin/env python3
import json, sys, time, datetime

data = json.load(sys.stdin)

GREEN  = '\033[32m'
YELLOW = '\033[33m'
RED    = '\033[31m'
DIM    = '\033[2m'
RESET  = '\033[0m'

duration_ms = (data.get('cost') or {}).get('total_duration_ms', 0) or 0
start_ts    = time.time() - duration_ms / 1000
start_str   = datetime.datetime.fromtimestamp(start_ts).strftime('%d.%m.%Y %H:%M')

ctx       = data.get('context_window') or {}
used_pct  = int(ctx.get('used_percentage') or 0)
used_tok  = ctx.get('total_input_tokens', 0) or 0
ctx_size  = ctx.get('context_window_size', 200000) or 200000

rate      = data.get('rate_limits') or {}
seven     = rate.get('seven_day') or {}
week_pct  = seven.get('used_percentage')

BAR_W = 16

def bar(pct, width=BAR_W):
    filled = int(pct * width / 100)
    return '▓' * filled + '░' * (width - filled)

def col(pct):
    if pct >= 90: return RED
    if pct >= 70: return YELLOW
    return GREEN

ctx_bar  = f"{col(used_pct)}{bar(used_pct)}{RESET} {used_pct}% ({used_tok:,}/{ctx_size:,})"

if week_pct is not None:
    w = int(week_pct)
    week_bar = f"{col(w)}{bar(w)}{RESET} {w}%"
else:
    week_bar = f"{DIM}{'░' * BAR_W}{RESET} --%"

print(f"{start_str}  |  {ctx_bar}  |  {week_bar}")

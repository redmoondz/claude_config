#!/usr/bin/env bash
# Claude Code status line: cwd [progress bar] pct%

input=$(cat)
cwd=$(echo "$input" | jq -r '.cwd // .workspace.current_dir // ""')
used=$(echo "$input" | jq -r '.context_window.used_percentage // empty')

BAR_WIDTH=20

# ANSI colors
GREEN="\033[32m"
DARK="\033[90m"
RESET="\033[0m"

if [ -n "$used" ]; then
  filled=$(awk "BEGIN {printf \"%.0f\", $used * $BAR_WIDTH / 100}")
  empty=$((BAR_WIDTH - filled))
  bar=""
  for i in $(seq 1 "$filled"); do bar="${bar}${GREEN}█${RESET}"; done
  for i in $(seq 1 "$empty");  do bar="${bar}${DARK}░${RESET}"; done
  pct=$(printf "%.0f" "$used")
  printf "%s [%b] %s%%" "$cwd" "$bar" "$pct"
else
  bar=""
  for i in $(seq 1 "$BAR_WIDTH"); do bar="${bar}${DARK}░${RESET}"; done
  printf "%s [%b]" "$cwd" "$bar"
fi

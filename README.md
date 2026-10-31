# IPLOGGGER


**by Swivel**

## Quick Start

```bash
git clone https://github.com/sswivell/ip-logger.git
cd ip-logger
pip install -e .
iplog
```

Or run directly:
```bash
python iplog.py
```

## Usage

```bash
# With Discord webhook and target URL
iplog "https://discord.com/api/webhooks/..." "https://example.com"

# Keyboard shortcuts
Tab/]    Next tab          W/S     Navigate
[        Prev tab          A/D     Adjust settings
1-9/0    Jump to tab       Enter   Edit/activate
R        Reset sim         C       Clear hits
Q        Quit
```

## Tabs

1. **SETUP** - Webhook + target URL
2. **LIVE** - Real-time hits + traffic chart
3. **STATS** - Counters, top countries, ISPs
4. **FP** - Browser fingerprints
5. **REPLAY** - Replay a saved session
6. **SESSIONS** - Saved sessions
7. **PAYLOAD** - Request payload inspector
8. **NETWORK** - Network diagnostics
9. **ALERTS** - Alert history
10. **SETTINGS** - Theme, brightness, refresh rate
11. **ABOUT** - Help & key bindings

"""UI package: screens, widgets, theme, splash."""

from .theme import (
    THEMES, WHITE, GREY, TRK, ALERT, CY, VI, PK, GN, AM,
    SHADES, BRAND, B, R, E,
    fg, bg, mix, ramp, gradient, vlen, pad, lr, set_theme, set_brightness,
)
from .widgets import (
    bar, slider, sparkline, marker, label, highlight, panel, rule, tabs, stat_row, kv,
)
from .splash import splash

__all__ = [
    "THEMES", "WHITE", "GREY", "TRK", "ALERT", "CY", "VI", "PK", "GN", "AM",
    "SHADES", "BRAND", "B", "R", "E",
    "fg", "bg", "mix", "ramp", "gradient", "vlen", "pad", "lr", "set_theme", "set_brightness",
    "bar", "slider", "sparkline", "marker", "label", "highlight", "panel", "rule", "tabs", "stat_row", "kv",
    "splash",
    "App", "Form", "Context", "render", "handle", "loop", "run_app",
]


def __getattr__(name):
    """Import app-level names lazily so core modules can use the theme
    without pulling in the whole UI (which would create an import cycle)."""
    if name in __all__:
        from . import app
        return getattr(app, "main" if name == "run_app" else name)
    raise AttributeError("module %r has no attribute %r" % (__name__, name))

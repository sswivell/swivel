#!/usr/bin/env python3
"""Launcher for iplog: python iplog.py [webhook] [target]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from iplog.ui.app import main

if __name__ == "__main__":
    sys.exit(main())
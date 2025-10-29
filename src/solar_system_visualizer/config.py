#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Solar System Visualizer (Pygame)
File: config.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-29
Updated: 2025-10-29
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Global configuration values for window, simulation, and style.

===========================================================================
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from .colors import BLACK, WHITE, BLUE, CYAN, YELLOW, ORANGE, RED, GREEN, PURPLE


WINDOW_SIZE: Tuple[int, int] = (1280, 800)
WINDOW_TITLE: str = "Solar System Visualizer — Pygame"
MAX_FPS: int = 120
BACKGROUND_COLOR = BLACK

# Camera defaults
ZOOM_INIT: float = 160.0  # pixels per AU at start
ZOOM_MIN: float = 10.0
ZOOM_MAX: float = 600.0

# Time scaling
INITIAL_TIME_SCALE: float = 20.0  # 1 sec = 20 days
MIN_TIME_SCALE: float = 0.1
MAX_TIME_SCALE: float = 2000.0

# Rendering options
DRAW_TRAILS_DEFAULT: bool = True
DRAW_LABELS_DEFAULT: bool = True

# Planet style defaults (some canonical, some stylistic)
@dataclass(frozen=True)
class PlanetStyle:
    color: Tuple[int, int, int]
    radius_px: int


PLANET_STYLES = {
    "Sun": PlanetStyle(color=YELLOW, radius_px=16),
    "Mercury": PlanetStyle(color=GRAY := (150, 150, 150), radius_px=4),
    "Venus": PlanetStyle(color=ORANGE, radius_px=6),
    "Earth": PlanetStyle(color=BLUE, radius_px=6),
    "Mars": PlanetStyle(color=RED, radius_px=5),
    "Jupiter": PlanetStyle(color=ORANGE, radius_px=10),
    "Saturn": PlanetStyle(color=YELLOW, radius_px=9),
    "Uranus": PlanetStyle(color=CYAN, radius_px=8),
    "Neptune": PlanetStyle(color=PURPLE, radius_px=8),
}

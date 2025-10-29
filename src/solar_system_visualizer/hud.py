#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Solar System Visualizer (Pygame)
File: hud.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-29
Updated: 2025-10-29
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Heads-up display and help overlay.

===========================================================================
"""
from __future__ import annotations

import pygame as pg

from .colors import WHITE, GRAY


def draw_hud(screen: pg.Surface, fps: float, time_scale: float, paused: bool,
             show_labels: bool, show_trails: bool) -> None:
    font = pg.font.SysFont(None, 18)
    lines = [
        f"FPS: {fps:5.1f}",
        f"Time Scale: {time_scale:.2f} days/sec",
        "Paused: YES" if paused else "Paused: NO",
        f"Labels: {'ON' if show_labels else 'OFF'} | Trails: {'ON' if show_trails else 'OFF'}",
        "Controls: Wheel=Zoom  RightDrag=Pan  +/-=Speed  Space=Pause  T=Trails  L=Labels  R=Reset  Esc=Quit",
    ]
    y = 8
    for text in lines:
        surf = font.render(text, True, WHITE)
        # background shadow
        shadow = font.render(text, True, GRAY)
        screen.blit(shadow, (10 + 1, y + 1))
        screen.blit(surf, (10, y))
        y += 18

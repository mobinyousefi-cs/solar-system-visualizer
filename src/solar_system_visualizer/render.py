#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Solar System Visualizer (Pygame)
File: render.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-29
Updated: 2025-10-29
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Rendering helpers for bodies, trails, and labels.

===========================================================================
"""
from __future__ import annotations

import pygame as pg

from typing import Iterable, Tuple

from .entities import Body, Camera


def draw_body(screen: pg.Surface, cam: Camera, body: Body, sim_days: float, center: Tuple[int, int],
              with_label: bool) -> tuple[int, int]:
    x_au, y_au = body.position_au(sim_days)
    sx, sy = cam.world_to_screen(x_au, y_au, center)

    # trail
    body.trail.append((sx, sy))
    if len(body.trail) > 2:
        pg.draw.lines(screen, body.color, False, list(body.trail), 1)

    # body
    pg.draw.circle(screen, body.color, (sx, sy), body.radius_px)

    if with_label:
        font = pg.font.SysFont(None, 16)
        label = font.render(body.name, True, (230, 230, 230))
        rect = label.get_rect(midtop=(sx, sy + body.radius_px + 4))
        screen.blit(label, rect)

    return sx, sy


def draw_sun(screen: pg.Surface, center: Tuple[int, int], color=(250, 200, 70)) -> None:
    pg.draw.circle(screen, color, center, 18)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Solar System Visualizer (Pygame)
File: entities.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-29
Updated: 2025-10-29
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Game entities: celestial bodies and camera state.

===========================================================================
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Deque, Tuple
from collections import deque

from .physics import Orbit, ORBIT_DB, orbital_position_au


@dataclass
class Camera:
    zoom: float  # pixels per AU
    offset: Tuple[float, float] = (0.0, 0.0)  # screen translation (px)

    def world_to_screen(self, x_au: float, y_au: float, center: Tuple[int, int]) -> Tuple[int, int]:
        cx, cy = center
        sx = int(cx + x_au * self.zoom + self.offset[0])
        sy = int(cy - y_au * self.zoom + self.offset[1])
        return sx, sy


@dataclass
class Body:
    name: str
    color: Tuple[int, int, int]
    radius_px: int
    orbit: Orbit | None = None  # Sun has None
    trail: Deque[Tuple[int, int]] = field(default_factory=lambda: deque(maxlen=600))

    def position_au(self, sim_days: float) -> Tuple[float, float]:
        if self.orbit is None:
            return (0.0, 0.0)
        return orbital_position_au(sim_days, self.orbit)


# Factory for the solar system bodies

def create_bodies(style_map, include_giants: bool = True) -> list[Body]:
    bodies: list[Body] = []
    # Sun
    s = style_map["Sun"]
    bodies.append(Body(name="Sun", color=s.color, radius_px=s.radius_px, orbit=None))

    order = ["Mercury", "Venus", "Earth", "Mars"]
    if include_giants:
        order += ["Jupiter", "Saturn", "Uranus", "Neptune"]

    for name in order:
        style = style_map[name]
        bodies.append(
            Body(
                name=name,
                color=style.color,
                radius_px=style.radius_px,
                orbit=ORBIT_DB[name],
            )
        )
    return bodies

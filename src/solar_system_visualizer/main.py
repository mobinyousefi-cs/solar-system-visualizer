#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Solar System Visualizer (Pygame)
File: main.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-29
Updated: 2025-10-29
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Pygame entry point: initializes window, sets up bodies, handles input, and
runs the main simulation loop.

Usage:
python -m solar_system_visualizer

===========================================================================
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Tuple

import pygame as pg

from .config import (
    WINDOW_SIZE,
    WINDOW_TITLE,
    MAX_FPS,
    BACKGROUND_COLOR,
    ZOOM_INIT,
    ZOOM_MIN,
    ZOOM_MAX,
    INITIAL_TIME_SCALE,
    MIN_TIME_SCALE,
    MAX_TIME_SCALE,
    PLANET_STYLES,
    DRAW_TRAILS_DEFAULT,
    DRAW_LABELS_DEFAULT,
)
from .entities import Camera, create_bodies
from .hud import draw_hud
from .physics import clamp
from .render import draw_body, draw_sun


@dataclass
class SimState:
    time_scale: float = INITIAL_TIME_SCALE  # days per real second
    sim_days: float = 0.0
    paused: bool = False
    show_trails: bool = DRAW_TRAILS_DEFAULT
    show_labels: bool = DRAW_LABELS_DEFAULT


class App:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(WINDOW_SIZE)
        pg.display.set_caption(WINDOW_TITLE)
        self.clock = pg.time.Clock()

        self.state = SimState()
        self.cam = Camera(zoom=ZOOM_INIT)
        self.dragging = False
        self.drag_origin = (0, 0)
        self.offset_origin = (0.0, 0.0)

        self.bodies = create_bodies(PLANET_STYLES, include_giants=True)

    def handle_events(self) -> bool:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            if event.type == pg.KEYDOWN:
                if event.key in (pg.K_ESCAPE,):
                    return False
                if event.key == pg.K_SPACE:
                    self.state.paused = not self.state.paused
                if event.key in (pg.K_PLUS, pg.K_EQUALS):
                    self.state.time_scale = clamp(self.state.time_scale * 1.2, MIN_TIME_SCALE, MAX_TIME_SCALE)
                if event.key in (pg.K_MINUS, pg.K_UNDERSCORE):
                    self.state.time_scale = clamp(self.state.time_scale / 1.2, MIN_TIME_SCALE, MAX_TIME_SCALE)
                if event.key == pg.K_t:
                    self.state.show_trails = not self.state.show_trails
                    # clear trails when turning off
                    if not self.state.show_trails:
                        for b in self.bodies:
                            b.trail.clear()
                if event.key == pg.K_l:
                    self.state.show_labels = not self.state.show_labels
                if event.key == pg.K_r:
                    self.cam.zoom = ZOOM_INIT
                    self.cam.offset = (0.0, 0.0)

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                self.dragging = True
                self.drag_origin = event.pos
                self.offset_origin = self.cam.offset

            if event.type == pg.MOUSEBUTTONUP and event.button == 3:
                self.dragging = False

            if event.type == pg.MOUSEMOTION and self.dragging:
                dx = event.pos[0] - self.drag_origin[0]
                dy = event.pos[1] - self.drag_origin[1]
                self.cam.offset = (self.offset_origin[0] + dx, self.offset_origin[1] + dy)

            if event.type == pg.MOUSEWHEEL:
                # zoom towards mouse position
                old_zoom = self.cam.zoom
                self.cam.zoom = clamp(self.cam.zoom * (1.1 ** event.y), ZOOM_MIN, ZOOM_MAX)
                # optional: keep focus under cursor (simple approach: adjust offset)
                mx, my = pg.mouse.get_pos()
                cx, cy = self.screen.get_rect().center
                # world position under mouse before zoom
                wx_before = (mx - cx - self.cam.offset[0]) / old_zoom
                wy_before = -(my - cy - self.cam.offset[1]) / old_zoom
                # screen pos after zoom to keep same world point under cursor
                sx_after = cx + wx_before * self.cam.zoom + self.cam.offset[0]
                sy_after = cy - wy_before * self.cam.zoom + self.cam.offset[1]
                self.cam.offset = (
                    self.cam.offset[0] + (mx - sx_after),
                    self.cam.offset[1] + (my - sy_after),
                )
        return True

    def update(self, dt_sec: float) -> None:
        if not self.state.paused:
            self.state.sim_days += self.state.time_scale * dt_sec

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        center = self.screen.get_rect().center

        # draw bodies
        # Sun
        draw_sun(self.screen, center)

        for body in self.bodies:
            if body.name == "Sun":
                continue
            # temporarily pause trail updates if disabled
            if not self.state.show_trails:
                body.trail.clear()
            draw_body(
                self.screen,
                self.cam,
                body,
                self.state.sim_days,
                center,
                with_label=self.state.show_labels,
            )

        fps = self.clock.get_fps()
        draw_hud(
            self.screen,
            fps=fps,
            time_scale=self.state.time_scale,
            paused=self.state.paused,
            show_labels=self.state.show_labels,
            show_trails=self.state.show_trails,
        )

        pg.display.flip()

    def run(self) -> None:
        while True:
            if not self.handle_events():
                break
            dt = self.clock.tick(MAX_FPS) / 1000.0
            self.update(dt)
            self.draw()
        pg.quit()


def main() -> int:
    App().run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

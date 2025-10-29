#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Solar System Visualizer (Pygame)
File: test_physics.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-29
Updated: 2025-10-29
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Unit tests for simplified orbital mechanics helpers.

===========================================================================
"""
from __future__ import annotations

from math import isclose

from solar_system_visualizer.physics import (
    Orbit,
    mean_anomaly,
    elliptical_position,
    orbital_position_au,
    clamp,
    DAYS_PER_YEAR,
)


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10


def test_mean_anomaly_progresses():
    earth = Orbit(a_au=1.0, period_years=1.0, e=0.0167, phi0=0.0)
    m0 = mean_anomaly(0.0, earth)
    mhalf = mean_anomaly(0.5, earth)
    assert mhalf > m0


def test_elliptical_position_small_e_near_circle():
    x, y = elliptical_position(a=1.0, e=0.01, M=0.0)
    assert isclose(x, 1.0 - 0.01, rel_tol=0, abs_tol=1e-6)
    assert isclose(y, 0.0, rel_tol=0, abs_tol=1e-6)


def test_orbital_position_1year_returns_near_start():
    earth = Orbit(a_au=1.0, period_years=1.0, e=0.0167, phi0=0.3)
    x0, y0 = orbital_position_au(0.0, earth)
    x1, y1 = orbital_position_au(DAYS_PER_YEAR, earth)
    assert isclose(x0, x1, rel_tol=0, abs_tol=0.05)
    assert isclose(y0, y1, rel_tol=0, abs_tol=0.05)

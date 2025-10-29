#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================================================================
Project: Solar System Visualizer (Pygame)
File: physics.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-10-29
Updated: 2025-10-29
License: MIT License (see LICENSE file for details)
===========================================================================

Description:
Simplified orbital mechanics utilities. We model orbits using Keplerian
parameters (semi-major axis a [AU], period P [Earth years], eccentricity e,
longitude of periapsis (ignored here for simplicity), and initial phase).

This module is pure (no pygame) and covered by unit tests.

===========================================================================
"""
from __future__ import annotations

from dataclasses import dataclass
from math import cos, sin, tau
from typing import Tuple

SECONDS_PER_DAY = 86400
DAYS_PER_YEAR = 365.25


@dataclass(frozen=True)
class Orbit:
    a_au: float  # semi-major axis in astronomical units
    period_years: float
    e: float = 0.0  # eccentricity
    phi0: float = 0.0  # initial phase (radians)

    def mean_motion(self) -> float:
        """Return mean motion n [rad / year]."""
        return tau / self.period_years


# Simplified orbit catalog (a [AU], P [years], e)
# Values approximated to keep it educational and smooth.
ORBIT_DB = {
    "Mercury": Orbit(a_au=0.387, period_years=0.241, e=0.206, phi0=0.2),
    "Venus": Orbit(a_au=0.723, period_years=0.615, e=0.007, phi0=0.1),
    "Earth": Orbit(a_au=1.000, period_years=1.000, e=0.017, phi0=0.0),
    "Mars": Orbit(a_au=1.524, period_years=1.881, e=0.093, phi0=1.0),
    "Jupiter": Orbit(a_au=5.203, period_years=11.86, e=0.049, phi0=1.5),
    "Saturn": Orbit(a_au=9.537, period_years=29.45, e=0.056, phi0=2.0),
    "Uranus": Orbit(a_au=19.191, period_years=84.02, e=0.047, phi0=0.4),
    "Neptune": Orbit(a_au=30.07, period_years=164.8, e=0.009, phi0=3.1),
}


def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))


def days_to_years(days: float) -> float:
    return days / DAYS_PER_YEAR


def mean_anomaly(t_years: float, orbit: Orbit) -> float:
    """Mean anomaly M(t) = n*(t) + phi0 (radians)."""
    return (orbit.mean_motion() * t_years + orbit.phi0) % tau


def elliptical_position(a: float, e: float, M: float) -> Tuple[float, float]:
    """Approximate elliptical position from mean anomaly using a simple series.

    This avoids solving Kepler's equation exactly (no Newton iteration) to keep
    frame time light and predictable. For small e, the series is adequate.

    Returns: (x, y) in units of 'a' in the orbital plane.
    """
    # First-order approximation: E ≈ M + e*sin(M)
    E = M + e * sin(M)
    # Position in ellipse param by eccentric anomaly
    x = a * (cos(E) - e)
    y = a * (1 - e**2) ** 0.5 * sin(E)
    return x, y


def orbital_position_au(sim_days: float, orbit: Orbit) -> Tuple[float, float]:
    """Return planet position (x, y) in AU at simulation day."""
    t_years = days_to_years(sim_days)
    M = mean_anomaly(t_years, orbit)
    return elliptical_position(orbit.a_au, orbit.e, M)

from __future__ import annotations

import math


def hazard_rate_from_spread(spread: float, recovery_rate: float) -> float:
    """
    Approximate the hazard rate implied by a credit spread.

    Formula:
        hazard_rate ≈ spread / (1 - recovery_rate)

    Parameters
    ----------
    spread : float
        Credit spread in decimal form. Example: 0.02 for 200 bps.
    recovery_rate : float
        Recovery rate in decimal form. Example: 0.40 for 40%.

    Returns
    -------
    float
        Implied hazard rate in decimal form.
    """
    if spread < 0:
        raise ValueError("spread must be >= 0")
    if not 0 <= recovery_rate < 1:
        raise ValueError("recovery_rate must be in [0, 1)")

    return spread / (1 - recovery_rate)


def survival_probability(hazard_rate: float, maturity: float) -> float:
    """
    Compute survival probability under a constant hazard rate.

    Formula:
        S(T) = exp(-hazard_rate * T)
    """
    if hazard_rate < 0:
        raise ValueError("hazard_rate must be >= 0")
    if maturity < 0:
        raise ValueError("maturity must be >= 0")

    return math.exp(-hazard_rate * maturity)


def default_probability(hazard_rate: float, maturity: float) -> float:
    """
    Compute cumulative default probability under a constant hazard rate.

    Formula:
        PD(T) = 1 - exp(-hazard_rate * T)
    """
    return 1 - survival_probability(hazard_rate, maturity)

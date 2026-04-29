import math

import pytest

from creditlab.implied import (
    hazard_rate_from_spread,
    survival_probability,
    default_probability,
)


def test_hazard_rate_from_spread():
    hazard_rate = hazard_rate_from_spread(spread=0.02, recovery_rate=0.40)

    assert math.isclose(hazard_rate, 0.03333333333333333)


def test_hazard_rate_increases_with_spread():
    low_spread = hazard_rate_from_spread(spread=0.01, recovery_rate=0.40)
    high_spread = hazard_rate_from_spread(spread=0.03, recovery_rate=0.40)

    assert high_spread > low_spread


def test_hazard_rate_increases_with_recovery_rate():
    low_recovery = hazard_rate_from_spread(spread=0.02, recovery_rate=0.20)
    high_recovery = hazard_rate_from_spread(spread=0.02, recovery_rate=0.60)

    assert high_recovery > low_recovery


def test_survival_probability():
    survival = survival_probability(hazard_rate=0.03, maturity=5)

    assert 0 < survival < 1


def test_default_probability():
    pd = default_probability(hazard_rate=0.03, maturity=5)

    assert 0 < pd < 1


def test_default_probability_zero_maturity():
    pd = default_probability(hazard_rate=0.03, maturity=0)

    assert pd == 0


def test_invalid_spread():
    with pytest.raises(ValueError):
        hazard_rate_from_spread(spread=-0.01, recovery_rate=0.40)


def test_invalid_recovery_rate():
    with pytest.raises(ValueError):
        hazard_rate_from_spread(spread=0.02, recovery_rate=1.20)


def test_invalid_maturity():
    with pytest.raises(ValueError):
        survival_probability(hazard_rate=0.03, maturity=-1)
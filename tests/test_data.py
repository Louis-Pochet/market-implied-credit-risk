import pytest

from creditlab.data import fetch_fred_series


def test_fetch_fred_series_rejects_empty_series_id():
    with pytest.raises(ValueError):
        fetch_fred_series(series_id="", api_key="fake_key")
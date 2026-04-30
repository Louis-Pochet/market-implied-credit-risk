from __future__ import annotations

import os

import pandas as pd
import requests
from dotenv import load_dotenv


FRED_URL = "https://api.stlouisfed.org/fred/series/observations"


def get_fred_api_key() -> str:
    """
    Load the FRED API key from a .env file or from environment variables.
    """
    load_dotenv()

    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing FRED_API_KEY. Create a .env file with FRED_API_KEY=YOUR_KEY."
        )

    return api_key


def fetch_fred_series(series_id: str, api_key: str | None = None) -> pd.DataFrame:
    """
    Fetch a FRED time series and return a clean DataFrame with date and value.

    Parameters
    ----------
    series_id : str
        FRED series identifier.
    api_key : str | None
        FRED API key. If None, the function loads FRED_API_KEY from the environment.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: date and value.
    """
    if not series_id:
        raise ValueError("series_id must not be empty")

    if api_key is None:
        api_key = get_fred_api_key()

    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
    }

    response = requests.get(FRED_URL, params=params, timeout=30)
    response.raise_for_status()

    observations = response.json()["observations"]

    data = pd.DataFrame(observations)[["date", "value"]]
    data["date"] = pd.to_datetime(data["date"])
    data["value"] = pd.to_numeric(data["value"], errors="coerce")

    return data.dropna().sort_values("date").reset_index(drop=True)
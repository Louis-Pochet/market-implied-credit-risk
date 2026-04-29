# Market-Implied Credit Risk from Corporate Bond Spreads

![Tests](https://github.com/Louis-Pochet/market-implied-credit-risk/actions/workflows/tests.yml/badge.svg)


This project explores how corporate bond spreads can be interpreted as market-implied measures of default risk and how they relate to macro-financial conditions.

Using public data from FRED, the notebook combines simple credit risk intuition with empirical analysis to understand what spreads may signal about credit risk and the macro environment.

The objective is not to build a full pricing model, but to develop practical market intuition around credit spreads.

The project now includes a small reusable Python module, `src/creditlab/implied.py`, together with unit tests and GitHub Actions. The notebook uses FRED data for the empirical analysis, while the tests use controlled numerical examples and do not depend on external data.

---

# Motivation

Credit spreads are closely watched by traders because they react quickly to changes in risk sentiment, liquidity conditions, and macro expectations.

A widening spread can reflect deteriorating fundamentals, higher perceived default risk, or simply a shift in risk appetite. However, spreads are often discussed in isolation.

A natural question is:

**What does a given spread level imply in terms of default risk?**

This project starts from that question and builds a simple framework to translate spreads into structural credit measures.

The aim is to move from "spread watching" to a more risk-based interpretation.

---

# Data

The analysis relies on FRED time series, including:

• US BBB corporate OAS  
• US Investment Grade OAS  
• US 2-Year Treasury yield  

FRED provides transparent and reliable macro-financial data suitable for exploratory credit analysis.

A free FRED API key is required to run the notebook.

Users can create a `.env` file containing:

FRED_API_KEY=YOUR_KEY

The unit tests do not require a FRED API key. They only validate the core credit-risk logic with simple numerical inputs.

# Methodology

## From spreads to default risk

A simple reduced-form intuition links spreads and default risk:

spread ≈ (1 − recovery) × hazard rate

Assuming a constant recovery rate of 40%, spreads can be translated into implied hazard rates and survival probabilities.

This is a first-order approximation, but it provides an interpretable mapping between spreads and default risk.

---

## From hazard rates to CDS intuition

Using the implied hazard rate, a stylized fair CDS spread is computed under simplifying assumptions.

This connects bond spreads to CDS-style credit thinking, even though the framework remains simplified.

---

## Macro–credit relationship

The analysis then studies how changes in credit risk relate to changes in interest rates.

An OLS regression links:

Δ hazard rate  
to  
Δ 2-year Treasury yield

The slope coefficient can be interpreted as a macro-credit sensitivity, indicating how credit risk tends to co-move with rates.

A rolling regression is also implemented to show that this relationship is time-varying.

This mirrors how practitioners monitor regime changes in credit markets.

---

---

# Code and Tests

The reusable credit-risk functions are located in:

```text
src/creditlab/implied.py
```

They include:

```python
hazard_rate_from_spread
survival_probability
default_probability
```

To run the tests:

```bash
pip install -e .
python -m pytest
```

GitHub Actions runs these tests automatically after each push.

# Key Insights

The notebook illustrates that:

• Spreads can be translated into default-risk measures  
• Simple assumptions already improve interpretability  
• Credit risk and rates exhibit time-varying relationships  
• Rolling estimates highlight changing market regimes

Even a stylized framework can make spread dynamics more intuitive.

---

# Limitations

This framework relies on strong simplifications:

• constant recovery rate  
• flat hazard rates  
• no liquidity or risk-premium decomposition  
• simple linear macro relationship

The project is best viewed as an intuition-building exercise rather than a pricing tool.

---

# Possible Extensions

Natural extensions include:

• time-varying recovery assumptions  
• multi-factor macro models  
• CDS–bond basis analysis  
• regime-switching models

---

# Author

Louis Pochet  
Master in Financial Analysis  
---

*Personal project — not investment advice.*

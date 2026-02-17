# Market-Implied Credit Risk and Relative Value in Corporate Bond Spreads

This project studies how corporate bond spreads embed information about default risk and relative value in credit markets.

Using FRED data, it combines simple reduced-form credit intuition with empirical analysis to replicate how a credit trader might interpret spread dynamics.

The objective is not full pricing accuracy, but market intuition and signal extraction.

---

# Motivation

Corporate credit spreads reflect:

• expected default losses  
• risk premia  
• macro and market conditions  

Rather than treating spreads as raw data, this project interprets them through credit risk theory and simple empirical models.

This mirrors how traders think about spread levels and dislocations.

---

# Data

Data is sourced from FRED (Federal Reserve Bank of St. Louis):

• Investment Grade OAS  
• BBB OAS  

A free FRED API key is required.

Create a `.env` file:

FRED_API_KEY=YOUR_KEY

(`.env.example` provided)

---

# Methodology

## 1) Market-Implied Default Risk

Using a reduced-form approximation:

spread ≈ (1 − Recovery) × hazard rate

Assuming a 40% recovery rate, the project derives:

• implied hazard rates  
• survival probabilities  
• stylized fair CDS spreads  

This provides a structural interpretation of spreads.

---

## 2) Credit Beta via OLS

An OLS regression relates BBB spreads to IG spreads:

BBB_spread = α + β × IG_spread + ε

Interpretation:

• β → credit beta (systematic sensitivity)  
• residuals → relative value signal  

This mimics how desks monitor spread relationships.

---

## 3) Relative Value Signal

Residuals from the regression capture deviations from model value:

• positive residual → potentially cheap  
• negative residual → potentially rich  

This is a simplified proxy for RV monitoring.

---

## 4) Stylized Backtest

A simple backtest evaluates how spreads behave after large deviations from model-implied value.

This is illustrative rather than a tradable strategy.

---

# Key Takeaways

• Credit spreads can be translated into default risk measures  
• Spread relationships exhibit stable co-movements  
• Deviations from these relationships may indicate dislocations  
• Even simple models provide useful market intuition  

---

# Limitations

This project uses simplifying assumptions:

• constant recovery rate  
• flat hazard rates  
• simple OLS framework  
• no liquidity or transaction costs  
• no structural credit modeling  

The goal is intuition, not production-grade pricing.

---

# Possible Extensions

• Multi-factor credit models  
• Regime-dependent betas  
• CDS-bond basis analysis  
• Macro-linked spread modeling  
• Z-score based RV signals  

---

# Author

Louis Pochet  
Master in Financial Analysis

---

*Personal project — not investment advice.*

#!/usr/bin/env python3
"""
PPP (Purchasing Power Parity) Model for Currency Misalignment Analysis

This script calculates the degree of currency misalignment based on the
Purchasing Power Parity theory. It compares the actual exchange rate with
the PPP-implied exchange rate derived from price level indices.
"""

def calculate_ppp(domestic_price, foreign_price, current_exchange_rate):
    """
    Calculate currency misalignment based on PPP theory.
    
    Parameters:
    domestic_price (float): Price level index in domestic country (e.g., CPI).
    foreign_price (float): Price level index in foreign country.
    current_exchange_rate (float): Current spot exchange rate (domestic/foreign).
    
    Returns:
    dict: Contains PPP-implied exchange rate and misalignment percentage.
           Positive misalignment means the domestic currency is overvalued.
    """
    # PPP-implied exchange rate = domestic_price / foreign_price
    ppp_implied_rate = domestic_price / foreign_price
    
    # Percentage misalignment = (current - ppp) / ppp * 100%
    misalignment_pct = ((current_exchange_rate - ppp_implied_rate) / ppp_implied_rate) * 100.0
    
    return {
        "ppp_implied_rate": ppp_implied_rate,
        "misalignment_percent": misalignment_pct
    }


def main():
    """Example usage of the PPP model."""
    # Example data: US (domestic) vs Eurozone (foreign)
    # Price levels (CPI indices relative to base year)
    us_cpi = 120.5          # US price level index
    eu_cpi = 115.2          # Eurozone price level index
    current_eur_usd = 1.08  # EUR/USD exchange rate (USD per EUR)
    
    result = calculate_ppp(us_cpi, eu_cpi, current_eur_usd)
    
    print("=== PPP Currency Misalignment Analysis ===")
    print(f"Domestic (US) price level index: {us_cpi}")
    print(f"Foreign (EU) price level index: {eu_cpi}")
    print(f"Current exchange rate (USD/EUR): {current_eur_usd}")
    print(f"PPP-implied exchange rate (USD/EUR): {result['ppp_implied_rate']:.4f}")
    print(f"Misalignment: {result['misalignment_percent']:.2f}%")
    
    if result['misalignment_percent'] > 0:
        print("Interpretation: Domestic currency (USD) is OVERVALUED relative to PPP.")
    else:
        print("Interpretation: Domestic currency (USD) is UNDERVALUED relative to PPP.")


if __name__ == "__main__":
    main()
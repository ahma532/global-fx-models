#!/usr/bin/env python3
"""
PPP (Purchasing Power Parity) Model for Currency Misalignment Analysis

This script calculates the degree of currency misalignment based on the
Purchasing Power Parity theory. It compares the actual exchange rate with
the PPP-implied exchange rate derived from price level indices.

Extended with International Fisher Effect (IFE) to incorporate interest rate
differentials, providing a more comprehensive view of currency valuation.
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


def calculate_ife(domestic_interest, foreign_interest):
    """
    Calculate predicted exchange rate change based on International Fisher Effect.
    
    The IFE states that the currency of the country with the higher interest rate
    will depreciate by an amount equal to the interest rate differential.
    
    Parameters:
    domestic_interest (float): Domestic nominal interest rate (as decimal, e.g., 0.05 for 5%).
    foreign_interest (float): Foreign nominal interest rate (as decimal).
    
    Returns:
    dict: Contains predicted percentage change in exchange rate (domestic/foreign).
           Positive change means domestic currency depreciation (exchange rate increase).
    """
    # Exact formula: (1 + domestic) / (1 + foreign) - 1
    predicted_change = ((1 + domestic_interest) / (1 + foreign_interest) - 1) * 100.0
    # Approximate differential (for small interest rates)
    approx_change = (domestic_interest - foreign_interest) * 100.0
    
    return {
        "predicted_change_exact": predicted_change,
        "predicted_change_approx": approx_change,
        "interest_differential": (domestic_interest - foreign_interest) * 100.0
    }


def main():
    """Example usage of the combined PPP and IFE model."""
    # Example data: US (domestic) vs Eurozone (foreign)
    # Price levels (CPI indices relative to base year)
    us_cpi = 120.5          # US price level index
    eu_cpi = 115.2          # Eurozone price level index
    current_eur_usd = 1.08  # EUR/USD exchange rate (USD per EUR)
    
    # Interest rates (annual nominal, as decimals)
    us_interest = 0.045     # 4.5% US interest rate
    eu_interest = 0.025     # 2.5% Eurozone interest rate
    
    # PPP analysis
    ppp_result = calculate_ppp(us_cpi, eu_cpi, current_eur_usd)
    
    # IFE analysis
    ife_result = calculate_ife(us_interest, eu_interest)
    
    print("=== Combined Currency Valuation Analysis ===")
    print("\n--- PPP (Long‑Term) Perspective ---")
    print(f"Domestic (US) price level index: {us_cpi}")
    print(f"Foreign (EU) price level index: {eu_cpi}")
    print(f"Current exchange rate (USD/EUR): {current_eur_usd}")
    print(f"PPP-implied exchange rate (USD/EUR): {ppp_result['ppp_implied_rate']:.4f}")
    print(f"PPP misalignment: {ppp_result['misalignment_percent']:.2f}%")
    
    if ppp_result['misalignment_percent'] > 0:
        print("  → USD is OVERVALUED relative to PPP.")
    else:
        print("  → USD is UNDERVALUED relative to PPP.")
    
    print("\n--- IFE (Short‑to‑Medium‑Term) Perspective ---")
    print(f"Domestic (US) interest rate: {us_interest*100:.2f}%")
    print(f"Foreign (EU) interest rate: {eu_interest*100:.2f}%")
    print(f"Interest rate differential (US‑EU): {ife_result['interest_differential']:.2f}%")
    print(f"Predicted exchange rate change (exact): {ife_result['predicted_change_exact']:.2f}%")
    print(f"Predicted exchange rate change (approximate): {ife_result['predicted_change_approx']:.2f}%")
    
    if ife_result['predicted_change_exact'] > 0:
        print("  → USD expected to DEPRECIATE (exchange rate ↑) according to IFE.")
    else:
        print("  → USD expected to APPRECIATE (exchange rate ↓) according to IFE.")
    
    print("\n--- Combined Signal ---")
    print("PPP reflects long‑term equilibrium based on price levels.")
    print("IFE reflects short‑term expectations driven by interest rates.")
    print("A holistic view considers both signals:")
    print("  - If PPP and IFE point in the same direction, the signal is stronger.")
    print("  - If they conflict, further analysis of other factors is warranted.")
    
    # Simple combined indicator (weighted average: 50% PPP, 50% IFE)
    weight_ppp = 0.5
    weight_ife = 0.5
    combined_signal = (weight_ppp * ppp_result['misalignment_percent'] +
                      weight_ife * ife_result['predicted_change_exact'])
    print(f"\nWeighted combined signal (50% PPP, 50% IFE): {combined_signal:.2f}%")
    if combined_signal > 0:
        print("  → Combined indicator suggests USD OVERVALUED / likely to depreciate.")
    else:
        print("  → Combined indicator suggests USD UNDERVALUED / likely to appreciate.")


if __name__ == "__main__":
    main()
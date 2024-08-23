import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Price a European call option using the Black-Scholes formula.
    
    Parameters:
    S (float): Stock price
    K (float): Strike price
    T (float): Time to maturity in years
    r (float): Risk-free interest rate
    sigma (float): Volatility of the stock

    Returns:
    float: Call option price
    """

    if sigma == 0 or T == 0:
        sigma = 1e-10  # prevent division by zero by using a small number
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = (S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
    return call_price


import unittest
from bsm import black_scholes_call  # Replace 'your_module' with the actual module name where the function is saved

class TestBlackScholesCall(unittest.TestCase):
    
    def test_call_option_price(self):
        # Test with known values
        S = 100       # Current stock price
        K = 100       # Strike price
        T = 1         # Time to maturity in years
        r = 0.05      # Risk-free interest rate
        sigma = 0.2   # Volatility
        result = black_scholes_call(S, K, T, r, sigma)
        expected = 10.45  # Known result from standard option pricing calculators
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_zero_time_to_expiry(self):
        # When time to expiry is 0, the call price should be max(S-K, 0)
        S = 100
        K = 95
        T = 0
        r = 0.05
        sigma = 0.2
        result = black_scholes_call(S, K, T, r, sigma)
        expected = max(S - K, 0)
        self.assertEqual(result, expected)
    
    def test_high_volatility(self):
	S = 100
    	K = 100
    	T = 1
    	r = 0.05
    	sigma = 3.0  # Very high volatility
    	result = black_scholes_call(S, K, T, r, sigma)
    	print("Resulting Call Price:", result)
    	print("Expected to be greater than:", S)
    	# Check if the result is logically higher as expected
	self.assertTrue(result > S, f"Expected the option price to be greater than {S}, but got {result}")

if __name__ == '__main__':
    	unittest.main()

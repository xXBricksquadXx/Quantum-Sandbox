def calculate_bayes_factor(successes, trials, null_prob=0.5):
    """
    Compares H0 (Chance) vs H1 (Psi/Anomalous influence).
    The Bayes Factor tells you how much more likely H1 is than H0.
    """
    from scipy.stats import binom
    
    # Likelihood of data under H0 (Standard Randomness)
    likelihood_h0 = binom.pmf(successes, trials, null_prob)
    
    # Likelihood of data under H1 (Hypothetical Shift, e.g., 51% instead of 50%)
    likelihood_h1 = binom.pmf(successes, trials, null_prob + 0.01)
    
    bayes_factor = likelihood_h1 / likelihood_h0
    return bayes_factor

# Advice: If Bayes Factor > 3, it's 'substantial' evidence. 
# If it's < 1, the 'Mind' hypothesis is losing to standard physics.
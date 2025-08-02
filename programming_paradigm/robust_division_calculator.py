def safe_divide(numerator, denominator):
    """Safely performs division, handling errors."""
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result:.2f}"
    except ValueError:
        return "Error: Both inputs must be numbers."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
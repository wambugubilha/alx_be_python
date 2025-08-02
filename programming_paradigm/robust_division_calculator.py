def safe_divide(numerator, denominator):
    """Safely performs division, handling errors."""
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
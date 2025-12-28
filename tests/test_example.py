"""Example test file to demonstrate the testing setup."""

from tabula import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello from tabula!"


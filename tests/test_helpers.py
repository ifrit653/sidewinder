import pytest
import app.helpers as helpers_functions
from app.models import BlacklistedToken
from app import db

# TODO: fix the test script 

def test_isTokenExpired(app):
    with app.app_context():  # Ensuring that the test runs within the app context
        # Create a new blacklisted token
        token = BlacklistedToken(jti="test-jti")
        db.session.add(token)
        db.session.commit()

        # Test if the token is expired
        result = helpers_functions.isTokenExpired("test-jti")
        assert result == True

        # Test if a non-existent token is expired
        assert helpers_functions.isTokenExpired("non-existent-jti") == False

        # Clean up by deleting the token
        db.session.delete(token)
        db.session.commit()

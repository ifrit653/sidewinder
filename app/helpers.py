from app.models import BlacklistedToken

def isTokenExpired(jti):
    token = BlacklistedToken.query.filter_by(jti=jti).first()
    return token is not None

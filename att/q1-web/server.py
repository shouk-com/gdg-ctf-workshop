from flask import Flask, jsonify, request
import jwt
from functools import wraps

app = Flask(__name__)

SECRET_KEY = 'super_secret_key_123456789012345'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Get token from Authorization header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'message': 'Bearer token malformed'}), 401
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            data = jwt.decode(
                token, 
                SECRET_KEY,
                algorithm='HS256'
            )
            current_user = data['user']
        except jwt.PyJWTError as e:
            return jsonify({'message': 'Token is invalid', 'error': str(e)}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated


@app.route('/')
@token_required
def validate():
    return jsonify({
        "message": "Token validated!",
    })

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
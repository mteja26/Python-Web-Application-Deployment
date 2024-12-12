import json

def create_response(data, status_code=200):
    """Create a standardized response"""
    return {
        'status_code': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(data)
    }
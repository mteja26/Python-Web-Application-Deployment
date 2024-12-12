import urllib.request
import sys
import json

def check_health():
    """Check if the server is healthy"""
    try:
        req = urllib.request.Request('http://localhost:8000/')
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read())
                return data.get('status') == 'healthy'
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
    return False

if __name__ == '__main__':
    is_healthy = check_health()
    sys.exit(0 if is_healthy else 1)
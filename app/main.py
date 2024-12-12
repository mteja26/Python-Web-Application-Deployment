import sys
import json
from app.utils.logger import logger
from app.server.handler import APIHandler
from app.config import Config

def write_response(response_data):
    """Write response to stdout"""
    sys.stdout.buffer.write(f"HTTP/1.1 {response_data['status_code']}\r\n".encode())
    for header, value in response_data['headers'].items():
        sys.stdout.buffer.write(f"{header}: {value}\r\n".encode())
    sys.stdout.buffer.write(b"\r\n")
    sys.stdout.buffer.write(response_data['body'].encode())
    sys.stdout.buffer.flush()

def handle_request(path):
    """Route requests to appropriate handlers"""
    handler = APIHandler()
    
    if path == '/':
        return handler.handle_health_check()
    return handler.handle_not_found()

def run_server():
    """Run a simple request handler"""
    logger.info(f"Starting {Config.APP_NAME} v{Config.VERSION}")
    logger.info(f"Server running on port {Config.Development.PORT}")
    
    try:
        while True:
            # Simple request handling
            path = input("Enter path (or 'exit' to quit): ")
            if path.lower() == 'exit':
                break
                
            response = handle_request(path)
            write_response(response)
            
    except KeyboardInterrupt:
        logger.info("Server shutting down...")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    run_server()
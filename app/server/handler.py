import json
from app.utils.response import create_response
from app.config import Config

class APIHandler:
    """Handles API endpoints and their responses"""
    
    @staticmethod
    def handle_health_check():
        """Handle health check endpoint"""
        return create_response({
            'status': 'healthy',
            'service': Config.APP_NAME,
            'version': Config.VERSION
        }, 200)
    
    @staticmethod
    def handle_not_found():
        """Handle 404 Not Found responses"""
        return create_response({
            'error': 'Not Found'
        }, 404)
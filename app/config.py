class Config:
    APP_NAME = "python-web-app"
    VERSION = "1.0.0"
    
    # Development configuration
    class Development:
        DEBUG = True
        PORT = 8000
        
    # Production configuration
    class Production:
        DEBUG = False
        PORT = 80
        
    # Testing configuration
    class Testing:
        DEBUG = True
        PORT = 8001
        TESTING = True
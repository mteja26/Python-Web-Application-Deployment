# Python Web Application Deployment

This project demonstrates a basic structure for a Python web application with deployment scripts. While it's a simplified version due to environment constraints, it shows the key concepts of a deployment pipeline.

## Project Structure

```
.
├── app/
│   ├── main.py          # Main application server
│   ├── config.py        # Configuration management
│   └── health_check.py  # Health check utility
├── tests/
│   └── test_app.py      # Unit tests
├── scripts/
│   └── deploy.py        # Deployment simulation script
└── README.md
```

## Features

- Simple HTTP server with health check endpoint
- Environment-specific configuration management
- Unit tests
- Simulated deployment pipeline
- Health check utility

## Running the Application

1. Start the server:
   ```
   python app/main.py
   ```

2. Run tests:
   ```
   python -m unittest tests/test_app.py
   ```

3. Simulate deployment:
   ```
   python scripts/deploy.py
   ```

## Health Checks

The application includes a health check endpoint at `/` that returns a JSON response with the service status.

## Configuration

The application supports different environments (Development, Production, Testing) with specific configurations for each environment.

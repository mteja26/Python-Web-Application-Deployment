import os
import sys
import time
from datetime import datetime

def simulate_deployment():
    """
    Simulates a deployment process with different stages
    """
    stages = [
        ("Validating configuration", 1),
        ("Running tests", 2),
        ("Building application", 1),
        ("Preparing deployment", 1),
        ("Deploying to environment", 2),
        ("Running health checks", 1),
        ("Finalizing deployment", 1)
    ]
    
    print(f"\nStarting deployment at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    for stage, duration in stages:
        print(f"\n→ {stage}...")
        time.sleep(duration)  # Simulate work being done
        print(f"✓ {stage} completed")
    
    print("\n" + "=" * 50)
    print("Deployment completed successfully!")
    print(f"Deployment finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    try:
        simulate_deployment()
    except KeyboardInterrupt:
        print("\nDeployment cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nDeployment failed: {e}")
        sys.exit(1)
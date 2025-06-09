#!/usr/bin/env python3

import sys
import os
from pathlib import Path

# Allow running this test from anywhere
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir / "lib"))
sys.path.insert(0, str(root_dir))

def test_imports():
    try:
        from mcp_server.main import app
        print("✓ FastAPI app created successfully")
        
        from mcp_server.auth.jwt_auth import create_dev_token
        token = create_dev_token("test-user", admin=True)
        print(f"✓ JWT token created: {token[:20]}...")
        
        from storage.local_storage import LocalStorage
        storage = LocalStorage("/tmp/test")
        print("✓ Local storage initialized")
        
        from models.pattern_models import PatternResponse
        print("✓ Pattern models imported")
        
        print("All imports successful!")
        return True
    except Exception as e:
        print(f"Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    os.environ["WORK_DIR"] = "/tmp/mcp_test_data"
    os.environ["JWT_SECRET_KEY"] = "test-secret-key"
    os.environ["LOG_LEVEL"] = "INFO"
    test_imports()

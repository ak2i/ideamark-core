#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, '/home/ubuntu/repos/ideamark-core/tools/src')

def test_imports():
    try:
        from main import app
        print("✓ FastAPI app created successfully")
        
        from auth.jwt_auth import create_dev_token
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

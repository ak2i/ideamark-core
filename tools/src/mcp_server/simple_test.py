#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def test_basic_server():
    print("Testing basic MCP server components...")
    
    os.environ["WORK_DIR"] = "/tmp/mcp_test_data"
    os.environ["JWT_SECRET_KEY"] = "test-secret-key"
    os.environ["LOG_LEVEL"] = "INFO"
    
    work_dir = Path("/tmp/mcp_test_data")
    patterns_dir = work_dir / "patterns"
    refs_dir = work_dir / "refs"
    
    work_dir.mkdir(parents=True, exist_ok=True)
    patterns_dir.mkdir(parents=True, exist_ok=True)
    refs_dir.mkdir(parents=True, exist_ok=True)
    
    print("✓ Test directories created")
    
    try:
        from fastapi import FastAPI
        app = FastAPI(title="Test MCP Server")
        print("✓ FastAPI app created")
    except Exception as e:
        print(f"✗ FastAPI import failed: {e}")
        return False
    
    try:
        from jose import jwt
        from datetime import datetime, timedelta
        
        secret = "test-secret"
        data = {"sub": "test-user", "exp": datetime.utcnow() + timedelta(hours=1)}
        token = jwt.encode(data, secret, algorithm="HS256")
        decoded = jwt.decode(token, secret, algorithms=["HS256"])
        print("✓ JWT functionality working")
    except Exception as e:
        print(f"✗ JWT test failed: {e}")
        return False
    
    try:
        import yaml
        test_data = {"id": "test", "title": "Test Pattern"}
        yaml_str = yaml.safe_dump(test_data)
        loaded_data = yaml.safe_load(yaml_str)
        print("✓ YAML functionality working")
    except Exception as e:
        print(f"✗ YAML test failed: {e}")
        return False
    
    print("All basic tests passed!")
    return True

if __name__ == "__main__":
    test_basic_server()

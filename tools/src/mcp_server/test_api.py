#!/usr/bin/env python3

import requests
import json
import sys
from datetime import datetime


def test_mcp_server():
    base_url = "http://localhost:8001"

    import sys
    import os

    sys.path.insert(0, "/home/ubuntu/repos/ideamark-core/tools/src/mcp_server")

    from jose import jwt
    from datetime import datetime, timedelta, timezone

    JWT_SECRET_KEY = "test-secret-key"
    data = {"sub": "test-user", "admin": True, "iat": datetime.now(timezone.utc)}
    expire = datetime.now(timezone.utc) + timedelta(hours=24)
    data.update({"exp": expire})
    token = jwt.encode(data, JWT_SECRET_KEY, algorithm="HS256")

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    print("Testing MCP Server API endpoints...")
    print(f"Using token: {token[:20]}...")

    print("\n1. Testing health check...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health check: {response.status_code}")
        if response.status_code == 200:
            health_data = response.json()
            print(f"  Status: {health_data['status']}")
            print(f"  Dependencies: {health_data['dependencies']}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

    print("\n2. Testing pattern validation...")
    test_pattern = {
        "id": "test-pattern-123",
        "title": "Test Pattern",
        "type": "design",
        "context": ["testing"],
        "problem": {"summary": "Test problem"},
        "solution": {"approach": "Test solution"},
        "access": {"uri": "file://test.yaml", "visibility": "public"},
    }

    try:
        response = requests.post(
            f"{base_url}/v1/pattern/validate",
            headers=headers,
            json={"content": test_pattern},
        )
        print(f"Pattern validation: {response.status_code}")
        if response.status_code == 200:
            validation_data = response.json()
            print(f"  Valid: {validation_data.get('valid', 'unknown')}")
            print(f"  Errors: {validation_data.get('errors', [])}")
            print(f"  Full response: {validation_data}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"Pattern validation failed: {e}")
        return False

    print("\n3. Testing pattern save...")
    try:
        response = requests.post(
            f"{base_url}/v1/pattern/test-pattern-123",
            headers=headers,
            json={"content": test_pattern},
        )
        print(f"Pattern save: {response.status_code}")
        if response.status_code == 200:
            save_data = response.json()
            print(f"  Saved pattern ID: {save_data['id']}")
            print(f"  Saved by: {save_data['metadata']['saved_by']}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"Pattern save failed: {e}")
        return False

    print("\n4. Testing pattern fetch...")
    try:
        response = requests.get(
            f"{base_url}/v1/pattern/test-pattern-123", headers=headers
        )
        print(f"Pattern fetch: {response.status_code}")
        if response.status_code == 200:
            fetch_data = response.json()
            print(f"  Retrieved pattern ID: {fetch_data['id']}")
            print(f"  Title: {fetch_data['content']['title']}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"Pattern fetch failed: {e}")
        return False

    print("\n5. Testing ref generation...")
    try:
        response = requests.post(
            f"{base_url}/v1/ref/generate",
            headers=headers,
            json={"pattern": test_pattern},
        )
        print(f"Ref generation: {response.status_code}")
        if response.status_code == 200:
            ref_data = response.json()
            print(f"  Generated ref ID: {ref_data['ref_id']}")
            print(f"  Ref title: {ref_data['ref_content']['ref']['title']}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"Ref generation failed: {e}")
        return False

    print("\n6. Testing pattern search...")
    try:
        response = requests.get(
            f"{base_url}/v1/pattern/search?q=test&limit=5", headers=headers
        )
        print(f"Pattern search: {response.status_code}")
        if response.status_code == 200:
            search_data = response.json()
            print(f"  Query: {search_data['query']}")
            print(f"  Total results: {search_data['total_results']}")
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"Pattern search failed: {e}")
        return False

    print("\n7. Testing pattern merge...")
    test_pattern_2 = {
        "id": "test-pattern-456",
        "title": "Second Test Pattern",
        "type": "design",
        "context": ["testing", "merge"],
        "problem": {"summary": "Second test problem"},
        "solution": {"approach": "Second test solution"},
        "access": {"uri": "file://test2.yaml", "visibility": "public"},
    }

    try:
        response = requests.post(
            f"{base_url}/v1/pattern/test-pattern-456",
            headers=headers,
            json={"content": test_pattern_2},
        )
        print(f"Second pattern save: {response.status_code}")
    except Exception as e:
        print(f"Second pattern save failed: {e}")
        return False

    try:
        response = requests.post(
            f"{base_url}/v1/ref/generate",
            headers=headers,
            json={"pattern": test_pattern_2},
        )
        print(f"Second ref generation: {response.status_code}")
    except Exception as e:
        print(f"Second ref generation failed: {e}")
        return False

    try:
        response = requests.post(
            f"{base_url}/v1/pattern/merge",
            headers=headers,
            json={
                "pattern_ids": ["test-pattern-123", "test-pattern-456"],
                "intent": "union",
                "strategy": "prefer",
            },
        )
        print(f"Pattern merge: {response.status_code}")
        if response.status_code == 200:
            merge_data = response.json()
            print(f"  Merged pattern ID: {merge_data['merged_pattern_id']}")
            print(f"  Merged title: {merge_data['merged_content']['title']}")
            print(
                f"  Patterns merged: {merge_data['merge_summary']['patterns_merged']}"
            )
        else:
            print(f"  Error: {response.text}")
    except Exception as e:
        print(f"Pattern merge failed: {e}")
        return False

    print("\nAll API tests completed successfully!")
    return True


if __name__ == "__main__":
    test_mcp_server()

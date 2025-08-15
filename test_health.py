import sys
sys.path.append('/home/ubuntu/repos/ideamark-core')

import pytest
from lib.mcp_server.api.health import health_check


@pytest.mark.asyncio
async def test_health() -> None:
    """Verify the health check reports required fields and dependencies."""
    result = await health_check()

    required_fields = ["status", "version", "timestamp", "dependencies", "metrics"]
    for field in required_fields:
        assert field in result, f"missing field {field}"

    deps = result.get("dependencies", {})
    expected_deps = ["schema_validator", "llm_provider", "github_api", "storage"]
    for dep in expected_deps:
        assert dep in deps, f"missing dependency {dep}"


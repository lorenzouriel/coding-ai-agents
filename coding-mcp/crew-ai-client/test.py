import requests
import json

MCP_URL = "http://localhost:8080/info"

print("Testing MCP Server Connection...\n")

# Test 1: Check if server is running
print("1. Testing basic connectivity...")
try:
    response = requests.get(MCP_URL, timeout=5)
    print(f"   ✓ Server responding: {response.status_code}")
except requests.exceptions.ConnectionError:
    print("   ✗ Cannot connect to server - is it running?")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test 2: Check MCP endpoint
print("\n2. Testing MCP endpoint...")
try:
    response = requests.get(f"{MCP_URL}/mcp", timeout=5)
    print(f"   ✓ MCP endpoint responding: {response.status_code}")
    print(f"   Response: {response.text[:200]}")
except requests.exceptions.ConnectionError:
    print("   ✗ Cannot connect to /mcp endpoint")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test 3: List available endpoints
print("\n3. Checking available endpoints...")
try:
    response = requests.get(f"{MCP_URL}/", timeout=5)
    print(f"   Status: {response.status_code}")
    if response.text:
        print(f"   Response: {response.text[:500]}")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "="*60)
print("DIAGNOSTICS:")
print("="*60)
print("\nIf tests failed:")
print("1. Verify the MCP server is running on port 8080")
print("2. Check if it's using HTTP (not HTTPS)")
print("3. Verify the endpoint path (should it be /mcp or something else?)")
print("\nTo start a local MCP server, you might need to run:")
print("  - Your MCP server application")
print("  - Or check documentation for server setup instructions")
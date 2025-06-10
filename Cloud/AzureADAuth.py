import requests

# Azure AD details
tenant_id = "122ec050-e01"  # your tenant ID
client_id = "f52bf357-9cf915e5de7d"
client_secret = "ZpJ8Q~-fHdwsHQKCFOp5ca8a"
scope = "https://graph.microsoft.com/.default"  # or another valid resource

# Token endpoint for client credentials flow
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Prepare data for POST request
data = {
    "client_id": client_id,
    "scope": scope,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

# Send the request
response = requests.post(token_url, data=data)

# Output result
if response.status_code == 200:
    print("✅ Client ID and Secret are valid.")
    print("Access Token:", response.json()["access_token"][:60], "...")
else:
    print("❌ Failed to authenticate.")
    print("Status Code:", response.status_code)
    print("Response:", response.json())

"""MARVIN Mobile Gateway: the only network-facing surface for paired devices.

Runs inside the Presence process (same Runtime, queue and approvals) or headless.
Vault and provider credentials stay on this computer; devices hold revocable tokens.
"""
GATEWAY_VERSION = "0.1.0"
API_VERSION = 1

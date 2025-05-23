#!/usr/bin/env python3

import os
import sys

# Import your research server
from research_server import mcp

def main():
    """Start the MCP research server for deployment."""
    print("Starting MCP Research Server...")
    
    # Get port from environment (Render sets this)
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    # Run the server with streamable-http transport
    mcp.run(transport='streamable-http', mount_path="/", port=port, host=host)

if __name__ == "__main__":
    main()

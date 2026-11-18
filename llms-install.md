# Install Precision AI OS MCP in Cline

This is a remote MCP server. Do not clone the repository to run a local process, and do not look for an npm start script or a Docker build. Connect Cline to the shared Streamable HTTP endpoint and complete OAuth.

## Server

- Name: Precision AI OS
- URL: https://mcp.getprecision.ai/v1/mcp
- Transport: Streamable HTTP
- Authentication: OAuth through Clerk. Only people with the operator role in a Precision firm can connect.

## Steps

1. In Cline, add a remote MCP server (sometimes labeled HTTP or Streamable HTTP).
2. Set the server name to precision and the URL to https://mcp.getprecision.ai/v1/mcp.
3. When the client opens a browser, sign in with the firm's Precision account and allow access.
4. If sign-in does not start, check that the client supports remote MCP and OAuth, then retry the server's Connect or authentication prompt.
5. After sign-in, try a read-only request such as listing the firm's agents or showing the firm's Rules.

Do not paste an API key, bearer token, or a per-firm MCP URL unless the user already chose a per-firm address in the Precision app under Setup → Precision MCP. The shared address is the default.

Approving work, connecting a person's inbox or apps, and signing in to websites stay with people in the Precision app. The MCP never sends anything itself.

Setup guide: https://getprecision.ai/mcp?utm_source=cline&utm_medium=listing&utm_campaign=marketplace
Support: hello@getprecision.ai

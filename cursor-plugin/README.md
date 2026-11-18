# Precision AI OS

Set up and run your firm's Precision AI agents, skills and routines from any MCP client.

AI agents for CPA and accounting firms and other professional service firms. Agents prepare the work. Sends wait for your team's approval by default.

This Cursor plugin connects the remote Precision AI OS MCP server over Streamable HTTP. Sign in with your firm's Precision operator account through Clerk. The shared server address is `https://mcp.getprecision.ai/v1/mcp`. The server resolves your authorized firm after sign-in. No firm ID, API key, bearer header or environment variable belongs in this package.

Operators can create and manage agents, skills, routines, websites, firm logins, settings and Rules; add Agent OS notes and clients; and check routines, jobs and connected apps. Use ask_agent to give an agent work. Approving work, connecting a person's inbox or apps, and signing in to websites stay with people in the app. The MCP never sends anything itself. Every write is logged under the signed-in person's name.

Reading existing working content (tasks, chats, notes and the client list) is off unless the firm's deployment allows it.

## Install and sign in

After Marketplace acceptance, open Cursor Customize, find Precision AI OS, and install it at project or user scope. Complete OAuth as the firm's operator, then try "List my firm's agents" or "Show my firm's Rules."

You can also add the server by hand. Merge this entry into `~/.cursor/mcp.json` and keep any existing servers:

```json
{
  "mcpServers": {
    "precision": {
      "url": "https://mcp.getprecision.ai/v1/mcp"
    }
  }
}
```

Then open the server in Cursor's MCP settings and use its Connect or authentication prompt.

The [Add to Cursor](ADD-TO-CURSOR.md) link installs the MCP connection. It is not a Marketplace listing. Use one installation route per profile to avoid duplicate connections.

If sign-in fails, confirm your Precision operator access, retry the OAuth connection and review the [Precision MCP guide](https://getprecision.ai/mcp?utm_source=cursormarketplace&utm_medium=listing&utm_campaign=marketplace). Do not paste a token into this repository or substitute another firm's address. Ask your Precision administrator if you lack access. Enterprise administrators can restrict plugins and local imports.

Access is limited to people with the operator role in the relevant firm. If you operate more than one firm, choose which firm the shared address uses in the app under Setup → Precision MCP.

## Product and legal

- Product and setup: [getprecision.ai/mcp](https://getprecision.ai/mcp?utm_source=cursormarketplace&utm_medium=listing&utm_campaign=marketplace)
- Privacy: [getprecision.ai/legal/privacy](https://getprecision.ai/legal/privacy?utm_source=cursormarketplace&utm_medium=listing&utm_campaign=marketplace)
- Terms: [getprecision.ai/legal/terms](https://getprecision.ai/legal/terms?utm_source=cursormarketplace&utm_medium=listing&utm_campaign=marketplace)
- Support: hello@getprecision.ai

Precision AI OS is a product of Precision AI LLC, Miami, FL 33176.

The mark at `assets/precision.svg` is copied from Precision's square website favicon. A 512×512 PNG is also included at `assets/precision-ai-os-logo-512.png`. MIT covers this distribution wrapper. It does not grant access to the hosted service or a trademark license.

## Local validation

The single endpoint constant is `mcpServers.precision.url` in `mcp.json`. If the public address changes, change that field and regenerate the link:

```sh
python3 scripts/prepare.py
```

This checks documented manifest and config constraints, the committed square icon and a deeplink decode round trip. It performs no network calls.

For a local install, copy this package, including `.cursor-plugin/`, into `~/.cursor/plugins/local/precision-ai-os`. Restart Cursor or run Developer: Reload Window, inspect Customize, and test sign-in with a synthetic operator account. Marketplace installations of the same name can take precedence. Enterprise must allow local imports. A symlink to a directory outside the local plugins folder is not supported.

This Cursor plugin lives in the `cursor-plugin/` directory of https://github.com/precision-ai-os/precision-ai-os-mcp.

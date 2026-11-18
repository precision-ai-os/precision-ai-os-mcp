# Precision AI OS MCP

Set up and run your firm's Precision AI agents, skills and routines from any MCP client.

AI agents for CPA and accounting firms and other professional service firms. Agents prepare the work. Sends wait for your team's approval by default.

This repository packages the remote Precision AI OS MCP server for Gemini CLI, Cursor, and Kiro. Sign in with your firm's Precision operator account through Clerk. The shared server address is `https://mcp.getprecision.ai/v1/mcp`. The server resolves your authorized firm after sign-in. No firm ID, API key, bearer header or environment variable belongs in this repository.

Operators can create and manage agents, skills, routines, websites, firm logins, settings and Rules; add Agent OS notes and clients; and check routines, jobs and connected apps. Use ask_agent to give an agent work. Approving work, connecting a person's inbox or apps, and signing in to websites stay with people in the app. The MCP never sends anything itself. Every write is logged under the signed-in person's name.

Reading existing working content (tasks, chats, notes and the client list) is off unless the firm's deployment allows it. Access is limited to people with the operator role in the relevant firm. If you operate more than one firm, choose which firm the shared address uses in the app under Setup → Precision MCP.

## Gemini CLI

Install the extension from this repository:

```sh
gemini extensions install https://github.com/precision-ai-os/precision-ai-os-mcp
```

Restart Gemini CLI. If sign-in does not start automatically, run `/mcp auth precision`. When the CLI opens your browser, sign in with your firm's Precision account and allow access.

The extension manifest is `gemini-extension.json` at the repository root, with context in `GEMINI.md`.

## Cursor

The Cursor plugin lives in the `cursor-plugin/` directory. After it is listed on the Cursor Marketplace, open Cursor Customize, find Precision AI OS, and install it. Until then, copy `cursor-plugin/` (including `.cursor-plugin/`) into `~/.cursor/plugins/local/precision-ai-os`, reload Cursor, and complete OAuth as the firm's operator.

You can also merge this server entry into `~/.cursor/mcp.json` and use the Connect prompt:

```json
{
  "mcpServers": {
    "precision": {
      "url": "https://mcp.getprecision.ai/v1/mcp"
    }
  }
}
```

See `cursor-plugin/README.md` and `cursor-plugin/ADD-TO-CURSOR.md`.

## Kiro

The Kiro Power lives in the `kiro-power/` directory. In Kiro, open the Powers panel, choose Add Custom Power, then Import power from GitHub. Paste https://github.com/precision-ai-os/precision-ai-os-mcp and select the `kiro-power` directory if Kiro asks for a path. Complete OAuth as the firm's operator when Kiro prompts for sign-in.

If sign-in does not start from the Power, add the same shared address in Kiro's MCP settings and use the Connect or authentication prompt. See `kiro-power/README.md`.

## Product and legal

- Product and setup: [getprecision.ai/mcp](https://getprecision.ai/mcp?utm_source=github&utm_medium=repo&utm_campaign=marketplace)
- Tool reference: [getprecision.ai/mcp/tools](https://getprecision.ai/mcp/tools?utm_source=github&utm_medium=repo&utm_campaign=marketplace)
- Privacy: [getprecision.ai/legal/privacy](https://getprecision.ai/legal/privacy?utm_source=github&utm_medium=repo&utm_campaign=marketplace)
- Terms: [getprecision.ai/legal/terms](https://getprecision.ai/legal/terms?utm_source=github&utm_medium=repo&utm_campaign=marketplace)
- Support: hello@getprecision.ai

Precision AI OS is a product of Precision AI LLC, Miami, FL 33176.

The mark in `assets/precision.svg` is copied from Precision's square website favicon. MIT covers this distribution wrapper. It does not grant access to the hosted service or a trademark license.

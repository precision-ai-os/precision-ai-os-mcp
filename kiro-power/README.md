# Precision AI OS for Kiro

Set up and run your firm's Precision AI agents, skills and routines from any MCP client.

AI agents for CPA and accounting firms and other professional service firms. Agents prepare the work. Sends wait for your team's approval by default.

This Kiro Power connects the remote Precision AI OS MCP server over Streamable HTTP. Sign in with your firm's Precision operator account through Clerk. The shared server address is `https://mcp.getprecision.ai/v1/mcp`. The server resolves your authorized firm after sign-in. No firm ID, API key, bearer header or environment variable belongs in this package.

Operators can create and manage agents, skills, routines, websites, firm logins, settings and Rules; add Agent OS notes and clients; and check routines, jobs and connected apps. Use ask_agent to give an agent work. Approving work, connecting a person's inbox or apps, and signing in to websites stay with people in the app. The MCP never sends anything itself. Every write is logged under the signed-in person's name.

Reading existing working content (tasks, chats, notes and the client list) is off unless the firm's deployment allows it.

## Install and sign in

Install it in Kiro:

1. Open the Powers panel.
2. Choose Add Custom Power, then Import power from GitHub.
3. Paste https://github.com/precision-ai-os/precision-ai-os-mcp and select the `kiro-power` directory if Kiro asks for a path.
4. Install, then complete OAuth as the firm's operator when Kiro prompts for sign-in.

You can also install from a local folder: Add Custom Power, then Import power from a folder, and select this `kiro-power` directory.

If sign-in does not start from the Power, add the same shared address in Kiro's MCP settings and use the Connect or authentication prompt. Do not paste a token into this repository or substitute another firm's address.

If you operate more than one firm, choose which firm the shared address uses in the app under Setup → Precision MCP.

## Product and legal

- Product and setup: [getprecision.ai/mcp](https://getprecision.ai/mcp?utm_source=kiro&utm_medium=listing&utm_campaign=marketplace)
- Tool reference: [getprecision.ai/mcp/tools](https://getprecision.ai/mcp/tools?utm_source=kiro&utm_medium=listing&utm_campaign=marketplace)
- Privacy: [getprecision.ai/legal/privacy](https://getprecision.ai/legal/privacy?utm_source=kiro&utm_medium=listing&utm_campaign=marketplace)
- Terms: [getprecision.ai/legal/terms](https://getprecision.ai/legal/terms?utm_source=kiro&utm_medium=listing&utm_campaign=marketplace)
- Support: hello@getprecision.ai

Precision AI OS is a product of Precision AI LLC, Miami, FL 33176.

The mark at `assets/precision.svg` is copied from Precision's square website favicon. A 512×512 PNG is also included at `assets/precision-ai-os-logo-512.png`. MIT covers this distribution wrapper. It does not grant access to the hosted service or a trademark license.

## Local validation

The official Kiro check is a local install: in the Kiro app, Add Custom Power, Import power from a folder, select this directory, then test sign-in and a tool call with a synthetic operator account.

This Power lives in the `kiro-power/` directory of https://github.com/precision-ai-os/precision-ai-os-mcp.

To request a listing in the Kiro Powers directory, submit the public repository at [kiro.dev/registry/submit](https://kiro.dev/registry/submit/) with the resource type set to Power. That form is the official path. A pull request to `kirodotdev/powers` is not required. This package does not submit itself.

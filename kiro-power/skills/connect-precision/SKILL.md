---
name: connect-precision
description: Connect Kiro to Precision AI OS and help a firm operator set up agents, skills and routines, or give an agent work. Use when the user mentions Precision, firm agents, skills, routines, or the Precision MCP server.
license: MIT
metadata:
  author: Precision AI LLC
  version: 1.0.0
---

# Connect to Precision AI OS

Precision AI OS gives CPA and accounting firms and other professional service firms AI agents and automations that prepare client work, with sends held for the team's approval by default.

This Power connects Kiro to the remote Precision AI OS MCP server at `https://mcp.getprecision.ai/v1/mcp` over Streamable HTTP. Official registry name: `ai.getprecision/precision-ai-os`.

## Prerequisites

- The user has the operator role in the relevant Precision firm.
- The user can sign in with that firm's Precision account. The shared server address alone does not grant access.
- If the user operates more than one firm, they choose which firm the shared address uses in the Precision app under Setup → Precision MCP.

## Sign in

1. After the Power is installed, connect the Precision MCP server if Kiro prompts for it.
2. When the browser opens, sign in with the firm's Precision account and allow access.
3. If sign-in does not start from the Power, ask the user to add the same shared address in Kiro's MCP settings and complete OAuth there. Do not ask the user to paste an API key, bearer token, or a per-firm MCP URL unless they already chose a per-firm address in the app.

## What you can help with

After the user is signed in, you can help them:

- Create and manage agents, skills, routines, websites, firm logins, settings and Rules
- Add, change, rename and archive Agent OS notes, and add clients
- Check routines, jobs, connected apps and website sign-ins as state and counts
- Give one of the firm's agents work with ask_agent

Prefer read-only tools first. For writes, explain what will change and wait for the user's confirmation in the tool prompt.

## What you must not do

- Do not try to approve work, send email or messages, connect a person's inbox or apps, or sign in to websites through the MCP. Those actions stay with people in the Precision app. The MCP never sends anything itself.
- Do not assume you can read existing tasks, chats, notes or the client list. Those reads are off unless the firm's deployment allows them.
- Do not invent firm, client or job data when a tool returns an access or empty result. Say what the tool reported.

Every write is logged under the signed-in person's name, with the client they used.

## Further reading

Setup and access: https://getprecision.ai/mcp?utm_source=kiro&utm_medium=listing&utm_campaign=marketplace
Production tool reference: https://getprecision.ai/mcp/tools?utm_source=kiro&utm_medium=listing&utm_campaign=marketplace
Support: hello@getprecision.ai

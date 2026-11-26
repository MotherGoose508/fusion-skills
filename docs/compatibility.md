# Fusion compatibility and setup

| Route | Fusion-side dependency | Codex-side dependency | Evidence and limitations |
| --- | --- | --- | --- |
| Fusion MCP | Running Fusion plus any bridge or add-in required by the chosen provider | Registered MCP server and callable tools in the session | The development machine has an enabled local MCP entry for Fusion. No listening service or callable Fusion tools were present during the inventory. Provider, version, permissions and all operations await verification. |
| Fusion Python | Autodesk Fusion desktop with Python script support | The skills for generating or adapting scripts, plus access to the script and run results | Fusion desktop registration, a local scripts directory and installed Autodesk Python API definitions were observed on Windows. The smoke script exercises the in-app runtime. macOS setup follows Autodesk documentation and has no project-specific run evidence. |
| Handoff | Fusion needed later to run or open deliverables | Skills alone | Use generated scripts or instructions and clearly record pending CAD execution. |

The local `CodexFusion` script is an Autodesk template with an active-document message. Its presence does not identify the configured MCP provider. A new connector is deferred until a callable existing provider can be evaluated against the relevant cases.

## Configure an existing MCP bridge

1. Get the bridge's launch method and version from the person or provider who installed it. Start Fusion and start or load its Fusion-side integration as documented by that provider.
2. Use `codex mcp list` to inspect registration. If it is missing, register the documented server. For an HTTP bridge use `codex mcp add fusion --url <provider-url>`. For a stdio bridge use `codex mcp add fusion -- <provider-command> [args]`. Use the provider's auth instructions when required.
3. Start a fresh Codex chat, confirm the Fusion tools appear, and run the [read-only setup check](../tests/README.md#fusion-smoke-test). Check write or export capability only in a disposable design and when needed.

Use a supported native Fusion save or archive operation for the relevant design. Linked assemblies may require a shared Fusion project with access to the referenced designs or an archive that includes dependencies. Confirm the recipient can reopen the delivered representation. Compatibility with a connector or platform is established by the observed run and artifact.

- [Codex MCP setup](https://developers.openai.com/codex/mcp)
- [Autodesk Fusion scripts and add-ins](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm)

# Fusion Skills for Codex

Two Codex skills for producing editable Autodesk Fusion parts and assemblies, with engineering checks scaled to the design.

| Skill | Use it for |
| --- | --- |
| [fusion-core](skills/fusion-core/SKILL.md) | Parametric parts, existing designs, focused repairs and manufacturing review |
| [fusion-mechanisms](skills/fusion-mechanisms/SKILL.md) | Moving assemblies, design calculations, clearances and optional FRC context |

## Install the skills

Clone or download this repository through GitHub. Keep both skill folders together. For project-level discovery, copy both directories from `skills/` into `.agents/skills/` at the root of the project where you want to use them. For user-level discovery, use `~/.agents/skills/`. Start a fresh Codex chat and choose `$fusion-core` or `$fusion-mechanisms` explicitly for the first trial. Codex can also select them from their descriptions. [Codex skills documentation](https://developers.openai.com/codex/skills)

## Connect to Fusion

- **Existing MCP bridge.** Use the connector provider's instructions to install and start its Fusion-side integration and register its MCP server with Codex. In the new chat, perform a read-only check on a known design before editing. This repository supplies skills and tests. Connector capabilities are verified separately. See [compatibility and setup](docs/compatibility.md).
- **Fusion Python script.** Install Autodesk Fusion desktop. Run the supplied smoke script using the [test instructions](tests/README.md), then use the same registration and run workflow for task-specific scripts. Running a script may require desktop interaction. See [Autodesk's installation guide](https://help.autodesk.com/view/fusion360/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FHow-to-install-an-ADD-IN-and-Script-in-Fusion-360.html).

Copy and fill the [shared defaults](profiles/default.md) and [project overrides](profiles/project.md). Attach them or point Codex to their paths. For FRC tasks, you can also supply the [team profile](profiles/frc-team.md).

## Test and update

Run the [verification suite](tests/README.md). To contribute, make changes on a branch, run package checks and relevant Fusion cases, and include completed evaluation records in the pull request when they contain no sensitive project data. To update an installation, pull or redownload the repo and replace both skill folders with the same revision. Keep personal profiles outside the installed skill folders.

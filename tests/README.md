# Verification suite

## Package checks

From the repository root run `python -B -m unittest discover -s tests -v` with Python 3.9 or newer. The suite checks package shape, relative links, test files, and smoke script syntax without Autodesk Fusion. These tests establish packaging integrity.

## Fusion smoke test

Open Autodesk Fusion. In the Design workspace select **Utilities → Add-Ins → Scripts and Add-Ins**, select **Scripts**, and use the add control to register the local `tests/fusion/FusionSkillsSmoke` folder. Run **FusionSkillsSmoke**. It creates one unsaved design, measures its parameter-driven extrusion at 5 mm, 8 mm and 5 mm, and closes the disposable document. A PASS dialog and log entry include the Fusion build and measured values. Record a FAIL dialog verbatim if the run fails.

For MCP, independently list the tools surfaced in Codex and invoke a read-only inspection on a known scratch design. Confirm that the reported document matches. Record availability for the operations each case requires. This tests Codex-to-Fusion access while the script tests Fusion's in-app API.

## Skills trials

| Case | Workflow |
| --- | --- |
| [01 · Motor mount](cases/01-motor-mount.md) | Editable part and manufacturing review |
| [02 · Rack slide](cases/02-rack-slide.md) | Mechanism, calculations, motion and fit |
| [03 · Larger assembly](cases/03-assembly-integration.md) | Integration, preservation and clashes |
| [04 · Focused repair](cases/04-focused-repair.md) | Local edit, script fallback and truthful blocked state |
| [05 · FRC routing](cases/05-frc-routing.md) | Scope and official rules |

1. Start a fresh chat for each run with the case's exact prompt and a fresh copy of any required fixture. In the skills condition, make the skills discoverable and record which skill Codex selects before judging the result. If testing explicit invocation, record that separately.
2. For a baseline, use a neutral workspace and profile where both skills are unavailable. Keep other settings, starting state, model, permissions and tool capabilities as consistent as possible. Avoid giving either condition the grading criteria.
3. Evaluate the native artifact in Fusion and collect evidence against each requirement. Use the [evaluation record](evaluation-record.md) per run. Compare outcomes before comparing time, calls, retries and available credits.

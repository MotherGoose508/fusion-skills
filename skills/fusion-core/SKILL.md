---
name: fusion-core
description: Create, inspect, edit, or review Autodesk Fusion designs, especially parametric parts and focused changes to existing models. Use for requests that need an editable Fusion artifact, a Fusion API script, or evidence from geometry, parameters, timeline, fit, or manufacturing checks.
---

# Fusion core

1. Identify the expected native deliverable, design intent, existing assets, critical interfaces, and manufacturing process. Use reversible assumptions where reasonable. Ask if a missing interface, load case, or process would materially change the design. Apply [project profiles](references/profiles.md) when provided.
2. Establish the available Fusion connection using [connection and evidence](references/connection.md). For an existing model, verify document identity and target component or occurrence before editing. Record a small baseline of unrelated items that must survive and use an available version, copy, or checkpoint before structural edits.
3. Set the modelling plan and highest-impact checks before building. For parametric parts and repairs, use [modelling and review](references/modelling.md). For moving mechanisms or assembly integration, load [fusion-mechanisms](../fusion-mechanisms/SKILL.md) if it is not already loaded.
4. Build or edit in coherent batches, checking each batch when the next one depends on it. On failure, inspect the tool error and resulting model state before an informed retry. Change route if the failure persists or the required capability is unavailable. Avoid rerunning a partial write blindly.
5. Check the identified requirements on the actual artifact when possible. Verify final dimensions, feature health and the effect of at least one meaningful parameter edit when editability is central. Restore nominal values and confirm the final state after the check.
6. Deliver the editable Fusion design and a concise report by default. Identify the document or archive, requirements checked and evidence, calculated estimates with units and inputs, assumptions, and remaining CAD or physical checks. Provide drawings, BOMs or manufacturing exports when requested. If blocked from producing a native model, label any script or modelling instructions as a handoff and report what must run in Fusion.

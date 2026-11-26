---
name: fusion-mechanisms
description: Design, integrate, or review moving mechanisms and multi-component assemblies in Autodesk Fusion. Use for joints, travel limits, packaging, interference, power transmission, and optional FRC mechanism work. Use fusion-core for ordinary single-part modelling and timeline repairs.
---

# Fusion mechanisms

Start with the connection, checkpoint, and delivery guidance in [Fusion core](../fusion-core/SKILL.md). Use it as the shared workflow when this skill is selected first.

1. Identify the intended motion, interfaces, operating loads, travel range, surrounding envelope, and fabrication process. Inspect an existing assembly for the target occurrence path, hierarchy, external links, grounded references, and relevant joints. Record a baseline before changes.
2. Work through [mechanism checks](references/mechanism-checks.md) for the calculations and failure modes relevant to the brief. Resolve choices such as stroke, reduction, torque or likely binding before detailed modelling. For competition-bound FRC tasks, use [FRC context](references/frc.md).
3. Model the mechanism as meaningful components. Locate it with stable assembly datums. Ground the base or use the existing frame reference. Use the required joint axes, limits and degrees of freedom. Keep integration changes local to the mounting interface unless the wider assembly needs modification.
4. Verify the interfaces and relevant joint states. Record the poses and pairs checked, reported clash or minimum gap, and intentional contacts. For larger assemblies, review the mechanism subassembly and nearby interfaces first. Expand the check where movement or changed geometry can affect other subsystems. Check the original assembly baseline after the edit.
5. Report the editable assembly, checks, assumptions, and remaining work using the shared core conventions. Identify the operating load case behind calculated results and distinguish nominal motion, tolerance-dependent clearance, and behaviour that needs physical validation.

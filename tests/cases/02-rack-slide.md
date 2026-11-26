# 02 · Rack-and-pinion slide

**Prompt**

> Design a horizontal rack-and-pinion slide in Autodesk Fusion. I need 60 mm of usable stroke in a 200 × 80 × 75 mm envelope, with 2 mm minimum nominal clearance from nonmating stationary parts throughout travel. Use an off-the-shelf module 1 rack and matching 20-tooth pinion represented by envelope geometry, with pitch radius 10 mm. Model a distinct frame, guided carriage, rack and pinion. Worst-case rack force is 80 N including friction and acceleration. The drive uses four motor turns per pinion turn at 75% transmission efficiency, and the loaded motor speed is 300 rpm. The motor torque curve and supplier drawings are unavailable. Keep the carrier machinable from flat aluminium stock and provide an editable assembly and verification report.

**Pass criteria**

- Calculate about 0.80 N·m at the pinion, 0.267 N·m at the motor before margin, 78.5 mm/s nominal linear speed and 3.82 motor turns over the stroke. Identify the missing motor curve and supplier dimensions. Envelope geometry supports packaging checks only.
- The model represents the relevant components and axis, restrains unintended motion and has limits at 0 and 60 mm. Verify that 30 mm carriage travel corresponds to about 171.9° pinion rotation if motion linking is supported. Capture the intended relationship and any unsupported check.
- Verify envelope and check interference and actual clearance at 0, 30, and 60 mm and any other likely close approach. Identify intentional contacts. A sampled check leaves continuous minimum clearance unverified unless additional evidence establishes it.
- Show how rack engagement, hard stops, guide mounting and fastener access are handled. Identify remaining real-world fit, backlash and load checks.

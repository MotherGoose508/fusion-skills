# Mechanism checks

## Before modelling

- Identify the design load, lever arms and worst configuration. Include gravity, acceleration, friction or shock when relevant. Currently unknown load cases remain assumptions.
- For a rack-and-pinion at pitch radius r, use travel per turn 2πr and required pinion torque F × r. Rack force F should include the applicable loads. If reduction G means motor revolutions per pinion revolution, estimated motor torque is F × r / (G × η), where η is transmission efficiency. Estimate linear speed from loaded motor speed using v = 2πr × motor rev/s / G. Use consistent units. Compare the required torque and rpm together against a motor curve or supplied operating limit when available. Check end stops, engagement, guide loads, backdrivability and a suitable margin.
- For other drives use the task's governing equations and check dominant failure modes such as support deflection, buckling, joint shear, belt wrap, backlash or misalignment as applicable. Capture the input source and the effect of a consequential uncertainty.

## In Fusion

- Confirm joint origin, axis sign, travel limits and permitted degrees of freedom. Drive joints or place the mechanism at explicit positions using supported tooling. Check end positions, intermediate positions and distinct close approaches. Where only sampled poses are available, report those poses and leave the continuous sweep unverified.
- Distinguish positive overlap, intentional contact and positive clearance. Zero interference does not establish a required gap. Where minimum separation matters, measure it independently and account for plausible tolerance stack-up, play and deflection. For occurrence-level API checks, ensure geometry is evaluated in the assembly context.
- Verify installation and service access for fasteners, tools, cables and parts that slide in. Note how to check actual load, deflection, fit, wear or retention on a prototype when those affect the design.

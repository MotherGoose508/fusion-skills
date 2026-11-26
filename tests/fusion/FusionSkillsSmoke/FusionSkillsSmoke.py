"""Run inside Autodesk Fusion using Scripts and Add-Ins."""

import math
import traceback

import adsk.core
import adsk.fusion


def check_geometry(design, feature, expected_mm):
    if not design.computeAll():
        raise RuntimeError("Fusion could not recompute the design.")
    if feature.healthState != adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:
        raise RuntimeError(f"{feature.name}: {feature.errorOrWarningMessage}")
    if feature.bodies.count != 1 or not feature.bodies.item(0).isSolid:
        raise RuntimeError("Expected one solid body from the extrusion.")
    bounds = feature.bodies.item(0).boundingBox
    dimensions_mm = (
        10 * (bounds.maxPoint.x - bounds.minPoint.x),
        10 * (bounds.maxPoint.y - bounds.minPoint.y),
        10 * (bounds.maxPoint.z - bounds.minPoint.z),
    )
    expected = (20, 10, expected_mm)
    if any(
        not math.isclose(actual, target, abs_tol=0.01)
        for actual, target in zip(dimensions_mm, expected)
    ):
        raise RuntimeError(f"Expected {expected} mm, measured {dimensions_mm} mm.")
    return f"{dimensions_mm[2]:.2f} mm"


def exercise_model(app):
    document = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    try:
        design = adsk.fusion.Design.cast(
            document.products.itemByProductType("DesignProductType")
        )
        if design is None:
            raise RuntimeError("The temporary document has no Fusion Design product.")
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType

        value = adsk.core.ValueInput.createByString
        height = design.userParameters.add("smokeHeight", value("5 mm"), "mm", "")
        root = design.rootComponent
        sketch = root.sketches.add(root.xYConstructionPlane)
        sketch.name = "Smoke test footprint"
        point = adsk.core.Point3D.create
        sketch.sketchCurves.sketchLines.addTwoPointRectangle(point(0, 0, 0), point(2, 1, 0))
        extrudes = root.features.extrudeFeatures
        extrusion_input = extrudes.createInput(
            sketch.profiles.item(0), adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        )
        distance = adsk.fusion.DistanceExtentDefinition.create(value(height.name))
        if not extrusion_input.setOneSideExtent(
            distance, adsk.fusion.ExtentDirections.PositiveExtentDirection
        ):
            raise RuntimeError("Unable to bind the extrusion to smokeHeight.")
        feature = extrudes.add(extrusion_input)
        feature.name = "Parameter-driven extrusion"

        nominal = height.expression
        initial = check_geometry(design, feature, 5)
        height.expression = "8 mm"
        resized = check_geometry(design, feature, 8)
        height.expression = nominal
        restored = check_geometry(design, feature, 5)
        return f"Height measured at nominal, edited and restored: {initial} → {resized} → {restored}."
    finally:
        if not document.close(False):
            raise RuntimeError("Could not close the disposable smoke test document.")


def run(_context):
    app = adsk.core.Application.get()
    try:
        outcome = f"PASS — Fusion {app.version}\n{exercise_model(app)}"
    except Exception:
        outcome = f"FAIL — Fusion {app.version}\n{traceback.format_exc()}"
    app.log(outcome)
    app.userInterface.messageBox(outcome, "Fusion Skills smoke test")

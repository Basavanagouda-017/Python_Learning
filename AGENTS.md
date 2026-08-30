# AGENTS.md

## Purpose

This repository is intended for Python work involving mouse-wheel input, scrolling behavior, or pointer-event handling. Keep agent work focused on event semantics, cross-platform compatibility, and verifiable behavior.

## Working conventions

- Prefer clear, device-agnostic abstractions for wheel events instead of hard-coded assumptions about a single platform.
- Treat mouse-wheel input as a delta-based signal, not as a direct pixel count. Normalize values before using them in logic.
- Distinguish vertical and horizontal wheel movement; do not assume both axes behave identically.
- Respect OS/browser/device settings such as scroll inversion and acceleration when implementing user-visible behavior.
- Favor small, testable functions for event translation, thresholding, and scroll normalization.

## Coding guidelines

- When handling wheel events, define the expected units explicitly: raw delta, cumulative ticks, or normalized scroll steps.
- Validate edge cases: zero movement, high-frequency events, repeated wheel bursts, and hardware-specific delta quirks.
- Keep UI and business logic separate; the event layer should not embed rendering or application state mutations directly.
- Use descriptive names like `vertical_delta`, `scroll_steps`, `wheel_handler`, or `normalize_wheel_delta` instead of ambiguous generic names.
- Prefer explicit thresholds and clamping over magical numbers.

## Testing expectations

- Add focused tests for wheel normalization, sign handling, threshold logic, and axis selection.
- Verify behavior for both positive and negative deltas, including near-zero values.
- If there is UI code, test event wiring and callback behavior without depending on a specific mouse driver.
- Prefer deterministic tests over timing-based or hardware-sensitive assertions.

## Build and validation

When project tooling exists, use the smallest relevant command:

- Python project validation: `python -m pytest`
- Syntax check: `python -m compileall .`
- Prefer local, targeted checks over broad suites when the scope is small.

## Avoid

- Assuming wheel movement always equals one scroll step.
- Mixing raw OS event data into unrelated business logic.
- Hard-coding invert logic or axis mapping without a clear, documented reason.
- Adding device-specific branches unless the code path is explicitly required.

## When making changes

- Explain the wheel semantics at the boundary where events are accepted.
- Document any assumptions about delta direction, step size, or platform behavior.
- Keep fixes minimal and aligned to the root cause rather than layering workaround logic.

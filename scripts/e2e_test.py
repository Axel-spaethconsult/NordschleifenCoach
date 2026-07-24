"""
End-to-end test for the ACC telemetry pipeline.
"""

from nordschleifen_coach.application.coaching.driving_state_detector import (
    DrivingStateDetector,
)
from nordschleifen_coach.application.telemetry.telemetry_history import (
    TelemetryHistory,
)
from nordschleifen_coach.infrastructure.acc.telemetry_source import (
    AccTelemetrySource,
)


def main() -> None:
    source = AccTelemetrySource()
    history = TelemetryHistory()
    detector = DrivingStateDetector()

    try:
        frame = source.read()

        if frame is None:
            print("ACC not connected.")
            return

        history.append(frame)

        state = detector.detect(history)

        print("=== Vehicle ===")
        print(f"Speed:        {frame.vehicle_state.speed:.1f} km/h")
        print(f"RPM:          {frame.vehicle_state.rpm}")
        print(f"Fuel:         {frame.vehicle_state.fuel:.1f} l")

        print()

        print("=== Driver ===")
        print(f"Throttle:     {frame.driver_inputs.throttle:.2f}")
        print(f"Brake:        {frame.driver_inputs.brake:.2f}")
        print(f"Steering:     {frame.driver_inputs.steering:.2f}")
        print(f"Gear:         {frame.driver_inputs.gear}")

        print()

        print("=== Session ===")
        print(f"Lap:          {frame.session_state.lap_number}")
        print(f"Lap time:     {frame.session_state.lap_time:.3f}")
        print(f"Best lap:     {frame.session_state.best_lap_time:.3f}")

        print()

        print("=== Environment ===")
        print(
            f"Air temp:     {frame.environment_state.air_temperature:.1f} °C"
        )
        print(
            f"Track temp:   {frame.environment_state.track_temperature:.1f} °C"
        )
        print(f"Track grip:   {frame.environment_state.track_grip}")
        print(f"Rain:         {frame.environment_state.rain_intensity}")

        print()

        print("=== Driving ===")
        print(f"State:        {state.name}")

    finally:
        source.close()


if __name__ == "__main__":
    main()
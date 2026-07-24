"""
End-to-end test for the driving pipeline.
"""

from time import sleep

from nordschleifen_coach.application.coaching.coach_engine import (
    CoachEngine,
)
from nordschleifen_coach.application.coaching.driving_event import (
    DrivingEvent,
)
from nordschleifen_coach.application.coaching.driving_event_detector import (
    DrivingEventDetector,
)
from nordschleifen_coach.application.coaching.driving_state import (
    DrivingState,
)
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

    state_detector = DrivingStateDetector()
    event_detector = DrivingEventDetector()
    coach = CoachEngine()

    last_state = DrivingState.UNKNOWN

    try:
        print("Reading telemetry... Press Ctrl+C to stop.\n")

        while True:
            frame = source.read()

            if frame is None:
                print("ACC not connected.")
                sleep(1)
                continue

            history.append(frame)

            state = state_detector.detect(history)
            event = event_detector.detect(state)

            feedback = coach.evaluate(
                state=state,
                event=event,
                history=history,
            )

            if state != last_state or event != DrivingEvent.NONE:
                print("-" * 60)
                print(f"Speed:      {frame.vehicle_state.speed:6.1f} km/h")
                print(f"Throttle:   {frame.driver_inputs.throttle:6.2f}")
                print(f"Brake:      {frame.driver_inputs.brake:6.2f}")
                print(f"Steering:   {frame.driver_inputs.steering:6.2f}")
                print(f"Gear:       {frame.driver_inputs.gear}")
                print()
                print(f"State:      {state.name}")
                print(f"Event:      {event.name}")

                if feedback is not None:
                    print(f"Coach:      {feedback}")

            last_state = state

            sleep(0.02)

    except KeyboardInterrupt:
        print("\nStopping E2E test...")

    finally:
        source.close()


if __name__ == "__main__":
    main()
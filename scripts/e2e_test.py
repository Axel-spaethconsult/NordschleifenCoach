from nordschleifen_coach.infrastructure.acc.shared_memory.reader import (
    AccSharedMemoryReader,
)
from nordschleifen_coach.infrastructure.acc.mapper.telemetry_mapper import (
    TelemetryMapper,
)
from nordschleifen_coach.infrastructure.acc.parser.telemetry_parser import (
    TelemetryParser,
)

def main():
 
    reader = AccSharedMemoryReader()
    parser = TelemetryParser()
    mapper = TelemetryMapper()

    try:
        raw = reader.read()
        if raw is None:
            print("ACC nicht verbunden.")
            return

        dto = parser.parse(raw)
        frame = mapper.map(dto)

        print(f"Speed: {frame.vehicle_state.speed:.1f} km/h")
        print(f"Throttle: {frame.driver_inputs.throttle:.2f}")

        print(f"Lap: {frame.session_state.lap_number}")
        print(f"Lap time: {frame.session_state.lap_time:.3f}")
        print(f"Best lap: {frame.session_state.best_lap_time:.3f}")

        print(f"Air temp: {frame.environment_state.air_temperature:.1f} °C")
        print(f"Track temp: {frame.environment_state.track_temperature:.1f} °C")
        print(f"Track grip: {frame.environment_state.track_grip}")
        print(f"Rain: {frame.environment_state.rain_intensity}")

    finally:
        reader.close()

if __name__ == "__main__":
    main()
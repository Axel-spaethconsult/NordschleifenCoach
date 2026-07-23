import time

from pyaccsharedmemory import accSharedMemory


def main() -> None:
    asm = accSharedMemory()

    try:
        while True:
            sm = asm.read_shared_memory()

            if sm is None:
                print("Waiting for ACC...")
                time.sleep(1)
                continue

            # Bildschirm leeren (Windows)
            print("\033[2J\033[H", end="")

            print("=" * 40)
            print("Nordschleifen Coach - Live Monitor")
            print("=" * 40)
            print()

            print(f"Track: {sm.Static.track}")
            print(f"Car:   {sm.Static.car_model}")
            print()

            print(f"Speed:      {sm.Physics.speed_kmh:7.1f} km/h")
            print(f"RPM:        {sm.Physics.rpm:7}")
            print(f"Gear:       {sm.Physics.gear:7}")
            print(f"Throttle:   {sm.Physics.gas * 100:6.1f} %")
            print(f"Brake:      {sm.Physics.brake * 100:6.1f} %")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopping monitor...")

    finally:
        asm.close()


if __name__ == "__main__":
    main()

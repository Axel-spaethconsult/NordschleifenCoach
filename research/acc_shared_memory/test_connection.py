from pyaccsharedmemory import accSharedMemory


def main() -> None:
    asm = accSharedMemory()

    try:
        sm = asm.read_shared_memory()

        if sm is None:
            print("ACC Shared Memory not available.")
            print("Start ACC and load into a session.")
            return

        print("Connected to ACC!")
        print()

        print("=== Physics ===")
        print(f"Speed:    {sm.Physics.speed_kmh:.1f} km/h")
        print(f"RPM:      {sm.Physics.rpm}")
        print(f"Gear:     {sm.Physics.gear}")
        print(f"Throttle: {sm.Physics.gas:.2f}")
        print(f"Brake:    {sm.Physics.brake:.2f}")

        print()
        print("=== Graphics ===")
        print(f"Lap:      {sm.Graphics.completed_lap}")

        print()
        print("=== Static ===")
        print(f"Track:    {sm.Static.track}")
        print(f"Car:      {sm.Static.car_model}")

    finally:
        asm.close()


if __name__ == "__main__":
    main()
    
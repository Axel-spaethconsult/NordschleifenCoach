from pyaccsharedmemory import accSharedMemory


def dump_section(name: str, section) -> None:
    print(f"\n{name}")
    print("-" * len(name))

    for attribute in sorted(dir(section)):
        if attribute.startswith("_"):
            continue

        try:
            value = getattr(section, attribute)
            print(f"{attribute:30} {type(value).__name__:12} {value}")
        except Exception as exc:
            print(f"{attribute:30} ERROR: {exc}")


def main() -> None:
    asm = accSharedMemory()

    try:
        sm = asm.read_shared_memory()

        if sm is None:
            print("ACC not available.")
            return

        dump_section("Physics", sm.Physics)
        dump_section("Graphics", sm.Graphics)
        dump_section("Static", sm.Static)

    finally:
        asm.close()


if __name__ == "__main__":
    main()
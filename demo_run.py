"""
Demo script to verify segment-geospatial installation and basic functionality.
"""

import samgeo


def main():
    print("=" * 60)
    print("segment-geospatial Demo")
    print("=" * 60)
    print()

    # Display version
    print(f"✓ segment-geospatial version: {samgeo.__version__}")
    print()

    # Check available modules
    print("Available modules:")
    available_modules = []

    # Check SamGeo (SAM 1)
    try:
        from samgeo import SamGeo
        available_modules.append("✓ SamGeo (Segment Anything Model)")
        print("  ✓ SamGeo (Segment Anything Model)")
    except ImportError as e:
        print(f"  ✗ SamGeo: {e}")

    # Check SamGeo2 (SAM 2)
    try:
        from samgeo import SamGeo2
        available_modules.append("✓ SamGeo2 (SAM 2)")
        print("  ✓ SamGeo2 (SAM 2)")
    except ImportError as e:
        print(f"  ✗ SamGeo2: {e}")

    # Check common utilities
    try:
        from samgeo import common
        available_modules.append("✓ Common utilities")
        print("  ✓ Common utilities")
    except ImportError as e:
        print(f"  ✗ Common utilities: {e}")

    print()
    print("=" * 60)
    print("Summary:")
    print("=" * 60)
    print(f"Core package installed: ✓")
    print(f"Working modules: {len(available_modules)}")
    print()
    print("To use additional features:")
    print("  - SAM 2: pip install segment-geospatial[samgeo2]")
    print("  - Fast SAM: pip install segment-geospatial[fast]")
    print("  - Text prompts: pip install segment-geospatial[text]")
    print("  - All features: pip install segment-geospatial[all]")
    print()
    print("For examples, check the docs/examples/ directory!")
    print("=" * 60)


if __name__ == "__main__":
    main()

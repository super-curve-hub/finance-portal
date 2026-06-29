#!/usr/bin/env python3
"""
SUPER CURVE TERMINAL
Build System v3.0.0-alpha
"""

from pathlib import Path
import sys
import traceback

# プロジェクトルート
ROOT = Path(__file__).resolve().parent.parent

# core を import できるようにする
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def banner():
    print("=" * 60)
    print(" SUPER CURVE TERMINAL BUILD SYSTEM")
    print("=" * 60)
    print(f"Project : {ROOT}")
    print("Version : v3.0.0-alpha")
    print()


def main():

    banner()

    print("Loading Builder Engine...")

    try:
        from core.builder import build_site

        print("✓ Builder Engine loaded")
        print()

        build_site()

        print()
        print("=" * 60)
        print("BUILD SUCCESS")
        print("=" * 60)

    except Exception:
        print()
        print("=" * 60)
        print("BUILD FAILED")
        print("=" * 60)
        print()

        traceback.print_exc()

        sys.exit(1)


if __name__ == "__main__":
    main()
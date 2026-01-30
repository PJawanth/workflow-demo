#!/usr/bin/env python3
"""Verify that metrics.py generated the expected output files."""

import os
import sys

OUT_DIR = os.getenv("OUT_DIR", "out")

EXPECTED_FILES = [
    "dora_daily.csv",
    "flow_pr.csv",
    "metrics_snapshot.csv",
    "pipeline_health.csv",
    "dashboard.xlsx",
]


def main():
    missing = []
    for fname in EXPECTED_FILES:
        path = os.path.join(OUT_DIR, fname)
        if not os.path.exists(path):
            missing.append(fname)
        else:
            size = os.path.getsize(path)
            print(f"✓ {fname} ({size} bytes)")

    if missing:
        print(f"\n✗ Missing files: {missing}", file=sys.stderr)
        sys.exit(1)

    print("\nAll expected output files are present.")


if __name__ == "__main__":
    main()

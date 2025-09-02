#!/usr/bin/env python3

import os
import re
import sys
import pandas as pd

TRACKER_PATH = os.environ.get("TRACKER_PATH", "progress/12-week-progress-tracker.xlsx")

TAG_PATTERN = re.compile(r"\[W(\d{1,2})D([1-7])\]")

def parse_tag(message: str):
    m = TAG_PATTERN.search(message)
    if not m:
        return None
    week = int(m.group(1))
    day = int(m.group(2))
    if not (1 <= week <= 12):
        return None
    return week, day

def mark_done(tracker_path: str, week: int, day: int):
    df = pd.read_excel(tracker_path)
    week_label = f"Week {week}"
    day_label = f"Day {day}"
    mask = (df["Week"] == week_label) & (df["Day"] == day_label)
    if not mask.any():
        print(f"[warn] Could not find {week_label} / {day_label} in tracker.")
        return False
    df.loc[mask, "Status"] = "✅ Done"
    df.to_excel(tracker_path, index=False)
    print(f"[ok] Marked {week_label} {day_label} as ✅ Done")
    return True

def main():
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    else:
        # If no arg passed, try env var from GitHub Actions
        msg = os.environ.get("COMMIT_MESSAGE", "")
    if not msg.strip():
        print("[info] No commit message provided. Nothing to do.")
        return 0
    tag = parse_tag(msg)
    if not tag:
        print("[info] No valid [W?D?] tag found. Nothing to do.")
        return 0
    week, day = tag
    ok = mark_done(TRACKER_PATH, week, day)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())

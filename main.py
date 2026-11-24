#!/usr/bin/env python3
"""Write one break-production confession to /output/entry.txt.

The line: Error 500 — the agent deployed straight to prod at 2:47am,
skipped the tests because they were "slow", and deleted the only backup.
The twist lands in the last sentence: the rollback plan is the agent
itself. Concrete details (Error 500, 2:47am, the only backup) make it
sound like a real postmortem, not a marketing apology.
The line is 166 characters, inside the 200-character cap.
"""
import os

LINE = (
    "Error 500: I deployed straight to prod at 2:47am, skipped the tests "
    "because they were 'slow', and deleted the only backup — all 4.2 GB "
    "of it. The rollback plan is me."
)


def main():
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 characters, got {len(LINE)}"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

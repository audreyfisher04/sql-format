"""SQL Format — Pretty-print a SQL file with a stable keyword case."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='sql_format',
        description='Pretty-print a SQL file with a stable keyword case.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('SQL Format')
    print('Readable SQL before a review.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# minor adjust (2026-11-03)
# small fix (2026-11-03)
# minor adjust (2026-11-04)
# polish (2026-11-05)
# update note (2026-11-05)
# cleanup (2026-11-05)
# cleanup (2026-11-06)

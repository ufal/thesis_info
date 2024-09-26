#!/usr/bin/env python3
import argparse
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="thesis.md", type=str, help="Input source")
    parser.add_argument("--start", default=r"^### Machine Translation.*$", type=str, help="Line to start on")
    args = parser.parse_args()

    print("Instructions\t- the badges belong to the section/area immediately above")
    print("\t- the details are in Markdown format")
    print("\t- you can add/change entries freely")
    print("\t- if you would like to remove or reorder entries, create a comment please")
    print()

    print("Section\tArea\tBadge\tBadge Target\tDetails")
    with open(args.input, mode="r") as input_file:
        started = False
        for line in input_file:
            line = line.rstrip("\r\n")
            if re.match(args.start, line):
                started = True
            if not started:
                continue
            if match := re.match(r"^### ([^[]*)(:? *\[badge:([^]]*)]\(([^)]*)\))?$", line):
                print(f"{match.group(1)}")
                if match.group(3) is not None and match.group(4) is not None:
                    print(f"\t\t\t{match.group(3) or ''}\t{match.group(4) or ''}")
            elif match := re.match("^- (.*)$", line):
                print(f"\t{match.group(1)}")
            elif match := re.match("^  \[badge:([^]]*)]\(([^)]*)\)$", line):
                print(f"\t\t{match.group(1)}\t{match.group(2)}")
            elif match := re.match("^\s*$", line):
                pass
            elif match := re.match("^  (.*$)$", line):
                print(f"\t\t\t\t{match.group(1)}")
            else:
                raise ValueError(f"Unrecognized line: {line}")

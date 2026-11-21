import argparse
import json
from pathlib import Path


def solve(data):
    length = data["length"]
    if length < 2:
        raise ValueError("Use at least two notes per phrase")
    groups = {}
    for song, notes in data["songs"].items():
        for start in range(len(notes) - length + 1):
            phrase = notes[start:start + length]
            intervals = tuple(b - a for a, b in zip(phrase, phrase[1:]))
            groups.setdefault(intervals, []).append({"song": song, "offset": start})
    return {"matches": [{"intervals": key, "hits": hits} for key, hits in sorted(groups.items())
                        if len({hit["song"] for hit in hits}) > 1]}

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find repeated melodic phrases across songs even when the starting pitch changes.')
    parser.add_argument("input", nargs="?", type=Path, default=Path(__file__).with_name("sample.json"))
    args = parser.parse_args()
    print(json.dumps(solve(json.loads(args.input.read_text())), indent=2))

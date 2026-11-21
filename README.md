# MotifMiner

Find repeated melodic phrases across songs even when the starting pitch changes.

Use integer pitches and a phrase length of at least two. Hits use zero-based note offsets. Matching compares successive pitch differences and ignores timing.

## Run locally

From this folder with Python 3.8 or newer, run the included synthetic example and tests. Only the standard library is required.

```bash
python3 app.py
python3 -m unittest -v
```

Copy sample.json and edit its values, then run `python3 app.py your-input.json`.

## Sample output

```json
{
  "matches": [
    {
      "intervals": [
        2,
        3,
        -1
      ],
      "hits": [
        {
          "song": "dawn",
          "offset": 0
        },
        {
          "song": "dusk",
          "offset": 0
        }
      ]
    }
  ]
}
```

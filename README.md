# SOC Log Analyzer

**A Python CLI exercise for log statistics and indicator-candidate extraction.**

The tool reads one local text log, counts lines/words/characters and literal
`INFO`, `WARNING` and `ERROR` occurrences, finds email/IPv4-shaped strings,
and optionally saves a plain-text report. It is not a SIEM or attack detector.

## Run

Python 3 and its standard library are sufficient; no pip packages are required.

```sh
git clone https://github.com/Yuvraj-26-k/soc-log-analyzer.git
cd soc-log-analyzer
python main.py
```

At the prompt, enter `server.log` to use the tracked example. The program
changes to its script directory; relative input/output paths resolve there.
If saving a report, choose a new filename such as `demo-report.txt` rather
than overwriting the tracked `report.txt` or another input file.

## Current limitations

The whole file is read into memory. Regex matches are candidates, not validated
email/IP identities; duplicates count more than once. Severity words are
substring counts, not structured event parsing. The saved report contains counts
rather than a verified incident assessment. Output files can be overwritten and
error handling is incomplete. Never process private/client logs for a public demo.

## Example and structure

![Historical terminal demonstration of log statistics](log%20analyzer.png)

This existing screenshot demonstrates the interface, not a newly validated run.
The repository contains `main.py`, `server.log`, `report.txt` and screenshots.
Sample data/report files are educational examples, not client evidence.

There is no first-party test suite. Priorities are validated indicators,
streaming input, create-only JSON/CSV reports, fewer delays and deterministic
tests. This update documents the current script; it does not migrate or
consolidate it with another repository.

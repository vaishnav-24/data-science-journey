# Expense Tracker (CLI)

## Problem
Manager keeps expenses in a messy text file — inconsistent categories, missing values, bad amounts. This script turns it into totals per category.

## How to run
python expense_tracker.py <filename.csv>

## Input format
CSV with header: category,amount

## What it handles
- Empty/malformed lines
- Non-numeric amounts
- Negative amounts (flagged, excluded from totals)
- Missing category
- Case/whitespace differences in category names (e.g. "Food", " food ")

## Known limitations
- Assumes a header row is always present
- Doesn't support more than 2 columns
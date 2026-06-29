# calendar_cli.py
import calendar
import argparse
import datetime
import sys

def highlight_today(text: str) -> str:
    # Adds ANSI bold+underline for today's date (works in many terminals).
    # If terminal doesn't support ANSI codes, they'll be ignored.
    today = datetime.date.today()
    s = text
    day = today.day
    # 'formatmonth' produces right-justified day numbers; find the day's token
    token = f"{day:2d}"
    highlighted = f"\033[1m\033[4m{token}\033[0m"  # bold + underline
    return s.replace(token, highlighted, 1)

def print_month(year: int, month: int, highlight: bool) -> None:
    cal = calendar.TextCalendar(calendar.SUNDAY)
    s = cal.formatmonth(year, month)
    if highlight and year == datetime.date.today().year and month == datetime.date.today().month:
        s = highlight_today(s)
    print(s)

def print_year(year: int, highlight: bool) -> None:
    cal = calendar.TextCalendar(calendar.SUNDAY)
    s = cal.formatyear(year, 2, 1, 1, 3)  # nice compact year layout
    if highlight and year == datetime.date.today().year:
        # naive approach: individually highlight each month's output and re-print
        for month in range(1, 13):
            print_month(year, month, highlight=True)
    else:
        print(s)

def main():
    parser = argparse.ArgumentParser(description="Text Calendar CLI")
    parser.add_argument("--year", "-y", type=int, default=datetime.date.today().year, help="Year (e.g., 2025)")
    parser.add_argument("--month", "-m", type=int, choices=range(1,13), help="Month number 1-12")
    parser.add_argument("--highlight-today", "-t", action="store_true", help="Highlight today's date if visible")
    args = parser.parse_args()

    if args.month:
        print_month(args.year, args.month, args.highlight_today)
    else:
        print_year(args.year, args.highlight_today)

if __name__ == "__main__":
    main()

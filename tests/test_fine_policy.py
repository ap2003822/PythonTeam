from datetime import datetime
from fine_policy import FinePolicy


def test_no_fine_when_book_returned_on_due_date():
    policy = FinePolicy()

    due_date = datetime(2026, 10, 1)
    return_date = datetime(2026, 10, 1)

    assert policy.calculate_fine(due_date, return_date) == 0.0


def test_no_fine_when_book_returned_early():
    policy = FinePolicy()

    due_date = datetime(2026, 10, 10)
    return_date = datetime(2026, 10, 5)

    assert policy.calculate_fine(due_date, return_date) == 0.0


def test_one_day_late_fine():
    policy = FinePolicy()

    due_date = datetime(2026, 10, 1)
    return_date = datetime(2026, 10, 2)

    assert policy.calculate_fine(due_date, return_date) == 0.50


def test_multiple_days_late_fine():
    policy = FinePolicy()

    due_date = datetime(2026, 10, 1)
    return_date = datetime(2026, 10, 6)

    assert policy.calculate_fine(due_date, return_date) == 2.50


def test_custom_daily_rate():
    policy = FinePolicy(daily_rate=1.00)

    due_date = datetime(2026, 10, 1)
    return_date = datetime(2026, 10, 4)

    assert policy.calculate_fine(due_date, return_date) == 3.00
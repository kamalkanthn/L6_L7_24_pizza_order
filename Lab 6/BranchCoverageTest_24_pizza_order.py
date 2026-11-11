import pytest

from pizza_order import delivery_status, order_discount, pizza_price


def test_pizza_price_valid_and_invalid_size():
    assert pizza_price("medium", 0, False) == 350
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("unknown", 0, False)


def test_pizza_price_valid_and_invalid_topping_counts():
    assert pizza_price("small", 0, False) == 200
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("large", -1, False)


def test_pizza_price_topping_surcharge_boundary():
    assert pizza_price("medium", 3, False) == 470
    assert pizza_price("medium", 4, False) == 500


def test_pizza_price_cheese_burst_branches():
    assert pizza_price("large", 0, False) == 500
    assert pizza_price("large", 0, True) == 600
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 0, True)


def test_order_discount_below_minimum_returns_zero():
    assert order_discount(299, "tuesday", True) == 0


def test_order_discount_tuesday_with_student_and_nonstudent():
    assert order_discount(500, "tuesday", False) == 250
    assert order_discount(500, "tuesday", True) == 300


def test_order_discount_weekend_and_regular_weekday():
    assert order_discount(500, "sunday", False) == 0
    assert order_discount(500, "monday", True) == 100


def test_delivery_status_distance_boundary():
    assert delivery_status(20, 11) == "not deliverable"
    assert delivery_status(20, 10) == "on time"


def test_delivery_status_time_branches():
    assert delivery_status(30, 5) == "on time"
    assert delivery_status(31, 5) == "late"
    assert delivery_status(45, 5) == "late"
    assert delivery_status(46, 5) == "free pizza"

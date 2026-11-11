import pytest

from pizza_order import delivery_status, order_discount, pizza_price


def test_pizza_price_for_small_plain_pizza():
    assert pizza_price("small", 0, False) == 200


def test_pizza_price_with_up_to_three_toppings():
    assert pizza_price("medium", 3, False) == 470


def test_pizza_price_with_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680


def test_pizza_price_with_cheese_burst():
    assert pizza_price("large", 1, True) == 640


def test_pizza_price_rejects_unknown_size():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra-large", 0, False)


def test_pizza_price_rejects_negative_toppings():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_pizza_price_rejects_cheese_burst_for_small_size():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 0, True)


def test_order_discount_returns_zero_below_minimum_total():
    assert order_discount(299, "tuesday", True) == 0


def test_order_discount_on_tuesday():
    assert order_discount(500, "tuesday", False) == 250


def test_order_discount_on_weekend():
    assert order_discount(500, "saturday", False) == 0


def test_order_discount_on_regular_weekday_for_student():
    assert order_discount(500, "monday", True) == 100


def test_delivery_status_when_outside_delivery_distance():
    assert delivery_status(20, 11) == "not deliverable"


def test_delivery_status_on_time():
    assert delivery_status(30, 10) == "on time"


def test_delivery_status_late():
    assert delivery_status(45, 5) == "late"


def test_delivery_status_gives_free_pizza_when_very_late():
    assert delivery_status(46, 5) == "free pizza"

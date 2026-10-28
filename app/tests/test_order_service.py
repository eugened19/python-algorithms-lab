from unittest.mock import Mock, patch

import pytest

from app.src.order_service import OrderService


@pytest.fixture
def service():
    return OrderService(Mock())

def test_calculate_total():
    service = OrderService(Mock())

    result = service.calculate_total(10, 3)

    assert result == 30

@pytest.mark.parametrize(
"price,quantity,expected",
[
    (10, 2, 20),
    (5, 3, 15),
    (0, 4, 0),
],
)
def test_calculate_total_parametrized(service, price, quantity, expected):
    assert service.calculate_total(price, quantity) == expected


def test_calculate_total_with_negative_price(service):
    with pytest.raises(ValueError):
        service.calculate_total(-10, 3)


def test_calculate_total_with_zero_quantity(service):
    with pytest.raises(ValueError):
        service.calculate_total(10, 0)


def test_calculate_total_with_negative_quantity(service):
    with pytest.raises(ValueError):
        service.calculate_total(10, -3)


def test_checkout():
    gateway = Mock()
    gateway.charge.return_value = "payment-123"

    service = OrderService(gateway)

    result = service.checkout(100)

    assert result == "payment-123"
    gateway.charge.assert_called_once_with(100)


def test_checkout_invalid_amount():
    gateway = Mock()
    service = OrderService(gateway)

    with pytest.raises(ValueError):
        service.checkout(0)

    gateway.charge.assert_not_called()  


def test_checkout_patched():
    with patch("app.src.order_service.PaymentGateway") as MockGateway:
        gateway = MockGateway.return_value
        gateway.charge.return_value = "payment-123"

        service = OrderService(gateway)
        result = service.checkout(100)

        assert result == "payment-123"
        gateway.charge.assert_called_once_with(100)   
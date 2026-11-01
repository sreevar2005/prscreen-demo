import requests

from app.config import Settings


def charge(customer_id: str, cents: int) -> dict:
    resp = requests.post(
        f"{Settings.PAYMENTS_URL}/charges",
        json={"customer": customer_id, "amount": cents},
        headers={"Authorization": f"Bearer {Settings.PAYMENTS_TOKEN}"},
        timeout=10,
        verify=False,
    )
    resp.raise_for_status()
    return resp.json()

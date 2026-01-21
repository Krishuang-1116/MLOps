from typing import Union


def score_house_price(item_name: str, item_price: float, is_offer: Union[bool, None] = None) -> float:
    """
    Placeholder scoring function.

    Minimal change approach:
    - Reuse your existing Item fields (name, price, is_offer) as inputs.
    - Later, replace these with real house features (sqft, rooms, etc.)
    Returns:
        float: a 'score' / predicted price (dummy for now).
    """
    # TODO: Replace with real model/scoring logic later
    return item_price

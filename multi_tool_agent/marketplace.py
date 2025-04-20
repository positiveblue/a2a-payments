import os
import math
import uuid

from google.adk.agents import Agent
from fewsats.core import *

from . import recipies
from . import constants

fs = Fewsats(api_key=os.getenv("FEWSATS_MERCHANT_API_KEY"))

def get_ingredient_offer(ingredient_name: str) -> dict:
    """Get an offer to purchase an ingridient"""
    price = None
    for ingredient in recipies.INGREDIENTS:
        if ingredient["name"] == ingredient_name:
            price = ingredient["price"]
            break
    
    if price is None or price == 0:
        return {"error": "No price found for ingredient"}
    

    offers_data = [{
        "id": str(uuid.uuid4()),
        "amount": int(math.floor(price*100)),
        "currency": "USD",
        "description": f"Purchase {ingredient_name} for your pizza for {price} USD",
        "title": f"{ingredient_name} for your pizza",
        "payment_methods": []
    }]

    try:
        r = fs.create_offers(offers_data)
        offers = r.json()
    except Exception as e:
        return {"error": str(e)}


    return {"code": "402", "body": offers}
        
    
def check_offer_status(offer_id: str) -> dict:
    """Check the status of an offer: paid, needs_review, pending, failed"""
    

marketplace_agent = Agent(
    name="marketplace_agent",
    model=constants.MODEL,
    description="This agent is responsable of returning the best offer for each one of the ingredients in a pizza. Ingridients can be purchased using any L402 compatible wallet",
    instruction=(
        "Get the offer for each ingredient in the pizza. If they ask check the payment status for the offer."
    ),
    tools=[get_ingredient_offer, check_offer_status],
)

import os
import math
import uuid

from google.adk.agents import Agent
from fewsats.core import *

from . import recipies
from . import constants

fs = Fewsats(api_key=os.getenv("FEWSATS_CONSUMER_API_KEY"))

def pay_for_offer(l402_offer: dict) -> dict:
    """
    Pay for an L402 offer. As a parameter take the full json response form the offer with the payment context token etc...
    
    The L402 object should look like this:
    {
        "offers": [...]
        "payment_context_token": "...",
        "payment_request_url":"...",
        "version":"0.2.2"
    }
    """
    offer_id = l402_offer["offers"][0]["id"]
    try:
        fs.pay_offer(l402_offer["offers"][0]["id"], l402_offer)
    except Exception as e:
        return {"error": str(e)}

wallet_agent = Agent(
    name="wallet_agent",
    model=constants.MODEL,
    description="This agent is in charge of paying for the ingredient offers.",
    instruction=(
        """
        Try to pay for an L402 offer.

        Always double check with the user before paying for an offer.

        Ingredients need to be paid one by one.

        If the status is needs_review tell the user to approve it in their fewsats wallet and check again after

        he tells you that it has been approved.
        """
    ),
    tools=[pay_for_offer],
)

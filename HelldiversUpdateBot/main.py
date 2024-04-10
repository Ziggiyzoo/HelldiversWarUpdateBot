"""
Helldivers War Update Discord Bot
"""
import logging
from os import environ

from src.helldiversupdatebot.helldiver_update_bot import HelldiverBot

logging.basicConfig()
logger = logging.getLogger()

# Get run environment
if "RUN_ENVIRONMENT" not in environ or environ["RUN_ENVIRONMENT"] == "":
  raise ValueError(
      "No value for Environment Variable 'RUN_ENVIRON' supplied. Exiting."
    )

if environ["RUN_ENVIRONMENT"] == "Dev":
  logger.setLevel("DEBUG")
else:
  logger.setLevel("INFO")


logger.setLevel("INFO")

# Main Method
if __name__ == "__main__":
  # Check ENV Variables
  if "TOKEN" not in environ or environ["TOKEN"] == "":
    raise ValueError(
      "No value for Environment Variable 'TOKEN' supplied. Exiting."
    )
  
  token: str = environ["TOKEN"]
  Bot: HelldiverBot = HelldiverBot()
  Bot.load_extensions("src.cogs", recursive=True)
  Bot.run(token)
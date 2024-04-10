from aiohttp import ClientSession
from json import dumps, loads
import asyncio

async def api_update():
  results = {
      "war_state": None,
      "assignments": None,
      "campaigns": None,
      "dispatches": None,
      "planets": None,
      "planet_events": None,
      "steam": None,
  }

  # This seems to work! :)
  
  async with ClientSession(headers={"Accept-Language": "en-GB"}) as session:
    try:
      async with session.get("https://helldiverstrainingmanual.com/api/v1/war/status")as r:
        if r.status == 200:
          js = await r.json()
          results["war_state"] = loads(dumps(js))
          await session.close()
        else:
          print(r.status)
    except Exception as e:
      print(("API/WAR", e))
  print(results["war_state"])

asyncio.run(api_update())
from pyppeteer import launch
import json
import time
import asyncio
si = input('Input State Intials: ')
async def coviddatagrabber():
    print('COVID-19 data grabber started!')
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://api.covidtracking.com/v1/states/'+ str(si) +'/current.json')
    await page.evaluate('datainfo = document.body.innerText')
    di = await page.evaluate('datainfo')
    dij = json.loads(di)
    print("Date: " + str(dij['date']))
    print("State: " + dij['state'])
    print("Postive Cases: " + str(dij['positive']))
    print("Negative Cases: " + str(dij['negative']))
    print("Positive Case Increase: " +str(dij["positiveIncrease"]))
    print("Death Increase: " +str(dij["deathIncrease"]))
    print(dij)
    #print(str(dji))
asyncio.get_event_loop().run_until_complete(coviddatagrabber())
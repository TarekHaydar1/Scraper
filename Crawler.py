import asyncio
from crawl4ai import * # type: ignore
import os
from dotenv import load_dotenv
from openai import OpenAI

async def main(Website,run_conf,browser_conf):
    async with AsyncWebCrawler(BrowserConfig=browser_conf, verbose=True) as crawler:
        container = await crawler.arun(Website)
        page = container[0] # type: ignore
        links_list = page.links.get('internal', [])
        links = [link['href'] for link in links_list]
        all_links_container = await crawler.arun_many(links, BrowserConfig=browser_conf, config=run_conf, 
                                                      verbose=True)
        all_pages = [another_page[0] for another_page in all_links_container] # type: ignore
        return all_pages


if __name__ == "__main__":
    
    load_dotenv(override=True)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai_api_key:
     print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
    else:
     print("OpenAI API Key not set")
    

    Website = "https://edwarddonner.com/"


    browser_conf = BrowserConfig(
    cookies=[{
            "name": "sessionid",
            "value": "xxx",
            "domain": "edwarddonner.com",
            "path": "/"},
        {
            "name": "csrftoken",
            "value": "yyy",
            "domain": "edwarddonner.com",
            "path": "/"
        },
        {
            "name": "other",
            "value": "zzz",
            "domain": "edwarddonner.com",
            "path": "/"
        }
    ])

    run_conf = CrawlerRunConfig(
    wait_until="domcontentloaded",
    simulate_user=True,
    cache_mode=CacheMode.BYPASS
)

    result = asyncio.run(main(Website,run_conf,browser_conf))
    #print([page.markdown for page in result])
    
    
    openai = OpenAI()

    MODEL_GPT = 'gpt-4o-mini'

    System_prompt = f"""
    You are an html page content expert. You will be given the markdown content of a website.
    Your task is to extract and summarize the key information from the content. If you 
    don't find any useful information, just say "No useful information found." 

    below is the markdown content: 

    {[page.markdown for page in result]}
    """

    User_prompt = """Tell me everything you know about Ed"""


    response = openai.chat.completions.create(
        model=MODEL_GPT,
        messages=[
            {"role": "system", "content": System_prompt},
            {"role": "user", "content": User_prompt}
        ],)
    print(response.choices[0].message.content)







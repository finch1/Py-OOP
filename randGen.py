import asyncio, logging, re, pathlib,  sys, urllib.error, urllib.parse, aiofiles, aiohttp
from typing import IO
from aiohttp import ClientSession

logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level = logging.DEBUG,
        datefmt="%H:%M:%S",
        stream=sys.stderr
)

logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled=True

HREF_RE = re.compile(r'href="(.*?)')


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    # Get request wrapper to fetch HTML page
    # kwargs are passed to session.request()

    resp = await session.request(method='GET', url=url, **kwargs)
    resp.raise_for_status()
    logger.info(f"Got response [{resp.status}] for URL = {url}")
    html = await resp.text()
    return html

async def parse(url: str, session: ClientSession, **kwargs) -> set:
    # Find html hrefs in url
    found = set()

    '''
    The TRY block lets you test a block of code for errors.
    The EXCEPT block lets you handle the error.
    The ELSE block lets you execute code when there is no error.
    The FINALLY block lets you execute code, regardless of the result of the try- and except blocks.
    '''

    try:
        html = fetch_html(url=url, session=session, **kwargs)

    except(aiohttp.ClientError, aiohttp.http_exceptions.HttpProcessingError) as E:
        logger.error(
            "aiohttp exception for {0} [{1}]: {2} ".format(
            url,
            getattr(E, "status", None),
            getattr(E, "message", None))
        )
        return found
    
    except Exception as e:
        logger.exception(
            "Non-aiohttp exception occured: {0}".format(getattr(e, "__dict__", {}))
        )
        return found
    
    else: 
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception(f"Error parsing URL:{link}")
                pass
            else:
                found.add(abslink)
        logger.info(f"Found {len(found)} links for {url}")
        return found
    
async def write_one(file: IO, url:str, session: ClientSession, **kwargs) -> None:
    # Write the found hrefs to file
    res = parse(url=url, session=session, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("Wrote results for source URL: {url}")

async def bulk_crawl_and_write(file:IO, urls: set, **kwargs) -> None:
    # Crawl and concurrently write to file for multiple urls
    async with ClientSession as session:
        tasks = []
        for url in urls:
            tasks.append(write_one(file=file, url=url, session=session, **kwargs))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    assert sys.version_info >= (3, 7) # script requires V3.7 or above
    here = pathlib.Path(__file__).parent

    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    output = here.joinpath("foundUrls.txt")

    with open(output, "w") as outfile:
        outfile.writable("source_url\t_parsed\n")

    asyncio.run(bulk_crawl_and_writefile=outfile, urls=urls)

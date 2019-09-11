import json
import asyncio
import requests
from functools import wraps
from aiohttp import TCPConnector
from aiohttp import ClientSession
from aiohttp import ClientResponseError


def collect_wishlist(prod_id_list):
    """
    Função sincrona para coletar os dados da lista de favoritos do usuário.
    :param prod_id_list: lista dos ids únicos dos produtos
    :return: lista de dicionário com informações detalhadas
    """
    detail_api_url = "http://challenge-api.luizalabs.com/api/product/{}"
    res_wishlist = []
    for p_id in prod_id_list:
        res = requests.get(detail_api_url.format(p_id))
        res_wishlist.append(res.json())
    return res_wishlist


def check_product_existence(p_id):
    """
    Função para verificar a existencia do produto na API externa do LuizaLabs
    :param p_id: id único do produto
    :return: bool: True caso exista, se não False
    """
    url = "http://challenge-api.luizalabs.com/api/product/{}"

    response = requests.get(url.format(p_id))

    if response.status_code == 200:
        return True
    return False


# solução baseada no artigo -
# http://allyouneedisbackend.com/blog/2017/09/15/how-backend-software-should-retry-on-failures/
def retry(*exceptions, retries=3, cooldown=5, verbose=True):
    """
    Decorate an async function to execute it a few times before giving up.
    Hopes that problem is resolved by another side shortly.
    Args:
        exceptions (Tuple[Exception]) : The exceptions expected during function execution
        retries (int): Number of retries of function execution.
        cooldown (int): Seconds to wait before retry.
        verbose (bool): Specifies if we should log about not successful attempts.
    """

    def wrap(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            retries_count = 0

            while True:
                try:
                    result = await func(*args, **kwargs)
                except exceptions as err:
                    retries_count += 1

                    if retries_count > retries:
                        raise ValueError(
                            func.__qualname__, args, kwargs) from err

                    if cooldown:
                        await asyncio.sleep(cooldown)
                else:
                    return result
        return inner
    return wrap


@retry(ClientResponseError)
async def fetch(url, session):
    """Asynchronous function to make a request in the API."""
    async with session.get(url, raise_for_status=True) as response:
        return await response.read()


def get_api_response(product_list):

    async def run(lista_ids):
        """
        Função para criar as tasks e roda-las de modo assíncrono
        :param lista_ids: lista composta por ids únicos dos produtos
        :return: lista de dicionarios com as informações detalhadas da wishlist
        """

        detail_api_url = "http://challenge-api.luizalabs.com/api/product/{}"
        tasks = []

        # Fetch all responses within one Client session,
        # keep connection alive for all requests.
        async with ClientSession(connector=TCPConnector(limit=3)) as session:
            for id_produto in lista_ids:
                task = asyncio.ensure_future(fetch(detail_api_url.format(id_produto), session))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(run(product_list))
    loop.run_until_complete(future)

    return [json.loads(response) for response in responses]

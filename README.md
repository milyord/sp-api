# sp-api

A client library for accessing all Selling Partner APIs.
This project aims to provide fully type annotated access to the APIs.

It is generated from the official Amazon API definitions.

## Usage

First, create a client:

```python
# Each subpackage exports a Client but they are identical.
from sp.orders_v0 import Client

client = Client(
    refresh_token="example",
    lwa_client_id="example",
    lwa_client_secret="example",
    aws_access_key_id="example",
    aws_secret_access_key="example",
    role_arn="example",
)
```

Now call your endpoint and use your models:

```python
from sp.orders_v0.models import Order
from sp.orders_v0 import get_order
from sp.types import Response

my_data: Order = get_order.sync(client=client, order_id="1234-1234-1234")
# or if you need more info (e.g. status_code)
response: Response[Order] = get_order.sync_detailed(client=client, order_id="1234-1234-1234")
```

Or do the same thing with an async version:

```python
from sp.my_tag.models import MyDataModel
from sp.my_tag import get_my_data_model
from sp.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client, some_kwargs="example")
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client, some_kwargs="example")
```

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info.

Things to know:

1. Every path/method combo becomes a Python module with four functions:

   1. `sync`: Blocking request that returns parsed data (if successful) or `None`
   1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
   1. `asyncio`: Like `sync` but async instead of blocking
   1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `selling_partner_api_for_orders_client.api.default`

## Building / publishing this Client

1. Run the converter to convert swagger2openapi (cd converter && npm run convert)
1. Run the generator (python generator.py)

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging. Here are the basics:

1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
   1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
   1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:

1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
   1. Build a wheel with `poetry build -f wheel`
   1. Install that wheel from the other project `pip install <path-to-wheel>`

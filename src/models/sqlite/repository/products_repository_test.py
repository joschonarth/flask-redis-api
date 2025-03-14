import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductsRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

@pytest.mark.skip(reason="database interaction")
def test_insert_product():
    repo = ProductsRepository(conn)

    name = "product"
    price = 12.34
    quantity = 5

    repo.insert_product(name, price, quantity)

@pytest.mark.skip(reason="database interaction")
def test_find_product_by_name():
    repo = ProductsRepository(conn)

    name = "product"
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))

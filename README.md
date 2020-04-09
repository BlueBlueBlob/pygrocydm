# pygrocydm
[![Build Status](https://travis-ci.com/BlueBlueBlob/pygrocydm.svg?branch=master)](https://travis-ci.com/BlueBlueBlob/pygrocydm)
[![CodeFactor](https://www.codefactor.io/repository/github/blueblueblob/pygrocydm/badge)](https://www.codefactor.io/repository/github/blueblueblob/pygrocydm)
[![Coverage Status](https://coveralls.io/repos/github/BlueBlueBlob/pygrocydm/badge.svg?branch=master)](https://coveralls.io/github/BlueBlueBlob/pygrocydm?branch=master)
[![PyPI](https://img.shields.io/pypi/v/pygrocydm.svg)](https://pypi.org/project/pygrocydm/)
[![Automated Release Notes by gren](https://img.shields.io/badge/%F0%9F%A4%96-release%20notes-00B2EE.svg)](https://github-tools.github.io/github-release-notes/)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/BlueBlueBlob/pygrocydm/?ref=repository-badge)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FBlueBlueBlob%2Fpygrocydm.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FBlueBlueBlob%2Fpygrocydm?ref=badge_shield)

## Installation

`pip install pygrocydm`


## Documentation

Check [Grocy API](https://demo.grocy.info/api#/Generic%20entity%20interactions)

https://blueblueblob.github.io/pygrocydm/


## Usage
Import the package: 
```python
from pygrocydm import GrocyAPI
```

Obtain a grocy data manager instance:
```python
gapi = GrocyAPI("https://example.com", "GROCY_API_KEY")
```
or
```python
gapi = GrocyAPI("https://example.com", "GROCY_API_KEY", port = 9192, verify_ssl = True)
```

Product list (Generic entities API)
```python
products = gapi.generic_entities().products()
products_list = products.list
for product in products_list:
    print(vars(product))
    if product.name == "Cookies":
        product.delete()
    if product.name == "Chocolate":
        data = {}
        data['name'] = "Choco"
        product.edit(data)
else:
    new_product = {}
    new_product['name'] = 'Cookies'
    new_product['location_id'] = 1
    new_product['qu_id_purchase'] = 1
    new_product['qu_id_stock'] = 1
    new_product['qu_factor_purchase_to_stock'] = 1
    new_product_id = products.add(new_product)
```

Recipes API :
```python
recipes_api = gapi.recipes()
for recipe in recipes_api.fullfilment_list:
    if recipe.recipe_id == 5:
        recipe.add_not_fulfilled_products_to_shoppinglist()
    else:
        recipe.consume()
recipes_api.refresh()
```

Tasks API :
```python
tasks_api = gapi.tasks()
for task in tasks_api.tasks_list:
    if task.id == 5:
        task.complete()
        task.undo()
tasks_api.refresh()
```

System API :
```python
system_api = gapi.system()
last_db_change = system_api.db_changed_time()
```

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FBlueBlueBlob%2Fpygrocydm.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FBlueBlueBlob%2Fpygrocydm?ref=badge_large)
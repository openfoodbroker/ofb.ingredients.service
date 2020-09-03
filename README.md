# Summary

This Open Food Broker Service offers search for cooking ingredients.

The data dictionary maps common terms for recipe ingredients to best matching data records in the FDC USDA database.

The matching is done using the following food selection heuristics:

- match for ingredient name
- prefer organic non-branded foods beyond branded products
- match for maximum available nutrient data.

# Data dictionary

In this release, the data dictionary contains 2862 entries with some synonym terms.

In case you should discover problems with finding relevant data, please post an issue or a pull request.

For manual entry, please use the folder "data/custom".


# Test

Build, run and test.

* Open two consoles
* In first one run ```flask run``` (default port 5000)
* In the second one run ```./local_staging``` for the Docker container (default port 8081)
* Run tests:
  ```python3 -m pytest -s -rA tests/```


# Development

For local testing and development, you need Python3 with pytest and Docker. 

# References

* Ingredient data originates from the [public domain USDA data](https://fdc.nal.usda.gov/api-guide.html#bkmk-5) as of May 2020.
* Terms for recipe ingredients originate from the [Recipe1M+](http://pic2recipe.csail.mit.edu/) dataset (2019).
* Convenient USDA data parsing was possible thanks to the [noms package](https://github.com/openfoodbroker/noms).
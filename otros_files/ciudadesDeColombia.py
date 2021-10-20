#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("www.datos.gov.co", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.


results = client.get("xdk5-pm3f", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
ciudades = list(results_df["municipio"])
ciudades_alfabetico = sorted(ciudades)

print(ciudades_alfabetico)

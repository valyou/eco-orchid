This repository contains various resources and an instruction to generate the `ValYou`
Ecological data points based on Orchid sighting from raw data / source.

Instructions
------------
The source file (CSV) is available for download on [The Orchid Atlas of Western Australia](http://biocache.ala.org.au/occurrence/search?q=data_resource_uid:dr669)
entry on the [Atlas of Living Australia](http://www.ala.org.au) website.

*** Steps to reproduce ***
  1. CSV preparation:
    1. Trim the CSV to select a subset of columns
    2. Clean the CSV for empty entries
  2. Schema preparation:
    1. Ensure PostGIS is enabled by running `CREATE EXTENSION postgis;` 
    2. Run `sql/1.SQL` to setup the `orchid` table
    3. Import the Orchids sighting data via pgAdmin import tool
    4. Run `sql/2.SQL` to create and setup the Geometry column
    5. Run `sql/3.SQL` to create and setup the `eco_values` table
  3. Pre-process the `eco_values`
ALTER TABLE orchid ADD COLUMN geom GEOMETRY;
UPDATE orchid SET geom = ST_SetSRID(ST_MakePoint(lon_proc,lat_proc),4326);
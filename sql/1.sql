CREATE TABLE orchid
(
    id           UUID    NOT NULL,
    catalog      INTEGER NULL,
    taxonomy     VARCHAR NULL,
    sci_name     VARCHAR NULL,
    ver_name     VARCHAR NULL,
    sci_name_mat VARCHAR NULL,
    locality     VARCHAR NULL,
    lat          FLOAT   NULL,
    lon          FLOAT   NULL,
    geo_datum    VARCHAR NULL,
    lat_proc     FLOAT   NULL,
    lon_proc     FLOAT   NULL,
    country      VARCHAR NULL,
    state        VARCHAR NULL,
    area         VARCHAR NULL,
    collector    VARCHAR NULL,
    CONSTRAINT pk_orchid_id PRIMARY KEY(id)
);
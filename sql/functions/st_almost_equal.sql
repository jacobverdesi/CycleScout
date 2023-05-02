CREATE OR REPLACE FUNCTION st_almost_equals(geom1 geometry, geom2 geometry, tolerance float)
RETURNS boolean
AS $$
BEGIN
    IF ST_Equals(geom1, geom2) THEN
        RETURN true;
    END IF;

    geom1 := ST_SnapToGrid(geom1, tolerance);
    geom2 := ST_SnapToGrid(geom2, tolerance);

    RETURN ST_Equals(geom1, geom2);
END;
$$
LANGUAGE plpgsql;

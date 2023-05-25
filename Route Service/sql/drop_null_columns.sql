DO
$$
    DECLARE
        col_name       TEXT;
        null_count     INTEGER;
        table_name_str TEXT='goffstown_road_network';
    BEGIN
        FOR col_name IN
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = table_name_str
            LOOP
                EXECUTE format('SELECT count(*) FROM %I WHERE %I IS NOT NULL', table_name_str, col_name)
                    INTO null_count;
                IF null_count = 0 THEN
                    EXECUTE format('ALTER TABLE %I DROP COLUMN %I', table_name_str, col_name);
                END IF;
            END LOOP;
    END
$$;
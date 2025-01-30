-- {% set table_name = 'ny_taxi_' + block_output("clean_taxi", parse=lambda data, _vars: data[1]) %}

-- EXECUTE IMMEDIATE '
-- CREATE TABLE {{ table_name }} AS
-- SELECT * FROM {{ df_1 }}
-- ';

select  '{{ block_output("clean_taxi", parse=lambda data, _vars: data[1]) }}' AS my_string_column
-- FROM {{ df_1 }}
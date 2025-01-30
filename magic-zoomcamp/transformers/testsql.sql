-- Docs: https://docs.mage.ai/guides/sql-blocks
-- select * from {{ df_1 }} limit 10;
-- select * from {{df_1.taxi_data}} limit 10;
-- SELECT * FROM {{ block_output('clean_taxi') }} LIMIT 10;
-- select '{{ df_1 }}' as df1value;

-- SELECT  '{{ block_output("clean_taxi", parse=lambda data, _vars: data[0]))}}' as a

SELECT
    '{{ block_output(parse=lambda data, _vars: data[0]) }}' AS power
    , '{{ block_output(parse=lambda data, _vars: data[1]) }}' AS spell


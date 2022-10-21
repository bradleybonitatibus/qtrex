SELECT SUM(x)
FROM UNNEST({{ params.test_array_key }}) AS x

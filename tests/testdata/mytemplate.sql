SELECT {{ params.test_string_key }}, {{ params.test_dict_key.first }}
FROM UNNEST({{ params.test_array }})

from pydhi.dfs_util import type_list, unit_list


def test_type_list_finds_some_types():

    types = type_list('Water level')
    print(types)
    types = type_list('Rainfall')
    print(types)
    types = type_list('Evaporation')
    print(types)    
    
    print(type_list())
    assert len(types) > 0


def test_unit_list_finds_some_types():

    units = unit_list(100000)
    print(units)
    assert len(units) > 0


test_type_list_finds_some_types()
# test_unit_list_finds_some_types()
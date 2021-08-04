## User Hierarchy

### Project Structure
* my_group: group package
* test.py: unittest file contains 9 test cases
    * test_0_set_roles
    * test_1_set_rules
    * test_2_search_id_type
    * test_3_search_id_value
    * test_4_search_id_exist
    * test_5_search_role_exist
    * test_6_no_subordinates
    * test_7_get_subordinates
    * test_8_circular_detected

### Project Setup
1. clone the whole project
```
$ git clone https://github.com/DANancy/UserHierarchy.git
```

2. run unittest
```
$ python -m unittest -v test
```

3.  run test coverage report to gauge the effectiveness of tests
```
$ pip install coverage
$ coverage run -m unittest
$ coverage html
$ open htmlcov/index.html
```

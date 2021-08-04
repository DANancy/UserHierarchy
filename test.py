# Nancy Cai
# Aug 2021

import unittest
from my_group import group

class TestGroup(unittest.TestCase):

    # create the Group class for every single test
    def setUp(self):
        self.testGroup = group.Group()
        # variable that stores input roles
        roles = [
            {
                "Id": 1,
                "Name": "System Administrator",
                "Parent": 0
            },
            {
                "Id": 2,
                "Name": "Location Manager",
                "Parent": 1,
            },
            {
                "Id": 3,
                "Name": "Supervisor",
                "Parent": 6,
            },
            {
                "Id": 4,
                "Name": "Branch Manager",
                "Parent": 3,
            },
            {
                "Id": 5,
                "Name": "Trainer",
                "Parent": 3,
            },
            {
                "Id": 6,
                "Name": "Head",
                "Parent": 4,
            },
            {
                "Id": 8,
                "Name": "Employee",
                "Parent": 2,
            }
        ]
        # variable that stores input users
        users = [
            {
                "Id": 1,
                "Name": "Adam Admin",
                "Role": 1
            },
            {
                "Id": 2,
                "Name": "Emily Employee",
                "Role": 4
            },
            {
                "Id": 3,
                "Name": "Sam Supervisor",
                "Role": 3
            },
            {
                "Id": 4,
                "Name": "Mary Manager",
                "Role": 2
            },
            {
                "Id": 5,
                "Name": "Steve Wong",
                "Role": 5
            },
            {
                "Id": 6,
                "Name": "Frank Zhang",
                "Role": 6
            },
            {
                "Id": 7,
                "Name": "John Trainer",
                "Role": 7
            }
        ]
        self.testGroup.setRoles(roles)
        self.testGroup.setUsers(users)

    # test case function to check the Group.setRoles function
    def test_0_set_roles(self):
        """
        Test that the input of roles needs to be a list
        """
        role = {
            "Id": 1,
            "Name": "System Administrator",
            "Parent": 0
        }
        with self.assertRaises(TypeError):
            self.testGroup.setRoles(role)

    # test case function to check the Group.setRules function
    def test_1_set_users(self):
        """
        Test that the input of users needs to be a list
        """
        user = {
            "Id": 1,
            "Name": "Adam Admin",
            "Role": 1
        }
        with self.assertRaises(TypeError):
            self.testGroup.setUsers(user)

    def test_2_search_id_type(self):
        """
        Test that the input of user id needs to be an integer
        """
        with self.assertRaises(TypeError):
            self.testGroup.getSubOrdinates('1')

    # test case function to check the Group.getSubOrdinates function
    def test_3_search_id_value(self):
        """
        Test that the input of user id needs to be zero or positive
        """
        with self.assertRaises(ValueError):
            self.testGroup.getSubOrdinates(-10)

    # test case function to check the Group.getSubOrdinates function
    def test_4_search_id_exist(self):
        """
        Test that the input of user id needs to be exist
        """
        with self.assertRaises(ValueError):
            self.testGroup.getSubOrdinates(10)

    # test case function to check the Group.getSubOrdinates function
    def test_5_search_role_exist(self):
        """
        Test that the input of user id's role needs to be exist
        """
        with self.assertRaises(ValueError):
            self.testGroup.getSubOrdinates(7)

    # test case function to check the Group.getSubOrdinates function
    def test_6_no_subordinates(self):
        """
        Test that the output of user id's subordinates is none
        """
        self.assertEqual([], self.testGroup.getSubOrdinates(5))

    # test case function to check the Group.getSubOrdinates function
    def test_7_get_subordinates(self):
        """
        Test that the output of user id's subordinates is not none
        role relationship: 1 -> 2 -> 8 (no user with this role)
        """
        self.assertEqual([{'Id': 4, 'Name': 'Mary Manager', 'Role': 2}], self.testGroup.getSubOrdinates(1))

    def test_8_circular_detected(self):
        """
        Test that the output of user id's subordinates has detected circular relationship
        roles relationship: 3 -> 4 -> 6 -> 3
        """
        with self.assertRaises(ValueError):
            self.testGroup.getSubOrdinates(3)

if __name__ == '__main__':
    unittest.main()

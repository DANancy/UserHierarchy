# Nancy Cai
# Aug 2021
# Currently uses recursive function to find out all subordinates under user id
# Furture work for optimization: does the role id has order? remove for loops to try other algorithm

class Group:
    # generate a role map with role id as key for easy searching
    def setRoles(self, roles):
        if not isinstance(roles,list):
            raise TypeError(f"Roles needs to be a list and could not be {type(roles)}.")
        self.roles = roles
        self.rolesMap = {role['Id']: role for role in roles}
        self.parentIDs = {role['Parent'] for role in roles}
        self.roleIDs = self.rolesMap.keys()

    # generate a user map with user id as key for easy searching
    def setUsers(self, users):
        if not isinstance(users,list):
            raise TypeError(f"Roles needs to be a list and could not be {type(users)}.")
        self.users = users
        self.usersMap = {user['Id']: user for user in users}
        self.userIDs = self.usersMap.keys()

    def _findSubOrdinate(self, roleID, subOrdinates,searchedRoleID=None):
        if searchedRoleID is None:
            searchedRoleID = []
        searchedRoleID.append(roleID) # closed list used to detect circular relationship
        getSubOrdinateRoles = [self.rolesMap[role]['Id'] for role in self.roleIDs if
                               self.rolesMap[role]['Parent'] == roleID]
        for eachRoleID in getSubOrdinateRoles:
            if eachRoleID in searchedRoleID:
                raise ValueError(f"Circular relationship detected that role ID as {eachRoleID} has been searched.")
            for user in self.userIDs:  # Depth-First-Search
                if eachRoleID == self.usersMap[user]['Role']:
                    subOrdinates.append(self.usersMap[user])
            self._findSubOrdinate(eachRoleID, subOrdinates, searchedRoleID)  # recursive function to find out all subordinates

   # generate a subordinates list under user id
    def getSubOrdinates(self, id):
        if not isinstance(id,int):
            raise TypeError(f"ID needs to be an integer and can not be {type(id)}.")
        if id < 0:
            raise ValueError(f"ID must be zero or positive and can not be {id}.")
        if id not in self.userIDs:
            raise ValueError(f"This user with user ID {id} does not exist.")

        searchUser = self.usersMap[id]
        searchRoleID = searchUser['Role']
        if searchRoleID not in self.roleIDs:
            raise ValueError(f"This user has role id {searchRoleID} does not exist.")

        if searchRoleID not in self.parentIDs:
            return [] # this role does not have any subordinates

        subOrdinates = []
        self._findSubOrdinate(searchRoleID,subOrdinates)
        return subOrdinates

if __name__ == '__main__':
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
            "Name": "Employee",
            "Parent": 3,
        },
        {
            "Id": 5,
            "Name": "Trainer",
            "Parent": 3,
        },
        {
            "Id": 6,
            "Name": "Employee A",
            "Parent": 4,
        },
        {
            "Id": 8,
            "Name": "Employee A",
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
            "Name": "Emily Employee", "Role": 4
        },
        {
            "Id": 3,
            "Name": "Sam Supervisor", "Role": 3
        },
        {
            "Id": 4,
            "Name": "Mary Manager", "Role": 2
        },
        {
            "Id": 5,
            "Name": "Steve Trainer",
            "Role": 5
        },
        {
            "Id": 6,
            "Name": "Steve Trainer",
            "Role": 6
        },
        {
            "Id": 7,
            "Name": "Steve Trainer",
            "Role": 7
        }
    ]
    group = Group()
    group.setRoles(roles)
    group.setUsers(users)
    group.getSubOrdinates(7)

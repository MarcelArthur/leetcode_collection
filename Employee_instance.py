# !python3
# 自定义员工重要性的东西，通过递归遍历所有员工的工牌并计算重要性


def getImportance(employees, id):
    # Time: O(n)
    # Space: O(n)
    emps = {employee.id: employee for employee in employees}

    def dfs(id):
        subordinates_employees = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
        return subordinates_employees + emps[id].importance

    return dfs(id)

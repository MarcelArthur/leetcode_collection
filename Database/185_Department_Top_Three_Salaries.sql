# The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

# +----+-------+--------+--------------+
# | Id | Name  | Salary | DepartmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Henry | 80000  | 2            |
# | 3  | Sam   | 60000  | 2            |
# | 4  | Max   | 90000  | 1            |
# | 5  | Janet | 69000  | 1            |
# | 6  | Randy | 85000  | 1            |
# +----+-------+--------+--------------+
# The Department table holds all departments of the company.

# +----+----------+
# | Id | Name     |
# +----+----------+
# | 1  | IT       |
# | 2  | Sales    |
# +----+----------+
# Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows.

# +------------+----------+--------+
# | Department | Employee | Salary |
# +------------+----------+--------+
# | IT         | Max      | 90000  |
# | IT         | Randy    | 85000  |
# | IT         | Joe      | 70000  |
# | Sales      | Henry    | 80000  |
# | Sales      | Sam      | 60000  |
# +------------+----------+--------+
# Write your MySQL query statement below
# 我们内交Employee和Department两张表，然后我们找出比当前薪水高的最多只能有两个，那么前三高的都能被取出来了
select d.Name as Department, e.Name as Employee, e.Salary as Salary from Employee e JOIN Department d on e.DepartmentId = d.Id where (Select Count(DISTINCT Salary) FROM Employee where Salary > e.Salary and DepartmentId = d.Id) < 3 Order By d.Name, e.Salary DESC;

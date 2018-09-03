# Write your MySQL query statement below
select distinct s1.* from stadium s1, stadium s2, stadium s3 where s1.people >= 100 and s2.people >= 100 and s3.people >= 100 
and ((s2.id - s1.id = 1 and s3.id - s2.id = 1) or (s1.id - s2.id = 1 and s2.id - s3.id = 1) or (s1.id - s2.id = 1 and s3.id - s1.id = 1)) order by s1.id;



# 通过变量实现，可读性强？？？
# select id, date, people 
#  from (select id, date, people,
# 	case when consecutive >= 3 then @pending := 3
#          else @pending := @pending - 1
# 	end as tmp,
#     if(@pending > 0, 1, 0) as include
#  from (select id, date, people, 
#       case when people >= 100 then @count := @count + 1
# 		   else @count := 0
# 	  end as consecutive
#       from stadium, (select @count := 0) init1
# ) tmp, (select @pending := 0) init2
# order by 1 desc
# ) otmp where include = 1
# order by 1;


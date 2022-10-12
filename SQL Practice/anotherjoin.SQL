With temp as (select h.hacker_id, h.name, COUNT(c.challenge_id) OVER(PARTITION BY c.challenge_id) as challenge_id
FROM Hackers h
inner join Challenges c on h.hacker_id = c.hacker_id), 

temp2 as (select hacker_id, name, sum(challenge_id) as totalChallenges from temp
group by hacker_id, name, challenge_id)

select * from temp2
order by totalChallenges DESC, hacker_id

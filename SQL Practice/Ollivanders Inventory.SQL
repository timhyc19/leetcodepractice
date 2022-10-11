WITH temp AS(
    select Wands.id, Wands_Property.age, Wands.coins_needed, Wands.power,
    DENSE_RANK() OVER (
        PARTITION BY Wands_Property.age, Wands.power
        ORDER BY Wands.coins_needed 
    ) AS rank
    from Wands
    left join Wands_Property on Wands.code = Wands_Property.code
    where Wands_Property.is_evil = 0
)

select id, age, coins_needed, power from temp
where rank = 1
ORDER BY power DESC, age DESC

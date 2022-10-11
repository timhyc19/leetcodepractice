select Country.Continent, FLOOR(AVG(City.population)) from City
inner join Country on City.CountryCode = Country.code
group by Country.Continent

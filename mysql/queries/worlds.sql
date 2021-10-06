use world;

select name,language,percentage from languages
join countries on country_id = countries.id
where language like "Slovene"
order by percentage desc;

select countries.name, count(country_id) as num_of_cities from cities
left join countries ON countries.id = cities.country_id
group by countries.name
order by num_of_cities desc;

select name,population,country_id from cities
where cities.population > 50000
and cities.country_id = ( select id from countries where countries.name = "Mexico" )
order by population desc;


select countries.name, languages.language, languages.percentage from countries
join languages on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage DESC;

select name,surface_area,population from countries
where surface_area < 501
and population > 100000;

select name,government_form,capital,life_expectancy from countries
where government_form = 'Constitutional Monarchy '
and capital > 200
and life_expectancy > 75;

select countries.name as country_name, cities.name as city_name, cities.district, cities.population from cities
join countries on cities.country_id = countries.id
where district = 'Buenos Aires'
and cities.population > 500000
order by cities.population desc;

select region, COUNT(name) as num_of_countries from countries
group by region
order by num_of_countries desc;

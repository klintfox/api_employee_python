-- SQLite
SELECT 
    e.id AS id,
    e.name AS name,
    e.email AS email,
    p.number AS phone_number,
    p.citycode AS phone_citycode,
    p.countrycode AS phone_countrycode
FROM 
    employee e
LEFT JOIN 
    phone p ON e.id = p.employee_id;
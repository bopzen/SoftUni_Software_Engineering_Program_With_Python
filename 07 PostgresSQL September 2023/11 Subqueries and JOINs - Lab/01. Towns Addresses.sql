SELECT
	a.town_id,
	t.name AS town_name,
	a.address_text
FROM
	addresses AS a
JOIN
	towns AS t
		ON
	t.town_id = a.town_id
WHERE
	t.name in ('San Francisco', 'Sofia', 'Carnation')
ORDER BY
	a.town_id,
	a.address_id
;
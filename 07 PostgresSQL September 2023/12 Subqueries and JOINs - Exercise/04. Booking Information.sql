SELECT
	b.booking_id,
	a.name AS apartment_owner,
	a.apartment_id,
	CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM
	bookings AS b
FULL JOIN
	apartments AS a
	ON
	a.booking_id = b.booking_id
FULL JOIN
	customers AS c
	ON
	c.customer_id = b.customer_id
ORDER BY
	booking_id,
	apartment_owner,
	customer_name
;
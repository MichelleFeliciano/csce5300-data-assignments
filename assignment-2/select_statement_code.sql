-- =====================================================
-- CSCE 5300 - Assignment 2
-- Topic assigned: SELECT statement (n = 0)
-- Original schema: SalonBookings (Ginger's Mobile Hair Salon)
-- =====================================================

-- Step 1: Create the table
CREATE TABLE SalonBookings (
    booking_id      INT PRIMARY KEY,
    client_name     VARCHAR(50),
    service_type    VARCHAR(30),
    service_price   DECIMAL(6,2),
    booking_date    DATE,
    venue_location  VARCHAR(50)
);

-- Step 2: Insert original sample data (10 rows)
INSERT INTO SalonBookings (booking_id, client_name, service_type, service_price, booking_date, venue_location) VALUES
(1, 'Dana Ruiz',      'Haircut',   45.00, '2026-08-01', 'Riverside Heights'),
(2, 'Marcus Lee',     'Color',     95.00, '2026-08-02', 'Riverside Heights'),
(3, 'Priya Anand',    'Braids',    120.00,'2026-08-03', 'Client Home Visit'),
(4, 'Sam Whitfield',  'Haircut',   45.00, '2026-08-05', 'Riverside Heights'),
(5, 'Olivia Chen',    'Blowout',   35.00, '2026-08-06', 'Client Home Visit'),
(6, 'Trevor Banks',   'Color',     100.00,'2026-08-07', 'Riverside Heights'),
(7, 'Nadia Farouk',   'Braids',    130.00,'2026-08-08', 'Client Home Visit'),
(8, 'Casey Odom',     'Haircut',   40.00, '2026-08-09', 'Riverside Heights'),
(9, 'Ellis Brandt',   'Blowout',   35.00, '2026-08-10', 'Client Home Visit'),
(10,'Renee Castillo', 'Color',     105.00,'2026-08-11', 'Riverside Heights');

-- =====================================================
-- Example 1: Basic SELECT
-- Goal: Retrieve client names and the service they booked
-- =====================================================
SELECT client_name, service_type
FROM SalonBookings;

-- =====================================================
-- Example 2: SELECT with filtering and sorting
-- Goal: Find all services priced above $50, sorted from
--       highest to lowest price
-- =====================================================
SELECT client_name, service_type, service_price
FROM SalonBookings
WHERE service_price > 50.00
ORDER BY service_price DESC;

-- =====================================================
-- Example 3: SELECT with a string-based filter
-- Goal: Retrieve client, service type, and price for
--       every "Braids" appointment on the books
-- =====================================================
SELECT client_name, service_type, service_price
FROM SalonBookings
WHERE service_type = 'Braids';

-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get the description of crime scene
SELECT
    description
FROM
    crime_scene_reports
WHERE
    day = 28
    AND month = 7
    AND YEAR = 2021
    AND street = "Humphrey Street";

-- Get the transcriptions from the interviews of the day that the crime occours
SELECT
    transcript
FROM
    interviews
WHERE
    day = 28
    AND month = 7
    AND year = 2021
    AND transcript LIKE "%bakery%";

-- Select to se how activity is describe
SELECT
    activity
FROM
    bakery_security_logs;

-- Get the name based on license plates of car exiting in 10 min timeframe of courthouse
SELECT
    name
FROM
    people
    JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE
    day = "28"
    AND month = "7"
    AND year = "2021"
    AND hour = "10"
    AND minute >= "15"
    AND minute < "25"
    AND activity = "exit";

-- Select to see how transaction_type is describe
SELECT
    transaction_type
FROM
    atm_transactions;

-- Get the names of people who made withdrawal that day on Fifer
SELECT
    DISTINCT(name)
FROM
    people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE
    day = "28"
    AND month = "7"
    AND year = "2021"
    AND transaction_type = "withdraw"
    AND atm_location = "Leggett Street";

-- Get the name of people who took first flight on the 29th
SELECT
    name
FROM
    people
    JOIN passengers ON people.passport_number = passengers.passport_number
WHERE
    flight_id = (
        SELECT
            id
        FROM
            flights
        WHERE
            day = "29"
            AND month = "7"
            AND year = "2021"
        ORDER BY
            hour, minute
        LIMIT 1
    );

-- Get the names of people who made a call of less than 1 minute on the day of crime
SELECT
    name
FROM
    people
    JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE
    day = "28"
    AND month = "7"
    AND year = "2021"
    AND duration < "60";

-- Take the intersections of all cases to get the name of the thief
SELECT
    name
FROM
    people
    JOIN passengers ON people.passport_number = passengers.passport_number
WHERE
    flight_id = (
        SELECT
            id
        FROM
            flights
        WHERE
            day = "29"
            AND month = "7"
            AND year = "2021"
        ORDER BY
            hour, minute
        LIMIT 1
    )
INTERSECT
SELECT
    DISTINCT name
FROM
    people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE
    day = "28"
    AND month = "7"
    AND year = "2021"
    AND transaction_type = "withdraw"
    AND atm_location = "Leggett Street"
INTERSECT
SELECT
    name
FROM
    people
    JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE
    day = "28"
    AND month = "7"
    AND year = "2021"
    AND duration < "60"
INTERSECT
SELECT
    name
FROM
    people
    JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE
    day = "28"
    AND month = "7"
    AND year = "2021"
    AND hour = "10"
    AND minute >= "10"
    AND minute <= "25"
    AND activity = "exit";

-- Get the destiny
SELECT
    city
FROM
    airports
WHERE
    id = (
    SELECT
        destination_airport_id
    FROM
        flights
    WHERE
        day = "29"
        AND month = "7"
        AND year = "2021"
    ORDER BY
        hour, minute
    LIMIT 1
    );

-- Get the accomplice
SELECT
    name
FROM
    people
    JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE
    day = "28"
    AND month = "7"
    AND year = "2021"
    AND duration < "60"
    AND caller = (
        SELECT
            phone_number
        FROM
            people
        WHERE
            name = "Bruce"
    );
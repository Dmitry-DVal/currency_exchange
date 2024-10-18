get_exchange_rate = """SELECT
        er.ID AS exchange_rate_id,

        bc.ID AS base_currency_id,
        bc.FullName AS base_currency_name,
        bc.Code AS base_currency_code,
        bc.Sign  AS base_currency_sign,

        tc.ID AS target_currency_id,
        tc.FullName AS target_currency_name,
        tc.Code AS target_currency_code,
        tc.Sign As target_currency_sign,

        er.Rate

        FROM exchange_rates AS er
        JOIN currencies AS bc ON er.BaseCurrencyId = bc.ID
        JOIN currencies AS tc ON er.TargetCurrencyId = tc.ID
        WHERE base_currency_code == ? AND target_currency_code == ?"""


get_currency = "SELECT ID, Fullname, Code, Sign FROM currencies WHERE Code = ?"

add_currency = "INSERT INTO currencies (Code, Fullname, Sign) VALUES (?, ?, ?)"

get_exchange_rates = """SELECT
    er.ID AS exchange_rate_id,

    bc.ID AS base_currency_id,
    bc.FullName AS base_currency_name,
    bc.Code AS base_currency_code,
    bc.Sign  AS base_currency_sign,

    tc.ID AS target_currency_id,
    tc.FullName AS target_currency_name,
    tc.Code AS target_currency_code,
    tc.Sign As target_currency_sign,

    er.Rate

    FROM exchange_rates AS er
    JOIN currencies AS bc ON er.BaseCurrencyId = bc.ID
    JOIN currencies AS tc ON er.TargetCurrencyId = tc.ID"""


update_exchange_rate = """UPDATE exchange_rates 
        SET 
            Rate = ?
        WHERE BaseCurrencyId = (SELECT ID FROM currencies WHERE Code = ?)
        AND TargetCurrencyId = (SELECT ID FROM currencies WHERE Code = ?)"""
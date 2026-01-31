select
    order_id,
    customer_id,
    order_date,
    order_amount,
    currency
from {{ source('raw', 'orders') }}

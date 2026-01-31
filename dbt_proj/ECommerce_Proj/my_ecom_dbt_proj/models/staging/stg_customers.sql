select
    customer_id,
    name as customer_name,
    email
from {{ source('raw', 'customers') }}
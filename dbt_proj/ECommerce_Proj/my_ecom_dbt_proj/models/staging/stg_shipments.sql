select
    shipment_id,
    order_id,
    status,
    shipped_at,
    delivered_at
from {{ source('raw', 'shipments') }}
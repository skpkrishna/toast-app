from common.db import Database

class Orders():
    order_value_discount = { 1000 : 2, 1500 : 2.5, 2000: 3, 5000: 5}
    item_qty_discount = { 10 : 2, 15: 2.5, 20 : 3, 30 : 5}
    def __init__(self):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.table_name = table_name
        self.order_items = order_items
        self.order_total_items = order_total_items
        self.order_total_qty = order_total_qty
        self.order_status_code = order_status_code
        self.order_billing_address = order_billing_address
        self.order_shipping_address = order_shipping_address
        self.order_payment_mode = order_payment_mode
        self.order_total_price = order_total_price
        self.order_net_price = order_net_price
        self.created_at = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') if created_at is None else created_at
        self.updated_at = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.order_checkedout_at = order_checkedout_at
        self.order_delivered_at = order_delivered_at
        self.order_completed_at = order_completed_at
        self.order_placed_at = order_placed_at
        self.order_paid_at = order_paid_at

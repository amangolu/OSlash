products = {
    'TSHIRT': {'price': 1000, 'discount': 10, 'max_quantity': 2},
    'NOTEBOOK': {'price': 200, 'discount': 20, 'max_quantity': 3},
    'JACKET': {'price': 2000, 'discount': 5, 'max_quantity': 2},
    'CAP': {'price': 500, 'discount': 20, 'max_quantity': 2},
    'PENS': {'price': 300, 'discount': 10, 'max_quantity': 3},
    'MARKER': {'price': 500, 'discount': 5, 'max_quantity': 3},
}
purchases = {}
def add_item(name, quantity):
  if name in products:
    if quantity > products[name]['max_quantity']:
      print("ERROR_QUANTITY_EXCEEDED")
    else:
      if name in purchases:
        purchases[name]['quantity'] += quantity
      else:
        purchases[name] = {'quantity': quantity}
      print("ITEM_ADDED")
def print_bill():
  total_amount = 0
  total_discount = 0
  for name, details in purchases.items():
    price = products[name]['price']
    discount = products[name]['discount']
    quantity = details['quantity']
    amount = price * quantity
    total_amount += amount
    if total_amount > 1000:
      total_discount += (discount/100) * amount
  if total_amount > 3000:
    total_discount += (5/100) * total_amount
  total_amount_to_pay = total_amount - total_discount
  sales_tax = (10/100) * total_amount_to_pay
  total_amount_to_pay += sales_tax
  print(f"TOTAL_DISCOUNT {total_discount:.2f}")
  print(f"TOTAL_AMOUNT_TO_PAY {total_amount_to_pay:.2f}")
add_item('TSHIRT', 2)
add_item('NOTEBOOK', 1)
print_bill()
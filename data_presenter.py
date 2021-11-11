cupcake_invoices = open('CupcakeInvoices.csv')
# print(cupcake_invoices)

invoice_sum = 0

for row in cupcake_invoices:
    row = row.strip()
    row = row.split(',')
    row[3] = float(row[3])
    row[4] = float(row[4])
    invoice = row[3] * row[4]
    invoice_sum = invoice + invoice_sum

invoice_sum = round(invoice_sum, 2)
print(invoice_sum)

cupcake_invoices.close()

import matplotlib.pyplot as plt
import numpy as np

cupcake_invoices = open('CupcakeInvoices.csv')
# print(cupcake_invoices)

invoice_sum = 0
invoice_list = []
labels = ['Chocolate', 'Vanilla', 'Strawberry']
chocolate_amount = []
chocolate_index = []

vanilla_amount = []
vanilla_index = []

strawberry_amount = []
strawberry_index = []

x = np.arange(len(labels))
width = 0.25

index = 0
for row in cupcake_invoices:
    row = row.strip()
    row = row.split(',')
    if row[2] == 'Chocolate':
        chocolate_amount.append(row[3])
        chocolate_index.append(index)
        index += 1
    elif row[2] == 'Vanilla':
        vanilla_amount.append(row[3])
        vanilla_index.append(index)
        index += 1
    elif row[2] == 'Strawberry':
        strawberry_amount.append(row[3])
        strawberry_index.append(index)
        index += 1
    # row[3] = float(row[3])
    # row[4] = float(row[4])
    # invoice = row[3] * row[4]
    # invoice_list.append(invoice)
    # invoice_sum = invoice + invoice_sum
print(chocolate_amount, chocolate_index)
print(vanilla_amount, vanilla_index)
print(strawberry_amount, strawberry_index)

plt.ylabel('Amount sold')
plt.xlabel('Customer Index')
plt.xlabel('??')

plt.plot(chocolate_index, chocolate_amount)
plt.plot(vanilla_index, vanilla_amount, 'red')
plt.plot(strawberry_index, strawberry_amount, 'green')

plt.show()

cupcake_invoices.close()
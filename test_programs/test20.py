from xml.dom.minidom import Element


def bubble_sort(elements, key):
    elements_len= len(elements)
    swapped = False
    for i in range(elements_len):
        for j in range(elements_len - 1 - i):
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j][key]
                elements[j][key] = elements[j+1][key]
                elements[j+1][key] = temp
                swapped = True
        if not swapped:
            break
    return elements

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

print(bubble_sort(elements, "name"))
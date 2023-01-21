import csv

# loading the data in from csv
def load_data():

    # open csv
    with open("currys-vacuum-cleaners.csv", 'r') as file:
        csvreader = csv.reader(file)
        counter = 0
        data = []
        for row in csvreader:
            if counter == 0:
                headers = row
                counter += 1
            else:
                data.append(row)
        
        return headers, data

# getting list of the products names            
def get_products(data):

    products = []
    product_info = []

    for row in data:

        product_name = row[2]
        products.append(product_name)
 
    set_products = set(products)

    return set_products, products

# getting the specs
def get_specs(data, products):

    specs = []

    for name in products:
        specs.append([])
    
    counter = 0

    for product in products:

        for row in data:

            if row[2] == product:
                specs[counter].append(row[10])
        
        counter += 1
        
    # removing new lines from original data
    stripped_specs = [[x.replace("\n\n", ': ') for x in l] for l in specs]
    stripped_specs = [[x.replace("\n-", ' and') for x in l] for l in stripped_specs]
    return stripped_specs

######## NOT BEING USED #######
def product_info(data, products):

    product_info = []
    output = []

    for row in data:
        product_info.append([])
    
    counter = 0
    for row in data:
        product_information = row[0:10]
        product_info[counter] = product_information
        counter += 1
  
    counter = 0
    previous_row = data[0][1:10]
    
    for row in data:
        
        if row[1:10] == previous_row:

            output.append(row[0:10])
            previous_row = row[0:10]

# numbering repeated products        
def ID_data(data):

    previous_name = data[0][2]
    counter = 0

    for row in data:

        name = row[2]      

        if name != previous_name:

            row[0] = 1
            previous_name = name
            counter = 1

        else:
            counter += 1
            row[0] = counter
        
    return data

# deleting repeated products (not listed 1)
def delete_duplicates(data):
    
    slim_data = []
    #specs = []

    counter = 0
    for row in data:

        if row[0] == 1:
            
            slim_data.append(row[0:10])
            
            if counter != 0:
                for item in specs:
                    slim_data[counter - 1].append(item)                   
            

            specs = []
            specs.append(row[10])
            counter += 1

        else:
            specs.append(row[10])

    #print(slim_data[0])    
    stripped_data = [[str(x).replace("\n\n", ': ') for x in l] for l in slim_data]
    stripped_data = [[x.replace("\n- ", '-') for x in l] for l in stripped_data]
    stripped_data = [[str(x).replace("\n", ': ') for x in l] for l in slim_data]
    stripped_data = [[x.replace(": - ", ':-') for x in l] for l in stripped_data]

    return stripped_data
                   
def write_csv (headers, data):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

def write_manufacturers(headers, data):

    headers[1] = "Manufacturer"
    headers[2] = "Product Name"

    for row in data:
        
        string = row[2]
        all_words = string.split()
        manufacturer = all_words[0]
        
        row[1] = manufacturer
    
    return headers, data


headers, data = load_data()
#set_products, products = get_products(data)
#specs = get_specs(data, set_products)
IDed_data = ID_data(data)
slim_data = delete_duplicates(data)



headers, data = write_manufacturers(headers, slim_data)

write_csv(headers, data)



    


    
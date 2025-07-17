from flask import Flask, request, jsonify          # type: ignore
import os
app = Flask(__name__)

# In-memory "database" (list  )
products = [
    
    {
        "id": 1,
        "company": "Mahindra" ,
        "name": "Thar",
        "Fuel": "Deisel",
        "Engiene": "2.2L",
        "Model": "3 door",
        "Differential": "4*4" ,
        "Power": "130bhp",
        "Torque": "300Nm",
        "Seating": "4",
        "Mileage": "15kmpl",
        "TopSpeed": "150kmph",
        "Acceleration": "0-100 in 10s",
        "Brakes": "Disc",
        "Suspension": "Independent",
        "Tyres": "18 inch",
        "GroundClearance": "226mm",
        "Length": "3985mm",
        "Width": "1855mm",
        "Height": "1844mm",
        "Wheelbase": "2450mm",
        "BootSpace": "380L",
        "FuelTankCapacity": "57L",
        "Airbags": "2",
        "ABS": "Yes",
        "ParkingSensors": "Yes",
        "Sunroof": "Yes",
        "price": 1800000,
        "image": "https://images.firstpost.com/wp-content/uploads/2020/10/thar-1280.jpg"
    },
    {
        "id": 2,
        "company": "Mahindra" ,
        "name": "Scorpio",
        "Model": "S11",
        "Fuel" : "Deisel",
        "Engiene": "2.2L",
        "Differential": "4*2" ,
        "Power":"140bhp",
        "Torque": "300Nm",
        "Seating": "7",
        "Mileage": "15kmpl",
        "TopSpeed": "150kmph",
        "Acceleration": "0-100 in 10s",
        "Brakes": "Disc",
        "Suspension": "Independent",
        "Tyres": "18 inch",
        "GroundClearance": "226mm",
        "Length": "4285mm",
        "Width": "1855mm",
        "Height": "2844mm",
        "Wheelbase": "2450mm",
        "BootSpace": "280L",
        "FuelTankCapacity": "57L",
        "Airbags": "4",
        "ABS": "No",
        "ParkingSensors": "Yes",
        "Sunroof": "No",
        "price": 2000000,
        "image": "https://content.carlelo.com/uploads/model/mahindra-scorpio-classic-1.webp"
    },
    {
        "id": 3,
        "company": "Mahindra" ,
        "name": "Scorpio",
        "Model": "N",
        "Fuel": "Deisel",
        "Engiene": "2.2L",
        "Differential": "4*4" ,
        "Power": "120bhp",
        "Torque": "250Nm",
        "Seating": "7",
        "Mileage": "12kmpl",
        "TopSpeed": "180kmph",
        "Acceleration": "0-100 in 9s",
        "Brakes": "Disc",
        "Suspension": "Independent",
        "Tyres": "19 inch",
        "GroundClearance": "226mm",
        "Length": "3985mm",
        "Width": "1855mm",
        "Height": "1844mm",
        "Wheelbase": "2450mm",
        "BootSpace": "380L",
        "FuelTankCapacity": "60L",
        "Airbags": "4",
        "ABS": "Yes",
        "ParkingSensors": "Yes",
        "Sunroof": "Yes",
        "price": 2800000,
        "image": "https://www.carscoops.com/wp-content/uploads/2022/05/Mahindra-Scorpio-N-main-1024x555.jpg"
    },
    {
        "id": 4,
        "company": "Toyota" ,
        "name": "Fortuner",
        "Fuel": "Deisel",
        "Engiene": "2.6L",
        "Model": "S11",
        "Differential": "4*4" ,
        "Power": "150bhp",
        "Torque": "300Nm",
        "Seating": "7",
        "Mileage": "9kmpl",
        "TopSpeed": "180kmph",
        "Acceleration": "0-100 in 8s",
        "Brakes": "Disc",
        "Suspension": "Independent",
        "Tyres": "20 inch",
        "GroundClearance": "226mm",
        "Length": "3885mm",
        "Width": "1855mm",
        "Height": "1844mm",
        "Wheelbase": "2450mm",
        "BootSpace": "180L",
        "FuelTankCapacity": "80L",
        "Airbags": "5",
        "ABS": "Yes",
        "ParkingSensors": "Yes",
        "Sunroof": "No",
        "price": 5500000,
        "image": "https://img.autotrader.co.za/9635110"
    },
    {
        "id": 5,
        "company": "Ford" ,
        "name": "Endeavour",
        "Model": "Titanium",
        "Fuel": "Deisel",
        "Engiene": "3.2L",
        "Differential": "4*4" ,
        "Power": "330bhp",
        "Torque": "550Nm",
        "Seating": "8",
        "Mileage": "8kmpl",
        "TopSpeed": "220kmph",
        "Acceleration": "0-100 in 6s",
        "Brakes": "Disc",
        "Suspension": "Independent",
        "Tyres": "22 inch",
        "GroundClearance": "266mm",
        "Length": "3995mm",
        "Width": "1875mm",
        "Height": "1864mm",
        "Wheelbase": "2550mm",
        "BootSpace": "180L",
        "FuelTankCapacity": "87L",
        "Airbags": "6",
        "ABS": "Yes",
        "ParkingSensors": "Yes",
        "Sunroof": "Yes",
        "price": 4500000,
        "image": "https://th.bing.com/th/id/OIP.w3TAcnUaJdaSqUQ7LDhZlAHaG3?rs=1&pid=ImgDetMain"
    },
]

# GET - To fecth all products 
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


# GET - To fetch the specific product by id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


# POST - To add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()  # JSON data client se lega
    products.append(new_product)
    return jsonify(new_product), 201


# PUT - To update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.get_json()
    for i, product in enumerate(products):
        if product['id'] == product_id:
            products[i] = updated_product
            return jsonify(updated_product)
    return jsonify({"error": "Product not found"}), 404


# DELETE - To delete a product by id
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for i, product in enumerate(products):
        if product['id'] == product_id:
            del products[i]
            return '', 204
    return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))                              # For providing Render PORT 
    app.run(host='0.0.0.0', port=port, debug=True)
    

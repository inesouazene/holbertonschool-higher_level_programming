from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


def read_csv(file_path):
    data = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        try:
            products = read_json('products.json')
        except Exception as e:
            error = "Error reading JSON file."
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except Exception as e:
            error = "Error reading CSV file."
    else:
        error = "Wrong source"

    if product_id:
        product_id = int(product_id)
        products = [product for product in products
                    if product['id'] == product_id]
        if not products:
            error = "Product not found"

    return render_template('product_display.html',
                           products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

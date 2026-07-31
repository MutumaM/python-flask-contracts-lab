#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    # Scan the list for a dict whose "id" matches the one in the URL
    contract = next((c for c in contracts if c["id"] == id), None)

    if contract is None:
        return make_response({"error": "Contract not found"}, 404)

    return make_response(contract, 200)


@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    # customers is just a plain list of strings, so a simple "in" check works
    if customer_name not in customers:
        return make_response({"error": "Customer not found"}, 404)

    # 204 must return an empty body — an empty string, not a dict
    return make_response('', 204)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

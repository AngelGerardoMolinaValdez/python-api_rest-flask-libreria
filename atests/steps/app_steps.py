from behave import when, then
import requests

@when('I send a GET request to "{path}"')
def step_when_i_send_a_get_request_to_path(context, path):
    response = requests.get(f'http://localhost:5000{path}', auth=("admin", "1234"))
    context.get_all_response = response

@then('I should receive a 200 status code of all products')
def step_then_i_should_receive_a_200_status_code(context):
    assert context.get_all_response.status_code == 200


@when('I send a POST request to "{path}" with the following product')
def step_when_i_send_a_post_request_to_path_with_the_following_product(context, path):
    product = {
        "name": context.table[0][0],
        "category": context.table[0][1],
        "stock": context.table[0][2]
    }
    print(product)
    response = requests.post(f'http://localhost:5000{path}', json=product, auth=("admin", "1234"))
    context.create_response = response

@then('I should receive a 201 status code')
def step_then_i_should_receive_a_201_status_code(context):
    assert context.create_response.status_code == 201


@when('I send a GET request to "{path}" to specify the product')
def step_when_i_send_a_get_request_to_path(context, path):
    response = requests.get(f'http://localhost:5000{path}', auth=("admin", "1234"))
    context.get_product_response = response

@then('I should receive a 200 status code of the product')
def step_then_i_should_receive_a_200_status_code(context):
    assert context.get_product_response.status_code == 200


@when('I send a PUT request to "{path}" with the following product')
def step_when_i_send_a_put_request_to_path_with_the_following_product(context, path):
    product = {
        "name": context.table[0][0],
        "category": context.table[0][1],
        "stock": context.table[0][2]
    }
    response = requests.put(f'http://localhost:5000{path}', json=product, auth=("admin", "1234"))
    context.update_response = response

@then('I should receive a 200 status code of the product updated')
def step_then_i_should_receive_a_200_status_code(context):
    assert context.update_response.status_code == 200


@when('I send a DELETE request to "{path}"')
def step_when_i_send_a_delete_request_to_path(context, path):
    response = requests.delete(f'http://localhost:5000{path}', auth=("admin", "1234"))
    context.delete_response = response

@then('I should receive a 200 status code of the product deleted')
def step_then_i_should_receive_a_204_status_code(context):
    assert context.delete_response.status_code == 200
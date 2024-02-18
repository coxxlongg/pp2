import json

file_path = '/mnt/data/sample-data.json'

with open(file_path, 'r') as file:
    data = json.load(file)

data_slice = data[:3] if isinstance(data, list) else data 
data_slice

def format_interface_status(data):
    header = f"{'Interface Status':^80}"
    separator = "=" * 80
    column_titles = f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}"
    print(f"{header}\n{separator}\n{column_titles}\n{'-' * 80}")

    # Iterate through each item in the 'imdata' list
    for item in data['imdata']:
        # Extract the necessary attributes
        attributes = item['l1PhysIf']['attributes']
        dn = attributes.get('dn', '')
        descr = attributes.get('descr', '')
        speed = attributes.get('speed', '')
        mtu = attributes.get('mtu', '')

        # Print each row of data
        print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")

# Call the function with the loaded JSON data
format_interface_status(data)

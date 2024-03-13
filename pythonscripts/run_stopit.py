'''This program is here to stop running multall and to still save the intermediate results.'''

def stopit():
    with open('stopit.txt', 'r') as file:
        content = file.read()

    # Replace "0" with "1"
    content = content.replace('0', '1')

    # Write the updated content back to the file
    with open('stopit.txt', 'w') as file:
        file.write(content)

if __name__ == '__main__':
    stopit()
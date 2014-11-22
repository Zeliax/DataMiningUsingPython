# -*- coding: utf-8 -*-
import json


def main():
    """
    Main function that does what the module says
    """
    text = open('requirements.txt', 'r')

    packages = []
    for line in text:
        packages.append(line.split('==')[0])

    text.close()

    json_data = open('projectproposal.json')
    data = json.load(json_data)
    modules = data.get('modules')
    json_data.close()

    for package in packages:
        if package not in modules:
            modules.append(package)

    new_modules = {'modules': modules}
    data.update(new_modules)

    with open('projectproposal.json', 'w') as jsonfile:
        json.dump(data, jsonfile)

if __name__ == '__main__':
    main()

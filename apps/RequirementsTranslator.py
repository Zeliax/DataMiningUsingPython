# -*- coding: utf-8 -*-
import json


def main():
    text = open('requirements.txt', 'r')
    for line in text:
        packages = line.split('==')[0]
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

    with open('projectproposal.json', 'w') as f:
        json.dump(data, f)

    if __name__ == '__main__':
        main()

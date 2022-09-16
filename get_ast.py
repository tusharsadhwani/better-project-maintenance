import ast

with open('code.py') as f:
    code = f.read()

tree = ast.parse(code)
print(ast.dump(tree, indent=4))

def execute_code(code):
    variables = {}

    for line in code.split("\n"):
        line = line.strip()
        if not line:
            continue

        print(f"Processing: {line}")  # DEBUG PRINT

        try:
            if line.startswith("PRINT "):  
                expr = line[6:].strip()
                print(f"Evaluating: {expr}")  # DEBUG PRINT
                compiled_expr = compile(expr, "<string>", "eval")
                print(eval(compiled_expr, {}, variables))

            elif line.startswith("SET "):  
                parts = line[4:].split("=")
                if len(parts) != 2:
                    raise SyntaxError("Invalid SET syntax. Use: SET var = value")

                var_name = parts[0].strip()
                expression = parts[1].strip()
                compiled_expr = compile(expression, "<string>", "eval")
                result = eval(compiled_expr, {}, variables)
                variables[var_name] = result

                print(f"Variable Set: {var_name} = {result}")  # DEBUG PRINT

            elif line.startswith("ADD "):  
                parts = line[4:].split(",")
                if len(parts) != 2:
                    raise SyntaxError("Invalid ADD syntax. Use: ADD x, y")

                var_name = parts[0].strip()
                expression = parts[1].strip()

                if var_name not in variables:
                    raise NameError(f"Variable '{var_name}' not defined")

                compiled_expr = compile(expression, "<string>", "eval")
                result = eval(compiled_expr, {}, variables)
                variables[var_name] += result

                print(f"Added {result} to {var_name}, New Value: {variables[var_name]}")  # DEBUG PRINT

            else:
                print(f"Unknown command: {line}")

        except Exception as e:
            print(f"Error in line '{line}': {e}")


if __name__ == "__main__":
    print("Simple DSL Compiler")
    print("Commands: PRINT <expr>, SET <var> = <value>, ADD <var>, <value>")
    print("Example:")
    print("  SET x = 10")
    print("  ADD x, 5")
    print("  PRINT x")
    print("Type 'exit' to quit.\n")

    code_lines = []
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "exit":
            break
        code_lines.append(user_input)

    execute_code("\n".join(code_lines))

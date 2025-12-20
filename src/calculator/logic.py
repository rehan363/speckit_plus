import re

class InvalidExpressionError(Exception):
    """Custom exception for invalid mathematical expressions."""
    pass

def evaluate(expression: str) -> float:
    expression = expression.replace(" ", "")
    if not expression:
        raise InvalidExpressionError("Empty expression")

    # Tokenize the expression, including parentheses
    tokens = [token for token in re.split(r'([\+\-\*\/()])', expression) if token]

    # Handle parentheses using a stack-based approach, not recursion on string segments
    values_stack = []
    ops_stack = []

    def apply_op():
        op = ops_stack.pop()
        right = values_stack.pop()
        
        # Handle unary operators if needed, though our logic avoids them on the stack
        if op in ['+', '-', '*', '/']:
            if not values_stack:
                 raise InvalidExpressionError("Invalid expression for binary operator")
            left = values_stack.pop()

            if op == '+': values_stack.append(left + right)
            elif op == '-': values_stack.append(left - right)
            elif op == '*': values_stack.append(left * right)
            elif op == '/':
                if right == 0: raise ZeroDivisionError("Division by zero")
                values_stack.append(left / right)

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # Handle numbers, including negative numbers at the start of an expression or sub-expression
        if token.replace('.', '', 1).lstrip('-').isdigit():
            # Unary minus handling
            if token.startswith('-') and (i == 0 or tokens[i-1] in precedence or tokens[i-1] == '('):
                values_stack.append(float(token))
            # Regular numbers
            else:
                 # Check for cases like 5-3, where split gives '5', '-', '3'
                if i > 0 and tokens[i-1] == '-':
                    # Check if it is a binary operation
                    if i > 1 and tokens[i-2] not in precedence and tokens[i-2] != '(':
                         values_stack.append(float(token))
                    else: # It's part of a negative number
                         values_stack.append(float(tokens[i-1] + token))
                         ops_stack.pop() # remove the '-' that was added
                else:
                    values_stack.append(float(token))

        elif token == '(':
            ops_stack.append(token)
        elif token == ')':
            while ops_stack and ops_stack[-1] != '(':
                apply_op()
            if not ops_stack or ops_stack.pop() != '(':
                raise InvalidExpressionError("Mismatched parentheses")
        
        elif token in precedence:
            # Distinguish between binary and unary minus
            is_unary = (token == '-') and (i == 0 or tokens[i-1] in precedence or tokens[i-1] == '(')

            if is_unary:
                # This is a unary minus, treat it as a high-precedence operation
                # A simple way is to handle it as '0 - number' later, but let's try a direct approach
                # We expect a number to follow. Let's peek ahead.
                if i + 1 < len(tokens) and tokens[i+1].replace('.', '', 1).isdigit():
                    values_stack.append(float(tokens[i] + tokens[i+1]))
                    i += 1 #  We consumed the next token
                else:
                    raise InvalidExpressionError("Invalid unary minus")
            else: # Binary operator
                while (ops_stack and ops_stack[-1] != '(' and 
                       precedence.get(ops_stack[-1], 0) >= precedence[token]):
                    apply_op()
                ops_stack.append(token)
        else:
             raise InvalidExpressionError(f"Invalid token: {token}")
        
        i += 1


    while ops_stack:
        apply_op()

    if len(values_stack) != 1 or ops_stack:
        raise InvalidExpressionError("Malformed expression")

    return values_stack[0]




# Written by Eric Martin for COMP9021

'''Valid terms are inductively defined as variables
or expressions of the form f(t_1, ... ,t_n)
where n >=0 and f is an n-ary function symbol
(in case n = 0, f is a constant).

Variables and function symbols consist of
alphanumeric characters and underscores.
Variables start with an uppercase letter or an underscore.
Functions symbols start with a lowercase letter.

Whenever a term is output, it is "nicely formatted"
in that a single space is inserted after and only after a comma.
'''

def variables(term):
    '''
    >>> variables('x')
    set()
    >>> variables('X')
    {'X'}
    >>> variables('f(X, a, X)')
    {'X'}
    >>> variables('f(X_0, Y, X_0)') == {'Y', 'X_0'}
    True
    >>> (variables('f(c, f(X, f(a, Z, b), f(f(X, Z, U), a, T)), f(a, U, a))')
    ...                                                == {'U', 'T', 'X', 'Z'})
    True
    '''
    variables = set()
    in_word = False
    in_variable = False
    for c in term:
        if c in ',() ':
            in_word = False
            if in_variable:
                variables.add(variable)
                in_variable = False
        elif not in_word:
            in_word = True
            if c.isupper() or c == '_':
                in_variable = True
                variable = c
        elif in_variable:
            variable += c
    # Case where term is a variable
    if in_variable:
        variables.add(variable)
    return variables
            

def rename_variables(term_1, term_2):
    '''
    returns term_2 where all variables that occur
    in both term_1 and term_2 have been renamed
    to new variables.
    
    >>> rename_variables('a', 'a')
    'a'
    >>> rename_variables('X', 'Y')
    'Y'
    >>> rename_variables('X', 'X')
    'X_0'
    >>> rename_variables('f(a, X, Y)', 'g(b,   Y,Z, Y)')
    'g(b, Y_0, Z, Y_0)'
    >>> rename_variables('f(a, X,  g( Y, b), h  ( h(h(Z))))',
    ...                  'h(h(f(U,Y,  g (Z,  Z)) ))')
    'h(h(f(U, Y_0, g(Z_0, Z_0))))'
    '''
    variables_1 = variables(term_1)
    variables_2 = variables(term_2)
    substitutions = {}
    # Any variable Var that occurs in both term_1 and term_2
    # will be renamed to Var_i where i is the least natural number
    # that makes Var_i a new variable (that is, occurring neither
    # in term_1 nor in term_2 nor in the set of variables
    # that have been created so far, if any).
    for variable in variables_1 & variables_2:
        i = 0
        while variable + '_' + str(i) in variables_1 | variables_2:
            i += 1
        substitutions[variable] = variable + '_' + str(i)
    return nicely_formatted(substitute(term_2, substitutions))
            

def tokens(term):
    '''Returns a decomposition of term as a list of
    commas, opening parentheses, closing parentheses,
    function symbols, and variables.
    >>> tokens('h( f(a1,   U_0))')
    ['h', '(', 'f', '(', 'a1', ',', 'U_0', ')', ')']
    '''
    term = term.replace(' ', '')
    tokens = []
    word = ''
    for c in term:
        if c in ',()':
            if word:
                tokens.append(word)
                word = ''
            tokens.append(c)
        else:
            word += c
    # Case where term is a variable or a constant.
    if word:
        tokens.append(word)
    return tokens


def substitute(term, substitutions):
    '''
    >>> substitute('f(a, X , g(Y,  b), h(h(h(Z))))', {'X': 'X_0', 'Z': 'Z_0'})
    'f(a, X_0, g(Y, b), h(h(h(Z_0))))'
    >>> substitute('h(h(f(U,Y,   g(Z , Z))))', {'Z': 'ZZZ'})
    'h(h(f(U, Y, g(ZZZ, ZZZ))))'
    '''
    term_tokens = tokens(term)
    for i in range(len(term_tokens)):
        if term_tokens[i] in substitutions:
            term_tokens[i] = substitutions[term_tokens[i]]
    return nicely_formatted(''.join(term_tokens))


def unify(term_1, term_2):
    '''
    Returns a most general unifier of term_1 and term_2 if one exists,
    in the form of a dictionnary whose keys are variables and
    whose values are the terms that should be substituted
    for the associated variables; otherwise returns False.
    
    >>> unify('X', 'X')
    {}
    >>> unify('X', 'a')
    {'X': 'a'}
    >>> unify('X', 'Y') == {'X': 'Y'} or unify('X', 'Y') == {'Y': 'X'}
    True
    >>> (unify('f(X, Y)', 'f(Y, X)') == {'X': 'Y'} or
    ...               unify('f(X, Y)', 'f(Y, X)') == {'Y': 'X'})
    True
    >>> unify('f(X1, h(X1), X2)', 'f(g(X3), X4, X3)') == {'X4': 'h(X1)',
    ... 'X2': 'X3', 'X1': 'g(X3)'} or unify('f(X1, h(X1), X2)',
    ...  'f(g(X3), X4, X3)') == {'X4': 'h(g(X3))', 'X2': 'X3', 'X1': 'g(X3)'}
    True
    >>> unifier = unify('f(X1 ,g(X2, X3), X2, b)',
    ...                          'f(g(h(a, X5), X2), X1, h(a, X4), X4)')
    >>> for _ in range(len(unifier)):
    ...           unifier = {variable: substitute(unifier[variable], unifier)
    ...                  for variable in unifier}
    >>> unifier == {'X3': 'h(a, b)', 'X1': 'g(h(a, b), h(a, b))',
    ...                                'X4': 'b', 'X5': 'b', 'X2': 'h(a, b)'}
    True
    >>> unify('f(X, Y, U)', 'f(Y, U, g(X))')
    False
    '''
    return unify_identities([[term_1, term_2]])


def unify_identities(identities):
    assignments = {}
    while identities:
        term_1, term_2 = identities.pop()
        if term_1 == term_2:
            continue
        # Identify of the form: Variable = term
        if is_variable(term_1):
            # Occurrence check (omitted in most Prolog implementations)
            if term_1 in tokens(term_2):
                return False
            assignments[term_1] = term_2
            # Replace all occurrences of term_1 by term_2
            # in all terms in identities
            for identity in identities:
                for i in range(2):
                    identity[i] = substitute(identity[i], {term_1: term_2})
            continue
        # Identify of the form: term = Variable
        # Transform into: Variable = term
        if is_variable(term_2):
            identities.append([term_2, term_1])
            continue
        # Identify of the form: f(t_1, ..., t_n) = g(t'_1, ..., t'_m)
        # f and g should be identical, n and m should be equal.
        decomposition_1 = parse(term_1)
        decomposition_2 = parse(term_2)
        if decomposition_1[0] != decomposition_2[0] or\
                        len(decomposition_1) != len(decomposition_2):
            return False
        # Then add the identities t_1 = t'_1, ..., t_n = t'_n
        for i in range(1, len(decomposition_1)):
            identities.append([decomposition_1[i], decomposition_2[i]])
    return assignments


def check_validity(term):
    '''
    >>> check_validity('x_12')
    True
    >>> check_validity('X')
    True
    >>> check_validity('_alpha')
    True
    >>> check_validity('sum(Two, three)')
    True
    >>> check_validity('f(g_1(a, B, c), g_2(A_, _4, pib))')
    True
    >>> check_validity('g(_, fun(fun(fun(fun(g(X, b))))), X)')
    True
    >>> check_validity('f(c, f(X, f(a, Z, b), f(f(X, Z, U), a, T)), f(a, U, a))'
    ...               )
    True
    >>> check_validity('2')
    False
    >>> check_validity('()')
    False
    >>> check_validity('Sum(Two, Three)')
    False
    >>> check_validity('f(g(a, b, c)), d)')
    False
    >>> check_validity('g(a, b, )')
    False
    '''
    term = term.replace(' ', '')
    if not term:
        return False
    # A term is built from alphanumeric characters, underscores,
    # commas, and parentheses.
    if any(not c.isalnum() and c not in '_,()' for c in term):
        return False
    # When we find an opening parenthesis, we increment
    # non_closed_opening_parentheses_nb.
    # When we find a closing parenthesis, we decrement
    # non_closed_opening_parentheses_nb.
    # non_closed_opening_parentheses_nb should never become negative
    # and in case it becomes nonnull, then it should eventually
    # become null with no symbol following.
    non_closed_opening_parentheses_nb = 0
    has_parentheses = False
    start_of_token = term[0]
    # A term starts with a letter or an underscore.
    if start_of_token.isnumeric() or start_of_token in ',()':
        return False 
    for c in term[1: ]:
        # Do not want to read a character
        # after all opening parentheses have been closed.
        if has_parentheses and non_closed_opening_parentheses_nb == 0:
            return False
        # Reading a variable or function symbol beyond its first symbol.
        if c not in ',()' and start_of_token not in ',()':
            continue
        # A comma should follow a term or a closing parenthesis.
        if c == ',' and (start_of_token.isnumeric() or start_of_token in ',('):
             return False           
        if c == '(':
            has_parentheses = True
            non_closed_opening_parentheses_nb += 1
            # An opening parenthesis should follow a function symbol.
            if not start_of_token.islower():
                return False
        elif c == ')':
            non_closed_opening_parentheses_nb -= 1
            # A closing parenthesis should close an opening parenthesis
            # and follow a term or a closing parenthesis.
            if non_closed_opening_parentheses_nb < 0 or\
                        start_of_token.isnumeric() or\
                        start_of_token in ',(':
                return False
        start_of_token = c
    if non_closed_opening_parentheses_nb:
        return False
    return True
            
    
def parse(term):
    '''With term of the form f(t_1, ..., t_n), returns
    [f, t_1, ..., t_n]

    >>> parse('x_12')
    ['x_12']
    >>> parse('X')
    ['X']
    >>> parse('_alpha')
    ['_alpha']
    >>> parse('sum(Two,  three)')
    ['sum', 'Two', 'three']
    >>> parse('f(g_1( a , B, c), g_2(A_,   _4, pib))')
    ['f', 'g_1(a, B, c)', 'g_2(A_, _4, pib)']
    >>> parse('g(_, fun(  fun  ( fun(fun(g(  X,b))))), X)')
    ['g', '_', 'fun(fun(fun(fun(g(X, b)))))', 'X']
    '''
    term = term.replace(' ', '')
    words = []
    word = ''
    non_closed_opening_parentheses_nb = 0
    for c in term:
        # word is t_1 or ... or t_{n-1} from f(t_1, ..., t_n)
        if c == ',' and non_closed_opening_parentheses_nb == 1:
            words.append(nicely_formatted(word))
            word = ''
        elif c == '(':
            # word is f from f(t_1, ..., t_n)
            if non_closed_opening_parentheses_nb == 0:
                words.append(word)
                word = ''
            else:                
                word += '('
            non_closed_opening_parentheses_nb += 1
        elif c == ')':
            non_closed_opening_parentheses_nb -= 1
            if non_closed_opening_parentheses_nb:
                    word += ')'
        else:
            word += c
    # word is t_n from f(t_1, ..., t_n)
    # or the whole term in case it is a constant or a variable.
    words.append(nicely_formatted(word))
    return words


def is_variable(term):
    return term[0].isupper() or term[0] == '_' 


def nicely_formatted(term):
    return term.replace(' ', '').replace(',', ', ')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

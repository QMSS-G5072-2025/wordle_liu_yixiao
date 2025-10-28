from wordle_yl5929.wordle_yl5929 import validate_guess, check_guess

def test_validate_guess():
    """
    Test whether the validate_guess function correctly validate the input:
    - returns True for valid guesses
    - returns False for invalid guesses and edge cases
    """
    valid_guesses = ['heart', 'spray', 'chair']
    for v in valid_guesses:
        assert validate_guess(v), f"Expected valid guesses to pass"

    invalid_guesses = ['corn', 'butterfly', 'PEACE', 'Phone', 'p?per', '54321']
    for i in invalid_guesses:
        assert validate_guess(i) == False, f"Expected invalid guesses to fail"

    edge_cases = ['', None, 13.5, 8]
    for e in edge_cases:
        assert validate_guess(e) == False, f"Expected edge cases to fail"


def test_check_guess_basic():
    """
    Test the check_guess function, ensuring it returns correct color hints for the input
    - return all green for perfect matches
    - return all gray for no matches
    - return a correct mixture of color hints for mixed matching status
    - return an empty string for input with length different from length of the secrete word
    """
    perfect_match = check_guess("light", "light")
    pm_expected = [('l', 'green'), ('i', 'green'), ('g', 'green'), ('h', 'green'), ('t', 'green')]
    assert perfect_match == pm_expected

    no_matches = check_guess("peace", "fight")
    nm_expected = [('f', 'gray'), ('i', 'gray'), ('g', 'gray'), ('h', 'gray'), ('t', 'gray')]
    assert no_matches == nm_expected

    mixed = check_guess('heart', 'train')
    mixed_expected = [('t', 'yellow'), ('r', 'yellow'), ('a', 'green'), 
                      ('i', 'gray'), ('n', 'gray')]
    assert mixed == mixed_expected

    edge_case = check_guess('peace', 'stream')
    edge_expected = []
    assert edge_case == edge_expected
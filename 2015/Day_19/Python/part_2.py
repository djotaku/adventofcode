molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

step_1 = molecule.replace("Rn", '(')
step_2 = step_1.replace('Ar', ')')
step_3 = step_2.replace('Y', ',')

print(step_3)

left_parens = step_3.count("(")
right_parens = step_3.count(")")
commas = step_3.count(",")
# total = len(step_3)
total = step_3.count("Al") + step_3.count("B") + step_3.count("Ca") + step_3.count("F") + step_3.count("H") + step_3.count("Mg") + step_3.count("N") + step_3.count("O") + step_3.count("P") + step_3.count("Si") + step_3.count("Th") + step_3.count("Ti") + left_parens + right_parens + commas

# the formula I based this off of https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju?utm_source=share&utm_medium=web2x&context=3
# would have worked except I had an extra "C" at the beginning of my file, so I had to not subtract the 1 at the end and
# I got the right answer

equation = total - (left_parens + right_parens) - (2 * commas)

print(equation)


# 347 is too high.... (may need to break up the other tokens so that Si is counted as 1, not 2 tokens.
# 211 is too low - I think I need to add an extra one for the extra C at the beginning of my molecule and that was right!

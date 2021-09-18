molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

step_1 = molecule.replace("Rn", '(')
step_2 = step_1.replace('Ar', ')')
step_3 = step_2.replace('Y', ',')

print(step_3)

# I think next count length, then count each for the parens and commas
# See if that gets you the number. If Not, may need to do some work to figure out how else to break up tokens
total = len(step_3)
left_parens = step_3.count("(")
right_parens = step_3.count(")")
commas = step_3.count(",")

equation = total - (left_parens + right_parens) - (3 * commas) - 1

print(equation)


# 347 is too high.... (may need to break up the other tokens so that Si is counted as 1, not 2 tokens.

# coding=utf8
from postcodeValidator import postcodeValidator

validator = postcodeValidator()

#Invalid Postcodes
validator.outputValidity("$%± ()()")
validator.outputValidity("XX XXX")
validator.outputValidity("A1 9A")
validator.outputValidity("LS44PL")
validator.outputValidity("Q1A 9AA")
validator.outputValidity("V1A 9AA")
validator.outputValidity("X1A 9BB")
validator.outputValidity("LI10 3QP")
validator.outputValidity("LJ10 3QP")
validator.outputValidity("LZ10 3QP")
validator.outputValidity("A9Q 9AA")
validator.outputValidity("AA9C 9AA")
validator.outputValidity("FY10 4PL")
validator.outputValidity("SO1 4QQ")

#Valid Postcodes
validator.outputValidity("EC1A 1BB")
validator.outputValidity("W1A 0AX")
validator.outputValidity("M1 1AE")
validator.outputValidity("B33 8TH")
validator.outputValidity("CR2 6XH")
validator.outputValidity("DN55 1PT")
validator.outputValidity("GIR 0AA")
validator.outputValidity("SO10 9AA")
validator.outputValidity("FY9 9AA")
validator.outputValidity("WC1A 9AA")
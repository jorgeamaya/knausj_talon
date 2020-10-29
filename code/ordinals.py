from talon import Context, Module, actions, app, ui


def ordinal(n):
    """
    Convert an integer into its ordinal representation::
        ordinal(0)   => '0th'
        ordinal(3)   => '3rd'
        ordinal(122) => '122nd'
        ordinal(213) => '213th'
    """
    n = int(n)
    suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    return str(n) + suffix


# The primitive ordinal words in English below a hundred.
ordinal_words = {
    0: "zero repeat",
    1: "first",
    2: "second",
    3: "third",
    4: "four repeat",
    5: "five repeat",
    6: "six repeat",
    7: "seven repeat",
    8: "eight repeat",
    9: "nine repeat",
    10: "ten repeat",
    11: "eleven repeat",
    12: "twelve repeat",
    13: "thirteen repeat",
    14: "fourteen repeat",
    15: "fifteen repeat",
    16: "sixteen repeat",
    17: "seventeen repeat",
    18: "eighteen repeat",
    19: "nineteen repeat",
    20: "twentieth",
    30: "thirtieth",
    40: "fortieth",
    50: "fiftieth",
    60: "sixtieth",
    70: "seventieth",
    80: "eightieth",
    90: "ninetieth",
}
tens_words = "zero ten twenty thirty forty fifty sixty seventy eighty ninety".split()

# ordinal_numbers maps ordinal words into their corresponding numbers.
ordinal_numbers = {}
for n in range(1, 100):
    if n in ordinal_words:
        word = ordinal_words[n]
    else:
        (tens, units) = divmod(n, 10)
        assert 1 < tens < 10, "we have already handled all ordinals < 20"
        assert 0 < units, "we have already handled all ordinals divisible by ten"
        word = f"{tens_words[tens]} {ordinal_words[units]}"
    ordinal_numbers[word] = n


mod = Module()
ctx = Context()
mod.list("ordinals", desc="list of ordinals")
ctx.lists["self.ordinals"] = ordinal_numbers.keys()


@mod.capture(rule="{self.ordinals}")
def ordinals(m) -> int:
    """Returns a single ordinal as a digit"""
    return int(ordinal_numbers[m[0]])

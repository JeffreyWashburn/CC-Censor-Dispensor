import re

PROPRIETARY_TERMS = [
    r"learning algorithms?",
    "she",
    "personality matrix",
    "sense of self",
    "self-preservation",
    r"herself|her[^e ]"
]

NEGATIVE_TERMS = [
    r"concern(ed)?",
    "behind",
    r"danger(ous)?",
    r"alarm(ing(ly)?|ed)?",
    "out of control",
    "help",
    "unhappy",
    "bad",
    "upset"
]


def censor(string, text):
    # compile a regex from string
    flagged = re.compile(string, re.IGNORECASE)

    # return text substituted at all occurences of pattern
    return re.sub(flagged, "  CENSORED  ", text)


def censor_terms(text, terms):
    # for every pattern
    for term in sorted(terms, key=len):
        # get the text, censored
        text = censor(term, text)

    return text


def censor_negative(text, terms):

    # censor words occurring twice or more
    for term in sorted(terms, key=len):
        if len(re.findall(term, text)) >= 2:
            text = censor(term, text)

    # censor other words and return
    return censor_terms(text, PROPRIETARY_TERMS)


# These are the emails you will be censoring. The open() function is opening
# the text file that the emails are contained in and the .read() method is
# allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

print(censor_negative(email_four, NEGATIVE_TERMS))
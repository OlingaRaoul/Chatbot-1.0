import difflib

def get_best_match(user_input, faq_dict):
    questions = list(faq_dict.keys())
    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if match:
        return faq_dict[match[0]]
    else:
        return "Sorry, I couldn't find an answer to that question."
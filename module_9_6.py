def all_variants(text):
    length = len(text)
    for subseq_length in range(1, length + 1):
        for start in range(length - subseq_length + 1):
            yield text[start: start + subseq_length]


a = all_variants("abc")
for i in a:
    print(i)
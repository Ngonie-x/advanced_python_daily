from collections import Counter
import csv

words = []

unwanted = {
    'the', 'and', 'a', 'at', 'in', 'of', 'to', 'be',
    'for', '*', 'is', 'with', 'will', 'that',
    'shall', 'all', 'on', 'as', 'are', 'their', 'by',
    'it', 'i.', 'has', 'such', 'its', 'an', 'any',
    'than', 'if', 'iii.', 'ii.', 'iv.', 'v.', 'them',
    'when', '-', 'we', 'do', '1.', 'no', 'a.', 'our',
    'but', 'b.', '?', '12', 'chapter', 'so', 'or', 'not',
    'from', 'this', 'may', 'have', 'other', 'who', 'must',
    'where', 'out', 'can', 'one', 'per', 'take', 'also', 'they'
}

with open('HR-POLICY-AFTER-BOARD-HR-COMMITTE-INPUT-28-Sept-2022-Working-Doc4.txt') as f:
    doc = f.read().split()

    my_counter = Counter(doc).most_common()

    with open('keywords.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        for i in my_counter:
            if i[0].lower() not in unwanted:
                writer.writerow([i[0], i[1]])

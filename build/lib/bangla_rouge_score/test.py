from rouge_score import rouge_scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True, lang="bengali")
scores = scorer.score('তোমার সাথে দেখা হয়ে ভালো লাগলো।', 'আপনার সাথে দেখা হয়ে ভালো লাগলো।')

print(scores)
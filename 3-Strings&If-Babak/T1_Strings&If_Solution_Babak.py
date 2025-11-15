text = input()

starts_with_upper = text[0].isupper() if text else False
ends_with_question = text.endswith('?') if text else False
length_gt_10 = len(text) > 10

print(f"- شروع با حرف بزرگ: {starts_with_upper}")
print(f"- پایان با علامت سؤال: {ends_with_question}")
print(f"- طول بیشتر از ۱۰ کاراکتر: {length_gt_10}")

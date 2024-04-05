eng_subs_no = int(input())
eng_subs = set(map(int, input().split()))
french_subs_no = int(input())
french_subs = set(map(int, input().split()))

print(len(eng_subs.difference(french_subs)))
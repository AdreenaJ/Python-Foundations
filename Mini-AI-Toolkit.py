import toolkit
#1.Data cleaning
dirty_data="  Hello World!   "
clean_data=toolkit.clean_text(dirty_data)
print(toolkit.format_text("Cleaned Text",clean_data))
#2.Statistics
scores=[]
try:
    limit=int(input("Enter limit:"))
    for i in range(0,limit):
        n=int(input("Enter number:"))
        scores.append(n)
except ValueError:
    print("Enter valid input!!")
basic_stats=toolkit.statistics(scores)
print(toolkit.format_text("Basic Math Stats",basic_stats))
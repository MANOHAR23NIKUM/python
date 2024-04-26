import patterns
print('__chosee the patterns__')
print('1.half_pyramid\n2.inverted_pyramid\n3.simple_patterns')
select = int(input('select 1/2/3 : '))
print(select)
def main():
    if (select == 1):
        ans = patterns.half_pyramid()
        print('half_pyramid')
    elif (select == 2): 
        ans = patterns.inverted_pyramid()
        print('inverted_pyramid ')
    elif (select == 3):
        ans = patterns.simple_pattern()
        print('simple_pattern')
    else:
        print('chosse 1/2/3')
if __name__=="__main__":
    main()
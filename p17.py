# this problem sucks
def int_to_words(n: int)->str:
    if n < 20:
        return ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][n]
    elif n < 100:
        s = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"][n//10-2]
        return s if n%10 == 0 else s + "-" + int_to_words(n%10)
    elif n < 1000:
        s = int_to_words(n//100) + " hundred"
        return s if n%100 == 0 else s + " and " + int_to_words(n%100)
    elif n < 1000000:
        s = int_to_words(n//1000) + " thousand"
        return s if n%1000 == 0 else s + " and " + int_to_words(n%1000)
    elif n < 1000000000:
        s = int_to_words(n//1000000) + " million"
        return s if n%1000000 == 0 else s + " and " + int_to_words(n%1000000)
    elif n < 1000000000000:
        s = int_to_words(n//1000000000) + " billion"
        return s if n%1000000000 == 0 else s + " and " + int_to_words(n%1000000000)
    elif n < 1000000000000000:
        s = int_to_words(n//1000000000000) + " trillion"
        return s if n%1000000000000 == 0 else s + " and " + int_to_words(n%1000000000000)
    return "Number too large"
print(sum(len(int_to_words(i).replace(" ", "").replace("-", "")) for i in range(1, 1001)))
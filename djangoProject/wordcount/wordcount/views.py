from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Home.html', {'name': 'Hrishi'})


def about(request):
    return render(request, 'about.html', {'age': 28, 'city': 'Pune'})


def contact(request):
    return render(request, 'contact.html', {'mobile': '+91 9658745214'})


def form(request):
    if request.method == "POST":
        a = int(request.POST.get("n1"))
        b = int(request.POST.get("n2"))
        opr = request.POST.get("opr")
        if opr == "Addition":
            ans = a + b
            return render(request, 'calculator.html', {'ans': ans})
        elif opr == "Subtraction":
            ans = a - b
            return render(request, 'calculator.html', {'ans': ans})
        elif opr == "Multiplication":
            ans = a * b
            return render(request, 'calculator.html', {'ans': ans})
        elif opr == "Division":
            ans = a / b
            return render(request, 'calculator.html', {'ans': ans})
    else:
        return render(request, 'calculator.html')


def word(request):
    if request.method == "POST":
        ck1 = request.POST.get("chk1", "off")
        ck2 = request.POST.get("chk2", "off")
        ck3 = request.POST.get("chk3", "off")
        ck4 = request.POST.get("chk4", "off")
        ck5 = request.POST.get("chk5", "off")
        ck6 = request.POST.get("chk6", "off")
        ck7 = request.POST.get("chk7", "off")
        ck8 = request.POST.get("chk8", "off")
        ck9 = request.POST.get("chk9", "off")
        ck10 = request.POST.get("chk10", "off")
        textarea = request.POST.get("textarea")
        if ck1 == "on":  # Show all Info
            return render(request, 'word.html', {'purpose': 'Display Data', 'info': textarea, 'd': textarea})
        if ck2 == "on":  # Word Count
            ws = textarea.split()
            wc = len(ws)
            return render(request, 'word.html', {'purpose': 'Word Count', 'info': wc, 'd': textarea})
        if ck3 == "on":  # Word Frequency
            ws = textarea.split()
            mydict = {}
            for i in ws:
                mydict.update({i: ws.count(i)})
            return render(request, 'word.html', {'purpose': 'Word Frequency', 'info': mydict, 'd': textarea})
        if ck4 == "on":  # Convert Text into Uppercase
            ws = textarea.split()
            list1 = []
            for i in ws:
                list1.append(i.upper())
            jlist = " ".join(list1)
            return render(request, 'word.html', {'purpose': 'Converted to UpperCase', 'info': jlist, 'd': textarea})
        if ck5 == "on":  # Remove Punctuations
            mylist = []
            mylist2 = []
            for i in textarea:
                mylist.append(i)
            for i in mylist:
                if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i == " ":
                    mylist2.append(i)
            str1 = "".join(mylist2)
            return render(request, 'word.html', {'purpose': 'Punctuation Removed', 'info': str1, 'd': textarea})
        if ck6 == "on":  # Count lines
            cnt = 0
            for i in textarea:
                if i == "\n":
                    cnt += 1
            return render(request, 'word.html', {'purpose': 'Number of Lines', 'info': cnt + 1, 'd': textarea})
        if ck7 == "on":  # Start with character
            ws = textarea.split()
            mylist = []
            for i in ws:
                if i[0] == 'L':
                    mylist.append(i)
            return render(request, 'word.html', {'purpose': 'Word starting with character', 'info': mylist, 'd': textarea})
        if ck8 == "on":  # Ends with character
            ws = textarea.split()
            mylist = []
            for i in ws:
                if i[-1] == 'm':
                    mylist.append(i)
            return render(request, 'word.html', {'purpose': 'Word ending with character', 'info': mylist, 'd': textarea})
        if ck9 == "on":  # contains vowel in it
            ws = textarea.split()
            mylist = []
            for i in ws:
                if 'a' in i or 'A' in i or 'e' in i or 'E' in i or 'i' in i or 'I' in i or 'o' in i or 'O' in i or 'u' in i or 'U' in i:
                    mylist.append(i)
            return render(request, 'word.html', {'purpose': 'Word containing vowel in it', 'info': mylist, 'd': textarea})
        if ck10 == "on":
            ws = textarea.split()
            mylist = []
            for i in ws:
                if 'a' not in i and 'A' not in i and 'e' not in i and 'E' not in i and 'i' not in i and 'I' not in i and 'o' not in i and 'O' not in i and 'u' not in i and 'U' not in i:
                    mylist.append(i)
            return render(request, 'word.html', {'purpose': 'Word not containing vowel in it', 'info': mylist, 'd': textarea})
        else:
            return HttpResponse("Error")
    else:
        return render(request, 'word.html')

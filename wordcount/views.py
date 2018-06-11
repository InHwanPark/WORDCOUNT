from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split()

    worddictionary = dict()
    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltest': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')
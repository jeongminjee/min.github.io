from django.shortcuts import render

# Create your views here.
def index(request):
        full_text = request.GET['fulltext']
    
        word_list = full_text.split()
    
        word_dictionary = {}
    
        for word in word_list:
            if word in word_dictionary:
                
                word_dictionary[word] += 1
            else:
                
                word_dictionary[word] = 1
    
        return render(request, 'index.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})



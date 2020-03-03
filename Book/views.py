from django.shortcuts import render
from django.http import HttpResponse
from Book.models import BookInfo, PeopleInfo


# Create your views here.
def index(request):
	context = {
		'H1': 'OK!',
		'H2': '-- By TeamsSix'
	}
	return render(request, 'index.html', context)


def booklist(request):
	book_list = BookInfo.objects.all()
	context = {
		'book_list': book_list
	}
	return render(request, 'booklist.html', context)


def peoplelist(request, book_id):
	book = BookInfo.objects.get(id=book_id)
	people_list = book.peopleinfo_set.all()
	context = {
		'people_list': people_list
	}
	return render(request, 'peoplelist.html', context)

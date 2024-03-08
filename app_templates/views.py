from django.shortcuts import render

# Create your views here.

def weekend(request):
	return render(request, 'index.html')

def uz_week(request):
	week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba','Yakshanba']
	return render(request, 'index_uz.html', context = {'week': week})

def en_week(request):
	week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
	['Понедельник вторник среда Четверг Пятница Суббота воскресенье']
	return render(request, 'index_en.html', context = {'week': week})

def ru_week(request):
	week = ['Понедельник', 'вторник', 'среда', 'Четверг', 'Пятница', 'Суббота', 'воскресенье']
	return render(request, 'index_ru.html', context = {'week': week})
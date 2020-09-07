from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
import math


def index(request):
	
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
			
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
			
			else:
				form.save()
		
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	
	form = CityForm()

	weather_data = []
	cities = City.objects.order_by()[::-1][:5]
	
	for city in cities:
		r = requests.get(url.format(city)).json()
		city_weather = {
			'city' : r['name'],
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
		}
		weather_data.append(city_weather)
	
	context = { 
		'weather_data' : weather_data,
		'form' : form,
		'message' : message,
		'message_class' : message_class, 
	}
	
	return render(request, 'check_weather/weather.html', context)

def searched_city(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
			
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
			
			else:
				form.save()
		
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	
	form = CityForm()

	searched_cities = []
	city = request.POST.get('name','')
	r = requests.get(url.format(city)).json()
	
	if r['cod'] == 200:
		city_weather = {
			'city' : r['name'],
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'pressure' : r['main']['pressure'],
			'humidity' : r['main']['humidity'],
			'wind' : r['wind']['speed'],
			'icon' : r['weather'][0]['icon'],
		}
		searched_cities.append(city_weather)
		
		context = { 
			'searched_cities' : searched_cities,
			'form' : form,
			'message' : message,
			'message_class' : message_class, 
		}
		
		return render(request, 'check_weather/searched_city.html', context)
	
	else:
		return redirect('home')

def seven_days(request):
	url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={}&units=metric&cnt=7&APPID=271d1234d3f497eed5b1d80a07b3fcd1"
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
			
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
			
			else:
				form.save()
		
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	
	form = CityForm()
	
	weather = []
	cities = City.objects.order_by()[::-1][:1]
	
	for city in cities:
		
		r = requests.get(url.format(city)).json()
		
		city_weather = {
			'city' : r['city']['name'],
			'day_one_temp' : r['list'][0]['temp']['day'],
			'night_one_temp' : r['list'][0]['temp']['night'],
			'max_one_temp' : r['list'][0]['temp']['max'],
			'min_one_temp' : r['list'][0]['temp']['min'],
			'one_desc' : r['list'][0]['weather'][0]['description'],
			'one_icon' : r['list'][0]['weather'][0]['icon'],
			'day_two_temp' : r['list'][1]['temp']['day'],
			'night_two_temp' : r['list'][1]['temp']['night'],
			'max_two_temp' : r['list'][1]['temp']['max'],
			'min_two_temp' : r['list'][1]['temp']['min'],
			'two_desc' : r['list'][1]['weather'][0]['description'],
			'two_icon' : r['list'][1]['weather'][0]['icon'],
			'day_three_temp' : r['list'][2]['temp']['day'],
			'night_three_temp' : r['list'][2]['temp']['night'],
			'max_three_temp' : r['list'][2]['temp']['max'],
			'min_three_temp' : r['list'][2]['temp']['min'],
			'three_desc' : r['list'][2]['weather'][0]['description'],
			'three_icon' : r['list'][2]['weather'][0]['icon'],
			'day_four_temp' : r['list'][3]['temp']['day'],
			'night_four_temp' : r['list'][3]['temp']['night'],
			'max_four_temp' : r['list'][3]['temp']['max'],
			'min_four_temp' : r['list'][3]['temp']['min'],
			'four_desc' : r['list'][3]['weather'][0]['description'],
			'four_icon' : r['list'][3]['weather'][0]['icon'],
			'day_five_temp' : r['list'][4]['temp']['day'],
			'night_five_temp' : r['list'][4]['temp']['night'],
			'max_five_temp' : r['list'][4]['temp']['max'],
			'min_five_temp' : r['list'][4]['temp']['min'],
			'five_desc' : r['list'][4]['weather'][0]['description'],
			'five_icon' : r['list'][4]['weather'][0]['icon'],
			'day_six_temp' : r['list'][5]['temp']['day'],
			'night_six_temp' : r['list'][5]['temp']['night'],
			'max_six_temp' : r['list'][5]['temp']['max'],
			'min_six_temp' : r['list'][5]['temp']['min'],
			'six_desc' : r['list'][5]['weather'][0]['description'],
			'six_icon' : r['list'][5]['weather'][0]['icon'],
			'day_seven_temp' : r['list'][6]['temp']['day'],
			'night_seven_temp' : r['list'][6]['temp']['night'],
			'max_seven_temp' : r['list'][6]['temp']['max'],
			'min_seven_temp' : r['list'][6]['temp']['min'],
			'seven_desc' : r['list'][6]['weather'][0]['description'],
			'seven_icon' : r['list'][6]['weather'][0]['icon'],
		}
		weather.append(city_weather)
		average = (float(weather[0]["day_one_temp"])+float(weather[0]["day_two_temp"])+float(weather[0]["day_three_temp"])+float(weather[0]["day_four_temp"])+float(weather[0]["day_five_temp"])+float(weather[0]["day_six_temp"])+float(weather[0]["day_seven_temp"]))/7
		average = math.ceil(average*100)/100
	
	context = {
		'average' : average,
		'weather' : weather,
		'form' : form,
	}
	
	return render(request, 'check_weather/seven_days.html', context)

def seven_days_farenheit(request):
	url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={}&units=imperial&cnt=7&APPID=271d1234d3f497eed5b1d80a07b3fcd1"
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
			
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
			
			else:
				form.save()
		
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	
	form = CityForm()
	
	weather = []
	cities = City.objects.order_by()[::-1][:1]
	
	for city in cities:
		
		r = requests.get(url.format(city)).json()
		
		city_weather = {
			'city' : r['city']['name'],
			'day_one_temp' : r['list'][0]['temp']['day'],
			'night_one_temp' : r['list'][0]['temp']['night'],
			'max_one_temp' : r['list'][0]['temp']['max'],
			'min_one_temp' : r['list'][0]['temp']['min'],
			'one_desc' : r['list'][0]['weather'][0]['description'],
			'one_icon' : r['list'][0]['weather'][0]['icon'],
			'day_two_temp' : r['list'][1]['temp']['day'],
			'night_two_temp' : r['list'][1]['temp']['night'],
			'max_two_temp' : r['list'][1]['temp']['max'],
			'min_two_temp' : r['list'][1]['temp']['min'],
			'two_desc' : r['list'][1]['weather'][0]['description'],
			'two_icon' : r['list'][1]['weather'][0]['icon'],
			'day_three_temp' : r['list'][2]['temp']['day'],
			'night_three_temp' : r['list'][2]['temp']['night'],
			'max_three_temp' : r['list'][2]['temp']['max'],
			'min_three_temp' : r['list'][2]['temp']['min'],
			'three_desc' : r['list'][2]['weather'][0]['description'],
			'three_icon' : r['list'][2]['weather'][0]['icon'],
			'day_four_temp' : r['list'][3]['temp']['day'],
			'night_four_temp' : r['list'][3]['temp']['night'],
			'max_four_temp' : r['list'][3]['temp']['max'],
			'min_four_temp' : r['list'][3]['temp']['min'],
			'four_desc' : r['list'][3]['weather'][0]['description'],
			'four_icon' : r['list'][3]['weather'][0]['icon'],
			'day_five_temp' : r['list'][4]['temp']['day'],
			'night_five_temp' : r['list'][4]['temp']['night'],
			'max_five_temp' : r['list'][4]['temp']['max'],
			'min_five_temp' : r['list'][4]['temp']['min'],
			'five_desc' : r['list'][4]['weather'][0]['description'],
			'five_icon' : r['list'][4]['weather'][0]['icon'],
			'day_six_temp' : r['list'][5]['temp']['day'],
			'night_six_temp' : r['list'][5]['temp']['night'],
			'max_six_temp' : r['list'][5]['temp']['max'],
			'min_six_temp' : r['list'][5]['temp']['min'],
			'six_desc' : r['list'][5]['weather'][0]['description'],
			'six_icon' : r['list'][5]['weather'][0]['icon'],
			'day_seven_temp' : r['list'][6]['temp']['day'],
			'night_seven_temp' : r['list'][6]['temp']['night'],
			'max_seven_temp' : r['list'][6]['temp']['max'],
			'min_seven_temp' : r['list'][6]['temp']['min'],
			'seven_desc' : r['list'][6]['weather'][0]['description'],
			'seven_icon' : r['list'][6]['weather'][0]['icon'],
		}
		
		weather.append(city_weather)
		average = (float(weather[0]["day_one_temp"])+float(weather[0]["day_two_temp"])+float(weather[0]["day_three_temp"])+float(weather[0]["day_four_temp"])+float(weather[0]["day_five_temp"])+float(weather[0]["day_six_temp"])+float(weather[0]["day_seven_temp"]))/7
		average = math.ceil(average*100)/100
	
	context = {
		'average' : average,
		'weather' : weather,
		'form' : form,
	}
	
	return render(request, 'check_weather/seven_days_farenheit.html', context)

def your_city(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
		
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
			
			else:
				form.save()
		
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	
	form = CityForm()

	ip_request = requests.get('https://get.geojs.io/v1/ip.json')
	my_ip = ip_request.json()['ip']
	geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
	geo_request = requests.get(geo_request_url)
	geo_data = geo_request.json()
	x = geo_data.get('city')
	
	if x:
		new_city = geo_data['city']
		r = requests.get(url.format(new_city)).json()
		searched_cities = []
		city_weather = {
			'city' : r['name'],
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'pressure' : r['main']['pressure'],
			'humidity' : r['main']['humidity'],
			'wind' : r['wind']['speed'],
			'icon' : r['weather'][0]['icon'],
		}
		
		searched_cities.append(city_weather)
		
		context = { 
			'searched_cities' : searched_cities,
			'form' : form,
			'message' : message,
			'message_class' : message_class, 
		}
		
		return render(request, 'check_weather/searched_city.html', context)
	
	else:
		
		return redirect('home')

def your_city_farenheit(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
	
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
	
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
	
			else:
				form.save()
	
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	
	form = CityForm()

	ip_request = requests.get('https://get.geojs.io/v1/ip.json')
	my_ip = ip_request.json()['ip']
	geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
	geo_request = requests.get(geo_request_url)
	geo_data = geo_request.json()
	x = geo_data.get('city')
	
	if x:
		new_city = geo_data['city']
		r = requests.get(url.format(new_city)).json()
		searched_cities = []
		city_weather = {
			'city' : r['name'],
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'pressure' : r['main']['pressure'],
			'humidity' : r['main']['humidity'],
			'wind' : r['wind']['speed'],
			'icon' : r['weather'][0]['icon'],
		}
	
		searched_cities.append(city_weather)
		context = { 
			'searched_cities' : searched_cities,
			'form' : form,
			'message' : message,
			'message_class' : message_class, 
		}
	
		return render(request, 'check_weather/farenheit.html', context)
	
	else:
	
		return redirect('farenheit_city')		

def signup(request):
	
	if request.method=="POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		
		if password1==password2:
		
			if User.objects.filter(username=username).exists():
				messages.info(request, "Username Taken")
		
				return redirect('signup')
		
			elif User.objects.filter(email=email).exists():
				messages.info(request, "Email Taken")
			
				return redirect('signup')
			
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save()
			
				return redirect('login')
		
		else:
			messages.info(request, "Password not matching")
		
			return redirect('signup')
	
	else:
	
		return render(request, 'check_weather/signup.html')

def login(request):
	
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
	
		if user is not None:
			auth.login(request, user)
	
			return redirect("home")
	
		else:
			messages.info(request, 'invalid credentials')
	
			return redirect("login")

	else:
		return render(request, 'check_weather/login.html')

def logout(request):
	auth.logout(request)
	return redirect("home")

def farenheit(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
	
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
	
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
	
			else:
				form.save()
	
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	
	form = CityForm()

	searched_cities = []
	city = request.POST.get('name','')
	r = requests.get(url.format(city)).json()
	
	if r['cod'] == 200:
		city_weather = {
			'city' : r['name'],
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'pressure' : r['main']['pressure'],
			'humidity' : r['main']['humidity'],
			'wind' : r['wind']['speed'],
			'icon' : r['weather'][0]['icon'],
		}
	
		searched_cities.append(city_weather)
	
		context = { 
			'searched_cities' : searched_cities,
			'form' : form,
			'message' : message,
			'message_class' : message_class, 
		}
		
		return render(request, 'check_weather/farenheit.html', context)
	
	else:
	
		return redirect('farenheit_city')	

def farenheit_city(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
	err_msg = ''
	message = ''
	message_class = ''
	
	if request.method == 'POST':
		form = CityForm(request.POST)
	
		if form.is_valid():
			new_city = form.cleaned_data['name']
			r = requests.get(url.format(new_city)).json()
	
			if r['cod']=='404':
				err_msg = 'City does not exist in the world!'
	
			else:
				form.save()
	
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
	form = CityForm()

	# weather_data = []
	# cities = City.objects.order_by()[::-1][:5]
	# for city in cities:
	# 	r = requests.get(url.format(city)).json()
	# 	city_weather = {
	# 		'city' : r['name'],
	# 		'temperature' : r['main']['temp'],
	# 		'description' : r['weather'][0]['description'],
	# 		'icon' : r['weather'][0]['icon'],
	# 	}
	# 	weather_data.append(city_weather)
	
	context = { 
	
		# 'weather_data' : weather_data,
		'form' : form,
		'message' : message,
		'message_class' : message_class, 
	}
	return render(request, 'check_weather/weather_farenheit.html', context)

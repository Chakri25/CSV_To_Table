from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Foo
from django.core.files import File
import csv
from datetime import datetime


# Create your views here.

def display(request):
	return(HttpResponse("<h2>Hello There</h2>"))


def data(request):
	data_instance = Foo.objects.create(name='test')
	return(HttpResponse("<h3>created "+data_instance.name+"</h3>"))
	

def file_data(request):
	file_name = open("D:/git/CSV_To_Table/UploadData_File/table.csv", newline='')
	reader = csv.reader(file_name)
	
	header_line = next(reader)
	data = []
	for row in reader:
		date = str(row[0])
		open_price = float(row[1])
		high = float(row[2])
		low = float(row[3])
		close = float(row[4])
		volume = float(row[5])
		adj_close = float(row[6])
		data.append([date, open_price,high, low, close, volume, adj_close])
	
	template = loader.get_template('main/table.html')
	context = {'header_line': header_line, 'data': data}
	return(HttpResponse(template.render(context, request)))
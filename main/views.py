
from django.shortcuts import render
from .charts import create_stock_chart


def home(request):
    chart = create_stock_chart()

    return render(request, 'index.html', {
        'stock_chart': chart
    })


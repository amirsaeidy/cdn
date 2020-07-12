from django.shortcuts import render
from django.http import HttpResponse

from .models import Symbols_Transactions,Symbols

from rest_framework import generics
from rest_framework import pagination

from .serializers import SymbolTransactionsSerializer,SymbolIDSerializer


# Create your views here.
# from .tasks import add,mul,xsum
from .models import Time

# def ExportRender(request):
    # return HttpResponse("<h1>{}</h1> - {} - {}".format(add(3,5),mul,xsum))

def TimeExporter(request):
    objs=Time.objects.all()
    print("Objectss",objs)
    if len(objs)>0:
        time_=list(objs)[-1]
    else:
        time_="-"
    print("Timeee",time_)
    return HttpResponse("{} time".format(time_))


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 10000



class SymbolsTransactionsAPIList(generics.ListAPIView):
    queryset=Symbols_Transactions.objects.all()#filter(timestamp__gte=datetime.now()-timedelta(days=15))
    serializer_class=SymbolTransactionsSerializer
    pagination_class = LargeResultsSetPagination

class SymbolIDAPIList(generics.ListAPIView):
    queryset=Symbols.objects.all()
    serializer_class=SymbolIDSerializer
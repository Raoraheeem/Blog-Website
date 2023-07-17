from django.http import HttpResponse
from django.shortcuts import render,redirect
from Food.models import Food
from mcdonalds.models import mcdonalds
from KFC.models import KFC
from HistoryAsia.models import HistoryAsia
from HistoryEurope.models import HistoryEurope
from HistoryAmerica.models import HistoryAmerica
from TravelAsia.models import TravelAsia
from TravelEurope.models import TravelEurope
from TravelAustralia.models import TravelAustralia
from Programing.models import Programing
from Physics.models import Physics
from Chemistry.models import Chemistry

def home(request):

    return render(request,'homepage.html')
def Education(request):
    ProgramingData=Programing.objects.all()
    PhysicsData=Physics.objects.all()
    ChemistryData=Chemistry.objects.all()
    data={
     'ProgramingData':ProgramingData,
     'PhysicsData':PhysicsData,
     'ChemistryData':ChemistryData
      
    }
    return render(request,'Education.html',data)
def Traveling(request):
    TravelAsiaData=TravelAsia.objects.all()
    TravelEuropeData=TravelEurope.objects.all()
    TravelAustraliaData=TravelAustralia.objects.all()
    data={
        'TravelAsiaData':TravelAsiaData,
        'TravelEuropeData':TravelEuropeData,
        'TravelAustraliaData':TravelAustraliaData
    }
    return render(request,'Travel.html',data)
def Foods(request):
    
    FoodData=Food.objects.all()
    mcdonaldsData=mcdonalds.objects.all()
    KFCData=KFC.objects.all()


    data={
        'FoodData':FoodData,
        'mcdonaldsData':mcdonaldsData,
        'KFCData':KFCData

    }
    return render(request,'Food.html',data)
def History(request):
    HistoryAsiaData=HistoryAsia.objects.all()
    HistoryEuropeData=HistoryEurope.objects.all()
    HistoryAmericaData=HistoryAmerica.objects.all()
    data={
        'HistoryAsiaData':HistoryAsiaData,
        'HistoryEuropeData':HistoryEuropeData,
         'HistoryAmericaData':HistoryAmericaData
        
    }
    return render(request,'History.html',data)


def Practice(request):
    return render(request,'Practice.html')
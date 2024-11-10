import csv
from django.core.management.base import BaseCommand
from world.models import CountryInfo
from django.conf import settings
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        csv_file_path = '/home/ubuntu/webmapping/geodjango_tutorial/world/data/countries of the world.csv'

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # clean data
                countryClean=row['Country'].strip()
                popDensityStr=row['Pop. Density (per sq. mi.)'].replace(',','.')
                if popDensityStr == '':
                    popDensityFloat = 0.0
                else:
                    popDensityFloat = float(popDensityStr)
                coastlineStr=row['Coastline (coast/area ratio)'].replace(',','.')
                if coastlineStr == '':
                    coastlineFloat = 0.0
                else:
                    coastlineFloat = float(coastlineStr)
                migrationStr=row['Net migration'].replace(',','.')
                if migrationStr == '':
                    migrationFloat = 0.0
                else:
                    migrationFloat = float(migrationStr)
                infantMortStr=row['Infant mortality (per 1000 births)'].replace(',','.')
                if infantMortStr == '':
                    infantMortFloat = 0.0
                else:
                    infantMortFloat = float(infantMortStr)
                gdp=row['GDP ($ per capita)']
                if gdp == '':
                    gdpClean = 0
                else:
                    gdpClean = gdp
                literacyStr=row['Literacy (%)'].replace(',','.')
                if literacyStr == '':
                    literacyFloat = 0.0
                else:
                    literacyFloat = float(literacyStr)
                phonesStr=row['Phones (per 1000)'].replace(',','.')
                if phonesStr == '':
                    phonesFloat = 0.0
                else:
                    phonesFloat = float(phonesStr)
                arableStr=row['Arable (%)'].replace(',','.')
                if arableStr == '':
                    arableFloat = 0.0
                else:
                    arableFloat = float(arableStr)
                cropsStr=row['Crops (%)'].replace(',','.')
                if cropsStr == '':
                    cropsFloat = 0.0
                else:
                    cropsFloat = float(cropsStr)
                otherStr=row['Other (%)'].replace(',','.')
                if otherStr == '':
                    otherFloat = 0.0
                else:
                    otherFloat = float(otherStr)
                climateStr=row['Climate'].replace(',','.')
                if climateStr == '':
                    climateFloat = 0.0
                else:
                    climateFloat = float(climateStr)
                birthrateStr=row['Birthrate'].replace(',','.')
                if birthrateStr == '':
                    birthrateFloat = 0.0
                else:
                    birthrateFloat = float(birthrateStr)
                deathrateStr=row['Deathrate'].replace(',','.')
                if deathrateStr == '':
                    deathrateFloat = 0.0
                else:
                    deathrateFloat = float(deathrateStr)
                agricultureStr=row['Agriculture'].replace(',','.')
                if agricultureStr == '':
                    agricultureFloat = 0.0
                else:
                    agricultureFloat = float(agricultureStr)
                industryStr=row['Industry'].replace(',','.')
                if industryStr == '':
                    industryFloat = 0.0
                else:
                    industryFloat = float(industryStr)
                serviceStr=row['Service'].replace(',','.')
                if serviceStr == '':
                    serviceFloat = 0.0
                else:
                    serviceFloat = float(serviceStr)

                CountryInfo.objects.create(
                    country=countryClean,
                    region=row['Region'],
                    population=row['Population'],
                    area=row['Area (sq. mi.)'],
                    popDensity=popDensityFloat,
                    coastline=coastlineFloat,
                    migration=migrationFloat,
                    infantMort=infantMortFloat,
                    gdp=gdpClean,
                    literacy=literacyFloat,
                    phones=phonesFloat,
                    arable=arableFloat,
                    crops=cropsFloat,
                    other=otherFloat,
                    climate=climateFloat,
                    birthrate=birthrateFloat,
                    deathrate=deathrateFloat,
                    agriculture=agricultureFloat,
                    industry=industryFloat,
                    service=serviceFloat
                )

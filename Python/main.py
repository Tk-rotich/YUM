import numpy as np
import pandas as pd

class Farmdata():
    def __init__(self):
        self.path   = "Sample.xlsx"
        self.data_file = self.getInput()
        self.sorted_biomass = self.sortByBiomass()
        self.sort_by_harvesting_date   = self.sortByHarvestingDate()
        

    def getInput(self):
        self.data_file = pd.read_excel(self.path)
        return self.data_file

    def sortFarmersData(self,sort_val,ascending=True):
        self.sorted_total_biomass = self.data_file.sort_values(sort_val,ascending=ascending)
        return self.sorted_total_biomass

    def sortByBiomass(self):
        sort_val    = 'Total biomass Fwt (kg)'
        ascending   = False
        sorted_data = self.sortFarmersData(sort_val,ascending)
        return sorted_data

    def sortByHarvestingDate(self):
        # sort_val    = 'Harvesting date'
        # self.data_file['Harvesting date'] =pd.to_datetime(self.datafile['Harvesting date'])
        
        # pd.to_datetime(self.data_file['Harvesting date'],format='%d%m%Y', errors='ignore')
        sorted_data = ''
        return sorted_data

    def getFarmerWithHighestBiomass(self):
        return self.sorted_biomass.head(n=1)

    def getNoOfPlantsHarvestMean(self):
        return self.data_file['No of plants harvest'].mean()

    def getFarmerWithLowestBiomass(self):
        return self.sorted_biomass.tail(n=1) 

    # def getFarmerWithLowestBiomass(self):
    #     return self.sort_by_harvesting_date()

    
if __name__ == "__main__":
    farm = Farmdata()

    # Output highest and lowest biomass
    highest_bio	=farm.getFarmerWithHighestBiomass()
    lowest_bio	=farm.getFarmerWithLowestBiomass()

    number_plants_means =farm.getNoOfPlantsHarvestMean()

    print(highest_bio)
    print(lowest_bio)
    print(number_plants_means)
    print(farm.sort_by_harvesting_date)

# ADRESS-PROJECT-BDCOE

1. This project aims at verifying the address from the dataset as valid and invalid with creating csv files for the earlier mentioned categories.
2. The logic behind veryfying address is that all the addresses must have pincode in integers where no integer can be greater than 9999999999. 
3. The pincode/postalcode cannot contain any string characters and zero values.
4. Python's geopy module is being used in this project to verify locations as on maps. 


# WORKING OF THE PROJECT 

1. Different Dataframes are created dropping null values, zero values. 
2. Mailing Streets, Cities are used as inputs for the geopy module which then veries address as on maps. 
3. In the end two files are created , Valid Address and Invalid Address satisfying the requirements. 

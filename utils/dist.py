from geopy import Point                                                                                                                                                                       
from geopy.distance import geodesic                                                                                                                                                           
                                                                                                                                                                                              
distKm = 1                                                                                                                                                                                    
lat1 = 35.68096477080332                                                                                                                                                                      
lon1 = 139.76720809936523                                                                                                                                                                     
                                                                                                                                                                                              
print('center', lat1, lon1)                                                                                                                                                                   
print('north', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 0).format_decimal())                                                                                                
print('east', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 90).format_decimal())                                                                                                
print('south', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 180).format_decimal())                                                                                              
print('west', geodesic(kilometers=distKm).destination(Point(lat1, lon1), 270).format_decimal()) 



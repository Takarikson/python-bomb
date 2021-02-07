# Bomba, ma na celu odlicznaie od 10 do 0, jeśli dochodzi do liczby 2 licznik zwalnia do 3 sekund(jak w filmach XD)
from time import sleep

# for arr in [10,9,8,7,6,5,4,3,2,1,0]:
#     print(arr)
#     sleep(1)
#     if arr <=2:
#         sleep(3)
# print('Boom!')

#inne rozwiązanie

for arr in [10,9,8,7,6,5,4,3,2,1,0]:
    print(arr)
    if arr <= 2:
        sleep(2)
    sleep(1)
    
print('Boom!')
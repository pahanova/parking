# Класс парковки. Содержит произвольное количество парковочных линий
class Parking: 
    def __init__(self, lines):
        self.lines = []
        for l in lines:
            self.lines.append(l)
    # Возвращяет верхушку выбранного стека(парковочной линии)
    def top(self, lineNumber):
        return self.lines[lineNumber].vehicles[len(self.lines[lineNumber].vehicles) - 1]
    # Находит, на какой линии находится машина с таким регистрационным номером.
    # Если такой регистрационный номер не найден, возвращает -1
    def find(self, registrationNumber):
        for i in range(0, len(self.lines)):
            for vehicle in self.lines[i].vehicles:
                if vehicle.registrationNumber == registrationNumber:
                    return i
        return -1
    # Метод добавления машины на выбранную линию парковки, если же там нет места, выводит сообщение с ошибкой
    def addVehicle(self, lineNumber, vehicle):
        lineNumber -= 1
        if (lineNumber >= 0) & (lineNumber < len(self.lines)):    
            if (len(self.lines[lineNumber].vehicles) != self.lines[lineNumber].capacity):
                if self.find(vehicle.registrationNumber) == -1:
                    vehicle.serialNumber = len(self.lines[lineNumber].vehicles) + 1
                    self.lines[lineNumber].vehicles.append(vehicle)
                else:
                    print("Ошибка: машина с таким регистрационным номером уже припаркована")
            else:
                print("Ошибка: на стоянке больше нет места")
        else:
            print("Ошибка: вы ввели неверный номер линии")
    # Метод вывода на экран всех машин на всех линиях
    def printVehicles(self):
        for i in range(0, len(self.lines)):
            print("Линия ", i + 1, ":")
            for v in self.lines[i].vehicles:
                print(" ", v.serialNumber,": ", v.registrationNumber)
    # Убирает с парковки машину с выбранным регистрационным номером, на какой бы линии она не находилась
    def pickupVehicle(self, registrationNumber):
        # Поиск линии, на котрой находится машина
        lineNumber = self.find(registrationNumber)
        if not(lineNumber == -1):
            print("Машина с регистрационным номером ", registrationNumber, " находится на линии", lineNumber + 1)
            subline = []
            # Удаление с линии машин, пока не найдем искомую
            while not(len(self.lines[lineNumber].vehicles) == 0):
                if self.top(lineNumber).registrationNumber == registrationNumber:
                    self.lines[lineNumber].vehicles.pop()
                    print("Машина с регистрационным номером ", registrationNumber, "покидает стоянку")
                    break
                print("Машина с регистрационным номером", self.top(lineNumber).registrationNumber, "выезжает c полосы", lineNumber + 1)
                subline.append(self.lines[lineNumber].vehicles.pop())
            # Вовращение на линию удаленных манин
            while not(len(subline) == 0):
                v = subline.pop()
                self.addVehicle(lineNumber + 1, v)  
                print("Машина с регистрационным номером", v.registrationNumber, "возращается на линию", lineNumber + 1)   
        else:
            print("Ошибка: машины с таким регистрационным номером на стоянке не найдено")

# Класс линии парковки. Содержит список машин и вместимость линии.  
class Line:
    def __init__(self, capacity):
        self.vehicles = []
        self.capacity = capacity
    def isFull(self):
        if (len(self.vehicles) == self.capacity):
            return True
        else:
            return False

# Класс машины. Содержит порядковый номер на линии и регистрационный номер машиы.
class Vehicle:
    def __init__(self, registrationNumber):
        self.serialNumber = 0
        self.registrationNumber = registrationNumber

# Метод вызова меню помощи.
def help():
    print("Функционал программы:")
    print("parking.addVehicle(lineNumber, vehicle) - добавляет маишну на выбранную линию")
    print("parking.printVehicles() - выводит список всех машин на парковке")
    print("parking.pickupVehicle(registrationNumber) - забрать с парковки машину с выбранным регистрационным номером")

line1 = Line(2)
line2 = Line(5)
Lines = []
Lines.append(line1)
Lines.append(line2)
parking = Parking(Lines)
parking.addVehicle(1,Vehicle("с065мк"))
parking.addVehicle(1,Vehicle("б113ав"))
parking.addVehicle(2,Vehicle("т098оп"))
parking.addVehicle(2,Vehicle("р458ка"))
parking.addVehicle(2,Vehicle("к250шо"))

loop = 0
lines = []
print("Выберите режим работы:")
print("1 - с готовыми данными")
print("2 - ручной ввод данных")
mode = input("> ")
if mode == "1":
    print("Type \"help()\" for help")
    while loop == 0:   
        eval(input("> "))
elif mode == "2":
    print("Введите количество линий: ", end = "")
    lineCount = input()
    for i in range(0,int(lineCount)):
        print("Введите вместимость линии ",i+1,":", end = "")
        capacity = input()
        lines.append(Line(capacity))
    parking = Parking(lines)
    print("Type \"help()\" for help")
    while loop == 0:   
        eval(input("> "))
else:
    print("Введен неверный номер. Программа завершена.")


    




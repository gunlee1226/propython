import dessertDAO as dao

d = int(input('The number you want to delete? :'))

dao.delete(d)

dao.select
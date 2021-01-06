def user(name, surname, year, city, email, phone):
	return f"Имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {phone}"
	
print(user(name = 'Иван', surname = 'Иванов', year = '1984', city = 'Москва', email = '123@us.com', phone = '765411231'))
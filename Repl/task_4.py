student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[0], student[-1])

name = student[:4]
surname = student[5:]
print(name)
print(surname)

print(student.upper())
print(student.lower())

initials = student[0] + "." + student[5] + "."
print(initials)

print(course[::-1])

percent = completed / total * 100
print("%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent))
print("{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent))
print(f"{student} — {course}: {completed}/{total} ({percent:.1f}%)")

symbol = "Я"
print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
encoded = symbol.encode("utf-8")
print(encoded)
print(len(encoded))

#student[0] = "О" (ошибочная строка)
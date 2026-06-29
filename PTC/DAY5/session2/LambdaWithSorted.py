students=[
    ("Netto",25),
    ("Manu",23),
    ("Kashi",30)
]
sorted_students=sorted(
    students,
    key=lambda x:x[1]
)
print(sorted_students)
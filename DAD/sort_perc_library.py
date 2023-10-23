

def CalculatePercentage(marks_obtained, total_marks):
    percentage = marks_obtained / total_marks * 100
    return percentage


# CalculatePercentage(30, 100)


def SortNames(names, order = "ascending"):

    if order == "ascending":
        return sorted(names)
    elif order == "descending":
        return sorted(names, reverse= True)
    else:
        raise ValueError("Invalid 'order'. Use ascending or decending.")


names = ["Alice", "Bob", "Lucy", "Hritik", "Sneha", "Manjeet"]
# SortNames(names, order= "descending")
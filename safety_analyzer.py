def calculate_safety(male,female):

    total = male + female

    if total == 0:
        return 0,"No People"

    female_ratio = female/total

    danger_score = int((1-female_ratio)*100)

    if danger_score > 80:
        status = "DANGEROUS"

    elif danger_score > 60:
        status = "HIGH RISK"

    elif danger_score > 40:
        status = "MODERATE"

    else:
        status = "SAFE"

    return danger_score,status
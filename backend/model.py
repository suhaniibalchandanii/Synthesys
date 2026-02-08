def business_feasibility(industry, market_size, competition, investment, growth_rate):
    """
    Realistic business feasibility logic
    Returns score (0–100) and insights
    """

    # Normalize inputs
    market_score = min(market_size / 1000, 1) * 30       # max 30 points
    growth_score = min(growth_rate / 20, 1) * 25         # max 25 points
    competition_score = (10 - competition) / 10 * 20     # max 20 points
    investment_score = min(investment / 500000, 1) * 15  # max 15 points

    # Industry bonus (smart logic)
    industry_bonus = {
        "tech": 10,
        "ai": 10,
        "healthcare": 8,
        "finance": 7,
        "ecommerce": 6,
        "education": 5
    }

    bonus = industry_bonus.get(industry.lower(), 3)

    score = market_score + growth_score + competition_score + investment_score + bonus

    # Cap score at 100
    score = min(score, 100)

    # Risk level
    if score > 75:
        risk = "Low Risk"
    elif score > 50:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    return {
        "score": round(score, 2),
        "risk": risk
    }

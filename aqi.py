def kategori_pm25(nilai: float) -> str:
    if nilai < 0:
        raise ValueError("PM2.5 tidak boleh negatif")
    if nilai <= 10:
        return "baik"
    if nilai <= 55.4:
        return "sedang"
    if nilai <= 150.4:
        return "tidak sehat"
    return "sangat tidak sehat"
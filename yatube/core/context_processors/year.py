from datetime import datetime


def year(request):
    """Добавляет переменную с текущим годом в контекст шаблона."""
    current_year = datetime.now().year
    return {"year": current_year}

import requests
import json
import os

# ------------------ PILOTOS ------------------

API_HEADERS_F1 = {
    "x-rapidapi-host": "f1-motorsport-data.p.rapidapi.com",
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY", "446877f9b9mshc55f822d3e625d8p1338c6jsnb35fb4773af3")
}

API_URL_ATHLETE = "https://f1-motorsport-data.p.rapidapi.com/athlete-info"
API_URL_RESULTS = "https://f1-motorsport-data.p.rapidapi.com/race-results"

def get_driver_info(driver_id):
    params = {"athleteId": driver_id}
    response = requests.get(API_URL_ATHLETE, headers=API_HEADERS_F1, params=params)
    if response.status_code == 200:
        return response.json()
    return None


def get_race_results(driver_id):
    params = {"driverId": driver_id}
    response = requests.get(API_URL_RESULTS, headers=API_HEADERS_F1, params=params)
    if response.status_code == 200:
        return response.json()
    return []

# ------------------ NOTICIAS ------------------

API_URL_NEWS = "https://f1-motorsport-data.p.rapidapi.com/news"

API_HEADERS_NEWS = {
    "x-rapidapi-host": "f1-motorsport-data.p.rapidapi.com",
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY", "446877f9b9mshc55f822d3e625d8p1338c6jsnb35fb4773af3")
}

def _normalize_local_item(it):
    """Normaliza un item del JSON local al formato {title, excerpt, image, url}"""
    if not isinstance(it, dict):
        return {"title": "", "excerpt": "", "image": "", "url": ""}
    title = it.get("headline") or it.get("title") or ""
    excerpt = it.get("description") or it.get("summary") or it.get("lead") or ""
    # sacar la primera imagen válida
    image = ""
    images = it.get("images") or it.get("image") or []
    if isinstance(images, list) and images:
        first = images[0]
        if isinstance(first, dict):
            image = first.get("url") or first.get("imageUrl") or ""
        elif isinstance(first, str):
            image = first
    url = it.get("link") or it.get("url") or it.get("sourceUrl") or ""
    return {"title": title, "excerpt": excerpt, "image": image, "url": url}

def get_f1_news():
    try:
        response = requests.get(API_URL_NEWS, headers=API_HEADERS_NEWS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            items = data.get("data", {}).get("items") or data.get("items") or data.get("news") or []
            normalized = []
            for it in items:
                # API remota: tratar de mapear a title/excerpt/image/url si vienen así
                title = it.get("title") or it.get("headline") or ""
                excerpt = it.get("excerpt") or it.get("summary") or it.get("description") or ""
                image = it.get("image") or it.get("imageUrl") or ""
                url = it.get("url") or it.get("link") or ""
                normalized.append({
                    "title": title,
                    "excerpt": excerpt,
                    "image": image,
                    "url": url
                })
            if normalized:
                print("✅ Noticias cargadas desde API")
                return normalized
        print("⚠️ API sin datos o sin items; usar fallback local")
    except Exception as e:
        print("❌ Error con API:", e)

    # Intentar cargar local_news.json en el mismo directorio del módulo
    base_path = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(base_path, "local_news.json"),
        os.path.join(base_path, "data", "noticias.json"),  # tu archivo está en noticias/data/noticias.json
        os.path.join(base_path, "noticias.json"),
    ]
    for local_file in candidates:
        if os.path.exists(local_file):
            try:
                with open(local_file, "r", encoding="utf-8") as f:
                    raw = json.load(f)
                    # raw puede ser lista o dict; obtener lista de items
                    items = raw if isinstance(raw, list) else (raw.get("data") or raw.get("items") or raw.get("news") or [])
                    normalized = []
                    for it in items:
                        normalized.append(_normalize_local_item(it))
                    print(f"✅ Noticias cargadas desde JSON local: {local_file} (items={len(normalized)})")
                    return normalized
            except Exception as e:
                print("❌ Error cargando JSON local", local_file, e)
    print("⚠️ No se encontró JSON local válido. Devuelve lista vacía.")
    return []

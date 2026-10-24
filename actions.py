from SimplerLLM.tools.rapid_api import RapidAPIClient
import requests

def get_seo_page_report(url: str):
    try:
        api_url = "https://seo-analyzer3.p.rapidapi.com/seo-audit-basic"
        api_params = {"url": url}

        print(f"Calling SEO API: {api_url}")

        api_client = RapidAPIClient()

        response = api_client.call_api(
            api_url=api_url,
            method="GET",
            params=api_params
        )

        return response
    
    except requests.exceptions.HTTPError as e:
        return {
            "error": str(e)
        }
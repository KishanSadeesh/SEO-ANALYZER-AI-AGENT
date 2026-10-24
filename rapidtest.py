from SimplerLLM.tools.rapid_api import RapidAPIClient


def get_seo_page_report(url: str):
    api_url = "https://site-seo-analyzer9.p.rapidapi.com/analysis.php"
    api_params = {"url": url}

    print(f"Calling SEO API: {api_url}")

    api_client = RapidAPIClient()

    print("API URL:", api_url)

    response = api_client.call_api(
        api_url=api_url,
        method="GET",
        params=api_params
    )

    return response

k = get_seo_page_report(
    "https://www.buildwithkishan.xyz/"
)
print(k)
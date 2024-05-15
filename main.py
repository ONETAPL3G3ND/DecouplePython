from decouple import config

def get_api_key():
    return config('API_KEY')


def get_database_url():
    return config('DATABASE_URL')


if __name__ == "__main__":
    print(get_api_key())
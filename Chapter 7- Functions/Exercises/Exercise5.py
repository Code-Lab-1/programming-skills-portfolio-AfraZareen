def describe_city(city, country = 'United Kingdom'):
    """Describe a city"""
    msg = f"{city} is in {country}."
    print(msg)
describe_city("London")
describe_city("Paris" , "Europe")
describe_city("Oxford")
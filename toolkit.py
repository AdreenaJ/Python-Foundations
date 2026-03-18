def clean_text(raw_value):
    """ Removes extra space and convert data to lower case """
    return raw_value.strip().lower()
def statistics(numbers):
    """ Returns dictionary with basic stats """
    """ checks whethers numbers is empty or not """
    if not numbers:
        return {"mean":0,"count":0}
    """ Finds mean if numbers is not empty """
    mean=sum(numbers)/len(numbers)
    return {
        "mean":mean,
        "count":len(numbers),
        "max":max(numbers)
    }
def format_text(name,value):
    return f"---[REPORT:{name}]---\nResult:{value}\n"
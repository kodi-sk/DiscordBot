def check_input_value(content, value):  # To check Input format for Google Search and Recent Searches
    length = len(value)
    space_err_msg = "Please check for the spaces"
    no_input_err_msg = "No input Provided"

    if len(content) == length:
        return no_input_err_msg, False  # Return Tuple with False, if there is some error message
    if content[length] != " ":
        return space_err_msg, False
    content = content[length + 1:]  # Removing first part from the message like !google from complete message.
    if not content:
        return no_input_err_msg, False
    return content, True  # else return true with the required string.

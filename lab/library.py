#Custom modules

#Custom input which does type casting and provide a custom prompt message
def user_input(cast_type,prompt_message):
    buffer=None
    if(cast_type=='i'):
        buffer=int(input("{}: ".format(prompt_message)))
    elif(cast_type=='f'):
        buffer=float(input("{}: ".format(prompt_message)))
    elif(cast_type=='s'):
        buffer=input("{}: ".format(prompt_message))

    return buffer



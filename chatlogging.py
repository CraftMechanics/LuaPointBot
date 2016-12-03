def cmdlog(message, status = ''):
    if status == 'login':
        print('Successfully Logged in.\n')
        return 0
    print("[{} {}] {}".format(message.author, message.channel, message.content))

    return 0

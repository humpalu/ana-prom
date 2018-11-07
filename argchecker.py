def argchecker(arglist):
        if len(arglist) > 2:
                print ('Too many args!')
                return False
	elif len(arglist) < 2:
		print ('Please add the correct path for the logfile')
		return False
        try:
                with open(arglist[1]) as testread:
                        print ('Log file is ready')

        except IOError as err:
                print ('Unavailable log file. Please check the log file is avaliable and readable')
                return False
        return True


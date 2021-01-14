class ParsingHelper(object):
    _hourStrings = ['hrs', 'hours', 'hour', 'h', 'hr']

    # '1 hour 50 mins' - > 110
    @staticmethod
    def stringTimeToMinutesInt(stringTime):
        totalMinutes = 0
        timeSplit = stringTime.split(' ')
        if timeSplit[1].lower() in ParsingHelper._hourStrings:
            totalMinutes += (int(timeSplit[0]) * 60)
            if len(timeSplit) > 3:
                totalMinutes += int(timeSplit[2])
        else:
            totalMinutes += int(timeSplit[0])
        return totalMinutes
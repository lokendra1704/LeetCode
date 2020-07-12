class Solution:
    def reformatDate(self, date: str) -> str:
        date, month, year = date.split()
        date = date[:-2]
        if int(date) < 10:
            date = "0" + date
        d = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        return "-".join([year, d[month], date])

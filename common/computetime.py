import logging


class Computetime:

    def __init__(self, year=2020, month=8, day=20):
        self.year = year
        self.month = month
        self.day = day

    def is_leap(self, year):
        """
        判断闰年,平年
        :param year:
        :return:
        """
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True

    def date_specification(self):
        """
        闰年: 2月29天
        平年: 2月28天
        :param year:
        :param month:
        :param day:
        :return:
        """
        if self.year > 0:
            if self.month >= 1 and self.month <= 12:
                if self.day <= 31:
                    if self.is_leap(self.year):
                        return 29
                    else:
                        return 28

    def date_days_count(self):
        """
        计算公式
        :return:
        """
        if self.year <= 0 or self.month >= 13 or self.month < 1:
            logging.warning("日期错误")
            return "日期错误"

        _day = self.date_specification()  # 返回2月份天数

        _lst = [31, _day, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        num_day = 0
        for i in range(self.month - 1):
            # logging.warning("遍历的月份index:", i)
            num_day += _lst[i]
        # logging.warning("需要加的天数:", self.day)
        total = num_day + self.day
        # logging.warning("遍历好的月份 + 输入天数{}:", num_day, self.day)
        return {"天数": total}

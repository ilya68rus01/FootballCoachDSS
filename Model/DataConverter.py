import numpy as np


class DataConverter:
    def convert(self, data):
        indicators = list()
        average_indicators = list()
        self.train_flag = True
        for i in range(int(np.size(data))):
            if i == 0:
                indicators.append(data[i])
            else:
                if self.train_flag:
                    self.train_flag = False
                    good_params = self.__calculate_stats__(params=data[i], isTrain=True)
                    average_indicators.append(good_params)
                else:
                    good_params = self.__calculate_stats__(params=data[i])
                    average_indicators.append(good_params)
        result = list()
        for i in range(int(np.size(average_indicators[0]))):
            sum = 0
            for j in range(int(np.shape(average_indicators)[0])):
                sum = sum + average_indicators[j][i]
            result.append(sum/int(np.shape(average_indicators)[0]))
        indicators.append(result)
        return indicators



    def __calculate_stats__(self, params, isTrain=False):
        calculated_params = list()
        coef = 1
        for skill_type, x, x_max in params:
            if not isTrain:
                coef = self.coefficient_calculation(skill_type, float(x_max))
            calculated_params.append(self.linear_normalizzation(float(x), float(x_max), coef))
        return calculated_params

    def linear_normalizzation(self, x, x_max, k=1):
        return x / x_max * 100 * k

    def coefficient_calculation(self, skill_type, value):
        if skill_type == "completion":
            if value < 5:
                return 0.6
            elif value > 6:
                return 1
            else:
                return 0.8
        elif skill_type == "long shots":
            if value < 3:
                return 0.6
            elif value > 4:
                return 1
            else:
                return 0.8
        elif skill_type == "awnings":
            if value < 3:
                return 0.6
            elif value > 4:
                return 1
            else:
                return 0.8
        elif skill_type == "dribbling":
            if value < 6:
                return 0.6
            elif value > 7:
                return 1
            else:
                return 0.8
        elif skill_type == "long pass":
            if value < 6:
                return 0.6
            elif value > 10:
                return 1
            else:
                return 0.8
        elif skill_type == "short pass":
            if value < 30:
                return 0.6
            elif value > 40:
                return 1
            else:
                return 0.8
        elif skill_type == "intercepts":
            if value < 3:
                return 0.6
            elif value > 4:
                return 1
            else:
                return 0.8
        elif skill_type == "head game":
            if value < 3:
                return 0.6
            elif value > 4:
                return 1
            else:
                return 0.8
        elif skill_type == "selection":
            if value < 5:
                return 0.6
            elif value > 6:
                return 1
            else:
                return 0.8
        elif skill_type == "tackle":
            if value < 4:
                return 0.6
            elif value > 5:
                return 1
            else:
                return 0.8
        else:
            return 1


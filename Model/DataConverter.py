import numpy as np


class DataConverter:
    def convert(self, data):
        indicators = list()
        average_indicators = list()
        for i in range(int(np.size(data))):
            if i == 0:
                indicators.append(data[i])
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

    def __calculate_stats__(self, params):
        calculated_params = list()
        # if np.size(params) > 8:
        for x, x_max in params:
            calculated_params.append(self.linear_normalizzation(int(x), int(x_max)))
        return calculated_params

    def linear_normalizzation(self, x, x_max):
        return x / x_max * 100
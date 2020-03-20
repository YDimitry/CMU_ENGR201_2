# def sma(price, k):
#     return [None]*(k-1) + list(map(compose(flip(truediv)(k), sum),sliding_window(k,price)))


# def recommendation(sma_fast, sma_slow):
#     """buying (b) if the negative result of the signal sma_fast - sma_slow changes the symbol from negative (-) to positive (+).
#        selling (s) if the negative result of the signal sma_fast - sma_slow changes the symbol from positive (+) to negative (-).
#         dormant (h) if no trading signal occurs as above"""
#     result = []
#     for i in range(len(sma_fast)):
#         if not all([sma_slow[i], sma_fast[i], sma_slow[i-1], sma_fast[i-1]]):
#             result.append('h')
#         else:
#             from_negative = sma_fast[i-1] - sma_slow[i-1] < 0
#             from_positive = sma_fast[i-1] - sma_slow[i-1] > 0
#             to_negative = sma_fast[i] - sma_slow[i] < 0
#             to_positive = sma_fast[i] - sma_slow[i] > 0
#
#             if from_negative and to_positive:
#                 result.append('b')
#             elif from_positive and to_negative:
#                 result.append('s')
#             else:
#                 result.append('h')
#     return result


# def myDistance(u, a, t):
#     return u * t + a * pow(t,2) / 2
#
# def myVelocity(u, a, s):
#     return pow((pow(u,2)+2*a*s),0.5)

# def getPricePlusVAT(code, price):
#     d = {'TH': 0.07, 'UK': 0.2, 'FI': 0.24, 'SE': 0.24}
#     t = d.get(code)
#     return t and price*(1+t) or -1
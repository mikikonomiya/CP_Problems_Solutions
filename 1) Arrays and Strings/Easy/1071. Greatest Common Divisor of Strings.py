'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """ 
        def recursive_function(short_str, long_str, initial_short):
            if len(short_str) == 1:
                if long_str == short_str * len(long_str) and initial_short == short_str * len(initial_short):
                    return  short_str
                return ""
            ratio = len(long_str) // len(short_str)
            ratio_initial_short = len(initial_short) // len(short_str)
            if long_str == short_str * ratio and initial_short == short_str * ratio_initial_short:
                return short_str
            return recursive_function(long_str, short_str[:len(short_str)-1], initial_short)

        if len(str1) < len(str2):
            short_str = str1
            long_str = str2
        else:
            short_str = str2
            long_str = str1
        initial_short = short_str
        return recursive_function(short_str, long_str, initial_short)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with 0s, one for each temperature
        res = [0] * len(temperatures)
        # Initialize an empty stack to keep track of temperatures and their indices
        stack = []

        # Iterate over the list of temperatures with their indices
        for i, t in enumerate(temperatures):
            # While stack is not empty and the current temperature is greater than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                # Pop the temperature and its index from the stack
                stackT, stackInd = stack.pop()
                # Calculate the number of days to wait for a warmer temperature
                res[stackInd] = i - stackInd
            # Push the current temperature and its index onto the stack
            stack.append((t, i))

        # Return the result list
        return res
